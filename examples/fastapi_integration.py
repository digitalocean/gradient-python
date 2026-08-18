#!/usr/bin/env python3
"""
FastAPI Integration Example for Gradient Python SDK

This example demonstrates how to integrate the Gradient Python SDK
with a FastAPI application to create AI-powered endpoints.

Requirements:
- fastapi
- uvicorn
- gradient (this SDK)

Setup:
1. Install dependencies: pip install fastapi uvicorn gradient
2. Set environment variables (see below)
3. Run: python fastapi_integration.py

Environment Variables Required:
- DIGITALOCEAN_ACCESS_TOKEN
- GRADIENT_MODEL_ACCESS_KEY
"""

import os
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Gradient SDK imports
from gradient import Gradient

app = FastAPI(title="Gradient AI API", version="1.0.0")

# Initialize Gradient client
gradient_client = Gradient(
    access_token=os.getenv("DIGITALOCEAN_ACCESS_TOKEN"),
    model_access_key=os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
)


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: str = "llama3.3-70b-instruct"


class ImageRequest(BaseModel):
    prompt: str


@app.post("/api/chat")
async def chat_completion(request: ChatRequest):
    """
    FastAPI endpoint for chat completions using Gradient SDK.
    """
    try:
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=request.model,
        )

        return {
            "response": response.choices[0].message.content,
            "model": response.model,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/images/generate")
async def image_generation(request: ImageRequest):
    """
    FastAPI endpoint for image generation using Gradient SDK.
    """
    try:
        response = gradient_client.images.generate(prompt=request.prompt)

        return {
            "image_url": response.data[0].url,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/agents")
async def list_agents(limit: int = 10):
    """
    FastAPI endpoint to list available agents.
    """
    try:
        response = gradient_client.agents.list(limit=limit)

        return {
            "agents": [
                {
                    "uuid": agent.uuid,
                    "name": agent.name,
                }
                for agent in response.agents
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)