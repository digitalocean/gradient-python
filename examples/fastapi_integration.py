#!/usr/bin/env python3
"""
Gradient FastAPI Integration Example

This example demonstrates how to integrate Gradient with FastAPI to create
a web API for AI-powered applications.
"""

import os
import time
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager

try:
    from fastapi import FastAPI, HTTPException, BackgroundTasks
    from fastapi.responses import StreamingResponse
    from pydantic import BaseModel, Field
    import uvicorn
except ImportError:
    print("FastAPI not installed. Install with: pip install fastapi uvicorn")
    exit(1)

from gradient import Gradient, AsyncGradient


# Pydantic models for request/response
class ChatRequest(BaseModel):
    messages: List[Dict[str, str]] = Field(..., description="List of chat messages")
    model: str = Field(default="llama3.3-70b-instruct", description="Model to use")
    temperature: Optional[float] = Field(default=0.7, description="Sampling temperature")
    max_tokens: Optional[int] = Field(default=None, description="Maximum tokens to generate")
    stream: bool = Field(default=False, description="Stream the response")


class ImageRequest(BaseModel):
    prompt: str = Field(..., description="Image generation prompt")
    model: str = Field(default="gpt-image-1", description="Image model to use")
    size: Optional[str] = Field(default=None, description="Image size")
    quality: Optional[str] = Field(default=None, description="Image quality")
    stream: bool = Field(default=False, description="Stream generation progress")


class BatchRequest(BaseModel):
    requests: List[Dict[str, Any]] = Field(..., description="List of requests to process")
    max_concurrent: int = Field(default=3, description="Maximum concurrent requests")


# Global clients
gradient_client: Optional[Gradient] = None
async_gradient_client: Optional[AsyncGradient] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    global gradient_client, async_gradient_client

    # Initialize clients on startup
    gradient_client = Gradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        access_token=os.environ.get("DIGITALOCEAN_ACCESS_TOKEN"),
    )

    async_gradient_client = AsyncGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
        access_token=os.environ.get("DIGITALOCEAN_ACCESS_TOKEN"),
    )

    print("Gradient clients initialized")

    yield

    # Cleanup on shutdown
    print("Shutting down Gradient clients")


# Create FastAPI app
app = FastAPI(
    title="Gradient AI API",
    description="AI-powered API using Gradient",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Gradient AI API", "status": "running"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": time.time()}


