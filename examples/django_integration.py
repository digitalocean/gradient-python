#!/usr/bin/env python3
"""
Django Integration Example for Gradient Python SDK

This example demonstrates how to integrate the Gradient Python SDK
with a Django application to create AI-powered endpoints.

Requirements:
- Django
- gradient (this SDK)

Setup:
1. Install dependencies: pip install django gradient
2. Set environment variables (see below)
3. Run: python manage.py runserver

Environment Variables Required:
- DIGITALOCEAN_ACCESS_TOKEN
- GRADIENT_MODEL_ACCESS_KEY
"""

import os
import json
from typing import Dict, Any

# Django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Gradient SDK imports
from gradient import Gradient

# Initialize Gradient client
gradient_client = Gradient(
    access_token=os.getenv("DIGITALOCEAN_ACCESS_TOKEN"),
    model_access_key=os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
)


@csrf_exempt
@require_http_methods(["POST"])
def chat_completion(request) -> JsonResponse:
    """
    Django view for chat completions using Gradient SDK.

    Expects JSON payload:
    {
        "messages": [{"role": "user", "content": "Hello!"}],
        "model": "llama3.3-70b-instruct"
    }
    """
    try:
        data: Dict[str, Any] = json.loads(request.body)
        messages = data.get("messages", [])
        model = data.get("model", "llama3.3-70b-instruct")

        if not messages:
            return JsonResponse({"error": "Messages are required"}, status=400)

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=model,
        )

        return JsonResponse({
            "response": response.choices[0].message.content,
            "model": response.model,
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def image_generation(request) -> JsonResponse:
    """
    Django view for image generation using Gradient SDK.

    Expects JSON payload:
    {
        "prompt": "A beautiful sunset over mountains"
    }
    """
    try:
        data: Dict[str, Any] = json.loads(request.body)
        prompt = data.get("prompt")

        if not prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)

        response = gradient_client.images.generate(prompt=prompt)

        return JsonResponse({
            "image_url": response.data[0].url,
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_http_methods(["GET"])
def list_agents(request) -> JsonResponse:
    """
    Django view to list available agents.

    Query parameters:
    - limit: Maximum number of agents to return (default: 10)
    """
    try:
        limit = int(request.GET.get("limit", 10))

        response = gradient_client.agents.list(limit=limit)

        return JsonResponse({
            "agents": [
                {
                    "uuid": agent.uuid,
                    "name": agent.name,
                }
                for agent in response.agents
            ]
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# URL patterns for Django
"""
# In your Django urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.chat_completion, name='chat_completion'),
    path('api/images/generate/', views.image_generation, name='image_generation'),
    path('api/agents/', views.list_agents, name='list_agents'),
]

# Example usage:
# POST /api/chat/ with {"messages": [{"role": "user", "content": "Hello!"}]}
# POST /api/images/generate/ with {"prompt": "A sunset"}
# GET /api/agents/
"""