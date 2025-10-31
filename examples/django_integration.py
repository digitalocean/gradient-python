#!/usr/bin/env python3
"""
Django Integration Example for Gradient SDK

This example demonstrates how to integrate Gradient SDK with Django
to create AI-powered web applications.
"""

import os
import json
from typing import List, Optional, Dict, Any

# Django imports
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.serializers.json import DjangoJSONEncoder

# Gradient SDK imports
from gradient import Gradient
from gradient._utils import PaginationHelper, ResponseCache, RateLimiter

# Initialize Gradient client
gradient_client = Gradient(
    access_token=os.getenv("DIGITALOCEAN_ACCESS_TOKEN"),
    model_access_key=os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
    agent_access_key=os.getenv("GRADIENT_AGENT_ACCESS_KEY"),
)

# Initialize utilities
cache = ResponseCache(max_size=100, ttl_seconds=300)  # 5 minute cache
rate_limiter = RateLimiter(requests_per_minute=60)

# Utility functions
def get_paginated_models(page: int = 1, per_page: int = 20) -> List[Any]:
    """Get paginated list of models with caching."""
    cache_key = f"models_page_{page}_per_{per_page}"

    # Try cache first
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result

    # Fetch from API
    helper = PaginationHelper(page_size=per_page, max_pages=10)
    result = helper.paginate(gradient_client.models.list, page=page, per_page=per_page)

    # Cache the result
    cache.set(cache_key, result)
    return result

# Django Views
@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint."""
    return JsonResponse({
        "status": "healthy",
        "service": "Gradient AI Django Integration"
    })

@require_http_methods(["GET"])
def list_models(request):
    """List available models with pagination."""
    try:
        # Rate limiting
        if not rate_limiter.allow_request():
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 20))
        format_type = request.GET.get('format', 'json')

        models = get_paginated_models(page, per_page)

        if format_type == "simple":
            model_names = [getattr(m, 'name', str(m)) for m in models]
            return JsonResponse({"models": model_names})

        response_data = {
            "models": models,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": len(models)
            }
        }

        return JsonResponse(response_data, encoder=DjangoJSONEncoder)

    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch models: {str(e)}"}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def chat_completion(request):
    """Chat completion endpoint."""
    try:
        # Rate limiting
        if not rate_limiter.allow_request():
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        data = json.loads(request.body)
        message = data.get('message')
        model = data.get('model', 'llama3.3-70b-instruct')
        stream = data.get('stream', False)
        max_tokens = data.get('max_tokens')

        if not message:
            return JsonResponse({"error": "Message is required"}, status=400)

        messages = [{"role": "user", "content": message}]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            stream=stream
        )

        if stream:
            def generate():
                for chunk in response:
                    if hasattr(chunk, 'choices') and chunk.choices:
                        content = chunk.choices[0].delta.content if hasattr(chunk.choices[0], 'delta') else ""
                        if content:
                            yield f"data: {json.dumps({'content': content})}\n\n"
                yield "data: [DONE]\n\n"

            return StreamingHttpResponse(
                generate(),
                content_type="text/event-stream"
            )

        return JsonResponse({
            "response": response.choices[0].message.content,
            "model": model,
            "usage": getattr(response, 'usage', None)
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Chat completion failed: {str(e)}"}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def generate_image(request):
    """Image generation endpoint."""
    try:
        # Rate limiting
        if not rate_limiter.allow_request():
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        data = json.loads(request.body)
        prompt = data.get('prompt')

        if not prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)

        response = gradient_client.images.generate(prompt=prompt)

        return JsonResponse({
            "images": response.data if hasattr(response, 'data') else [],
            "prompt": prompt
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Image generation failed: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def list_agents(request):
    """List available agents."""
    try:
        # Rate limiting
        if not rate_limiter.allow_request():
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        # Try cache first
        cache_key = "agents_list"
        cached_result = cache.get(cache_key)
        if cached_result:
            return JsonResponse({"agents": cached_result})

        response = gradient_client.agents.list()
        agents = response.agents if hasattr(response, 'agents') else []

        agent_data = [
            {
                "name": getattr(agent, 'name', 'Unknown'),
                "uuid": getattr(agent, 'uuid', 'Unknown'),
                "status": getattr(agent, 'status', 'Unknown')
            }
            for agent in agents
        ]

        # Cache for 5 minutes
        cache.set(cache_key, agent_data)

        return JsonResponse({"agents": agent_data})

    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch agents: {str(e)}"}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def agent_chat(request):
    """Chat with an agent."""
    try:
        # Rate limiting
        if not rate_limiter.allow_request():
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        data = json.loads(request.body)
        message = data.get('message')
        agent_endpoint = data.get('agent_endpoint')

        if not message:
            return JsonResponse({"error": "Message is required"}, status=400)

        # Use agent-specific client if endpoint provided
        client = gradient_client
        if agent_endpoint:
            from gradient import Gradient as AgentGradient
            client = AgentGradient(
                agent_access_key=os.getenv("GRADIENT_AGENT_ACCESS_KEY"),
                agent_endpoint=agent_endpoint,
            )

        response = client.agents.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model="llama3.3-70b-instruct"
        )

        return JsonResponse({
            "response": response.choices[0].message.content,
            "agent_endpoint": agent_endpoint
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Agent chat failed: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def get_stats(request):
    """Get API usage statistics."""
    try:
        stats = {
            "status": "operational",
            "models_available": len(get_paginated_models()),
            "cache_stats": cache.get_stats(),
            "rate_limiter_status": "active",
            "features": [
                "chat_completion",
                "image_generation",
                "agent_chat",
                "streaming_support",
                "pagination",
                "caching",
                "rate_limiting"
            ]
        }

        return JsonResponse(stats)

    except Exception as e:
        return JsonResponse({"error": f"Failed to get stats: {str(e)}"}, status=500)

@require_http_methods(["POST"])
def clear_cache(request):
    """Clear the response cache."""
    try:
        cache.clear()
        return JsonResponse({"message": "Cache cleared successfully"})
    except Exception as e:
        return JsonResponse({"error": f"Failed to clear cache: {str(e)}"}, status=500)

# URL Configuration Example
"""
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('models/', views.list_models, name='list_models'),
    path('chat/', views.chat_completion, name='chat_completion'),
    path('images/generate/', views.generate_image, name='generate_image'),
    path('agents/', views.list_agents, name='list_agents'),
    path('agents/chat/', views.agent_chat, name='agent_chat'),
    path('stats/', views.get_stats, name='get_stats'),
    path('cache/clear/', views.clear_cache, name='clear_cache'),
]
"""

# Django Settings Example
"""
# settings.py
import os

# Gradient AI Configuration
GRADIENT_ACCESS_TOKEN = os.getenv('DIGITALOCEAN_ACCESS_TOKEN')
GRADIENT_MODEL_ACCESS_KEY = os.getenv('GRADIENT_MODEL_ACCESS_KEY')
GRADIENT_AGENT_ACCESS_KEY = os.getenv('GRADIENT_AGENT_ACCESS_KEY')
GRADIENT_AGENT_ENDPOINT = os.getenv('GRADIENT_AGENT_ENDPOINT')

# Caching and Rate Limiting
GRADIENT_CACHE_TTL = 300  # 5 minutes
GRADIENT_RATE_LIMIT_RPM = 60  # requests per minute
"""

if __name__ == "__main__":
    print("This is a Django integration example.")
    print("To use this in a Django project:")
    print("1. Copy the view functions to your Django views.py")
    print("2. Add the URL patterns to your urls.py")
    print("3. Set the required environment variables")
    print("4. Run your Django server")