@app.post("/chat/completions")
async def chat_completion(request: ChatRequest, background_tasks: BackgroundTasks):
    """Chat completion endpoint."""

    if not async_gradient_client:
        raise HTTPException(status_code=500, detail="Client not initialized")

    try:
        if request.stream:
            # Streaming response
            async def generate():
                stream = await async_gradient_client.chat.completions.create(
                    messages=request.messages,
                    model=request.model,
                    temperature=request.temperature,
                    max_tokens=request.max_tokens,
                    stream=True
                )

                async for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                        yield f"data: {chunk.choices[0].delta.content}\n\n"
                    elif chunk.choices and chunk.choices[0].finish_reason:
                        yield f"data: [DONE]\n\n"
                        break

            return StreamingResponse(
                generate(),
                media_type="text/plain",
                headers={"Content-Type": "text/event-stream"}
            )
        else:
            # Regular response
            response = await async_gradient_client.chat.completions.create(
                messages=request.messages,
                model=request.model,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
            )

            return {
                "id": response.id,
                "object": "chat.completion",
                "created": response.created,
                "model": response.model,
                "choices": [
                    {
                        "index": choice.index,
                        "message": {
                            "role": choice.message.role,
                            "content": choice.message.content,
                        },
                        "finish_reason": choice.finish_reason,
                    }
                    for choice in response.choices
                ],
                "usage": response.usage.model_dump() if response.usage else None,
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat completion failed: {str(e)}")


@app.post("/images/generations")
async def generate_image(request: ImageRequest):
    """Image generation endpoint."""

    if not async_gradient_client:
        raise HTTPException(status_code=500, detail="Client not initialized")

    try:
        if request.stream:
            # Streaming image generation
            async def generate():
                stream = await async_gradient_client.images.generate(
                    prompt=request.prompt,
                    model=request.model,
                    stream=True,
                    partial_images=5,  # Enable partial images
                )

                async for event in stream:
                    if hasattr(event, 'data') and event.data:
                        yield f"data: {{\"type\": \"partial\", \"size\": {len(event.data)}}}\n\n"
                    elif hasattr(event, 'url') and event.url:
                        yield f"data: {{\"type\": \"complete\", \"url\": \"{event.url}\"}}\n\n"
                        break

            return StreamingResponse(
                generate(),
                media_type="text/plain",
                headers={"Content-Type": "text/event-stream"}
            )
        else:
            # Regular image generation
            response = await async_gradient_client.images.generate(
                prompt=request.prompt,
                model=request.model,
                size=request.size,
                quality=request.quality,
            )

            return {
                "created": response.created if hasattr(response, 'created') else time.time(),
                "data": [
                    {
                        "url": getattr(response, 'url', None),
                        "revised_prompt": getattr(response, 'revised_prompt', None),
                    }
                ]
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")


@app.post("/batch/chat")
async def batch_chat_completion(request: BatchRequest, background_tasks: BackgroundTasks):
    """Batch chat completion endpoint."""

    if not async_gradient_client:
        raise HTTPException(status_code=500, detail="Client not initialized")

    try:
        from gradient._utils import batch_process_async

        async def process_request(req_data: Dict[str, Any]) -> Dict[str, Any]:
            """Process a single chat request."""
            response = await async_gradient_client.chat.completions.create(
                messages=req_data["messages"],
                model=req_data.get("model", "llama3.3-70b-instruct"),
                temperature=req_data.get("temperature", 0.7),
                max_tokens=req_data.get("max_tokens"),
            )

            return {
                "request": req_data,
                "response": {
                    "content": response.choices[0].message.content if response.choices else "",
                    "usage": response.usage.model_dump() if response.usage else None,
                }
            }

        # Process batch
        results = await batch_process_async(
            request.requests,
            process_request,
            max_concurrent=request.max_concurrent,
        )

        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch processing failed: {str(e)}")


@app.get("/models")
async def list_models():
    """List available models."""

    if not async_gradient_client:
        raise HTTPException(status_code=500, detail="Client not initialized")

    try:
        from gradient._utils import collect_all_pages_async

        models = await collect_all_pages_async(
            async_gradient_client.models.list,
            item_attr='models'
        )

        return {
            "object": "list",
            "data": [
                {
                    "id": model.id,
                    "object": "model",
                    "created": getattr(model, 'created', None),
                    "owned_by": getattr(model, 'owned_by', 'gradient'),
                }
                for model in models
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list models: {str(e)}")


@app.get("/agents")
async def list_agents():
    """List available agents."""

    if not async_gradient_client:
        raise HTTPException(status_code=500, detail="Client not initialized")

    try:
        response = await async_gradient_client.agents.list()

        return {
            "object": "list",
            "data": [
                {
                    "id": agent.id,
                    "object": "agent",
                    "name": agent.name,
                    "description": getattr(agent, 'description', None),
                    "created": getattr(agent, 'created_at', None),
                }
                for agent in response.agents
            ] if hasattr(response, 'agents') and response.agents else []
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list agents: {str(e)}")


def main():
    """Run the FastAPI server."""

    print("Starting Gradient FastAPI Server")
    print("=" * 40)
    print("Make sure to set these environment variables:")
    print("  GRADIENT_MODEL_ACCESS_KEY")
    print("  DIGITALOCEAN_ACCESS_TOKEN (optional)")
    print()
    print("Example requests:")
    print("  curl -X POST http://localhost:8000/chat/completions \\")
    print("    -H 'Content-Type: application/json' \\")
    print("    -d '{\"messages\": [{\"role\": \"user\", \"content\": \"Hello!\"}]}'")
    print()
    print("  curl http://localhost:8000/models")
    print()

    uvicorn.run(
        "fastapi_integration:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()