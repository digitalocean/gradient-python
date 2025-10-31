#!/usr/bin/env python3
"""
FastAPI Integration Example for Gradient SDK

This example demonstrates how to integrate Gradient SDK with FastAPI
to create AI-powered REST API endpoints.
"""

import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn

# Import Gradient SDK
from gradient import Gradient
from gradient._utils import PaginationHelper, StreamProcessor

# Initialize FastAPI app
app = FastAPI(
    title="Gradient AI API",
    description="AI-powered API using Gradient SDK",
    version="1.0.0"
)

# Initialize Gradient client
gradient_client = Gradient(
    access_token=os.getenv("DIGITALOCEAN_ACCESS_TOKEN"),
    model_access_key=os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
    agent_access_key=os.getenv("GRADIENT_AGENT_ACCESS_KEY"),
)

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    model: str = "llama3.3-70b-instruct"
    stream: bool = False
    max_tokens: Optional[int] = None

class ChatResponse(BaseModel):
    response: str
    model: str
    usage: Optional[dict] = None

class ImageRequest(BaseModel):
    prompt: str
    size: str = "1024x1024"

class AgentRequest(BaseModel):
    message: str
    agent_endpoint: Optional[str] = None

# Utility functions
def get_paginated_models(page: int = 1, per_page: int = 20):
    """Get paginated list of models."""
    helper = PaginationHelper(page_size=per_page, max_pages=10)
    return helper.paginate(gradient_client.models.list, page=page, per_page=per_page)

# API Routes
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Gradient AI API", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

@app.get("/models")
async def list_models(page: int = 1, per_page: int = 20, format: str = "json"):
    """List available models with pagination."""
    try:
        models = get_paginated_models(page, per_page)

        if format == "simple":
            return {"models": [getattr(m, 'name', str(m)) for m in models]}

        return {
            "models": models,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": len(models)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch models: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    """Chat completion endpoint."""
    try:
        messages = [{"role": "user", "content": request.message}]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=request.model,
            max_tokens=request.max_tokens,
            stream=False
        )

        return ChatResponse(
            response=response.choices[0].message.content,
            model=request.model,
            usage=getattr(response, 'usage', None)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat completion failed: {str(e)}")

@app.post("/chat/stream")
async def chat_completion_stream(request: ChatRequest):
    """Streaming chat completion endpoint."""
    try:
        messages = [{"role": "user", "content": request.message}]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=request.model,
            max_tokens=request.max_tokens,
            stream=True
        )

        def generate():
            processor = StreamProcessor()
            processor.add_handler("text", lambda event: event.get("content", ""))

            for chunk in response:
                if hasattr(chunk, 'choices') and chunk.choices:
                    content = chunk.choices[0].delta.content if hasattr(chunk.choices[0], 'delta') else ""
                    if content:
                        yield f"data: {content}\n\n"

            yield "data: [DONE]\n\n"

        return StreamingResponse(
            generate(),
            media_type="text/plain",
            headers={"Content-Type": "text/event-stream"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Streaming chat failed: {str(e)}")

@app.post("/images/generate")
async def generate_image(request: ImageRequest):
    """Image generation endpoint."""
    try:
        response = gradient_client.images.generate(prompt=request.prompt)

        return {
            "images": response.data if hasattr(response, 'data') else [],
            "prompt": request.prompt
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")

@app.get("/agents")
async def list_agents():
    """List available agents."""
    try:
        response = gradient_client.agents.list()
        agents = response.agents if hasattr(response, 'agents') else []

        return {
            "agents": [
                {
                    "name": getattr(agent, 'name', 'Unknown'),
                    "uuid": getattr(agent, 'uuid', 'Unknown'),
                    "status": getattr(agent, 'status', 'Unknown')
                }
                for agent in agents
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch agents: {str(e)}")

@app.post("/agents/chat")
async def agent_chat(request: AgentRequest):
    """Chat with an agent."""
    try:
        # Use agent-specific client if endpoint provided
        client = gradient_client
        if request.agent_endpoint:
            from gradient import Gradient as AgentGradient
            client = AgentGradient(
                agent_access_key=os.getenv("GRADIENT_AGENT_ACCESS_KEY"),
                agent_endpoint=request.agent_endpoint,
            )

        response = client.agents.chat.completions.create(
            messages=[{"role": "user", "content": request.message}],
            model="llama3.3-70b-instruct"
        )

        return {
            "response": response.choices[0].message.content,
            "agent_endpoint": request.agent_endpoint
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent chat failed: {str(e)}")

@app.get("/stats")
async def get_stats():
    """Get API usage statistics."""
    try:
        # This is a simplified example - in production you'd track real metrics
        return {
            "status": "operational",
            "models_available": len(get_paginated_models()),
            "features": [
                "chat_completion",
                "image_generation",
                "agent_chat",
                "streaming_support",
                "pagination"
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")

if __name__ == "__main__":
    # Check for required environment variables
    required_vars = ["DIGITALOCEAN_ACCESS_TOKEN", "GRADIENT_MODEL_ACCESS_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set them before running the server.")
        exit(1)

    print("🚀 Starting Gradient AI API server...")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔗 OpenAPI Schema: http://localhost:8000/openapi.json")

    uvicorn.run(
        "fastapi_integration:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )