#!/usr/bin/env python3
"""
Flask Integration Example for Gradient SDK

This example demonstrates how to integrate Gradient SDK with Flask
to create AI-powered web applications.
"""

import os
import json
from typing import List, Optional, Dict, Any
from flask import Flask, request, jsonify, Response, stream_with_context
import logging

# Gradient SDK imports
from gradient import Gradient
from gradient._utils import PaginationHelper, ResponseCache, RateLimiter

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def check_rate_limit():
    """Check if request should be rate limited."""
    if not rate_limiter.allow_request():
        return jsonify({"error": "Rate limit exceeded"}), 429
    return None

# Flask Routes
@app.route("/")
def index():
    """Root endpoint."""
    return jsonify({
        "message": "Gradient AI Flask API",
        "status": "running",
        "endpoints": [
            "/health",
            "/models",
            "/chat",
            "/chat/stream",
            "/images/generate",
            "/agents",
            "/agents/chat",
            "/stats",
            "/cache/clear"
        ]
    })

@app.route("/health")
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})

@app.route("/models")
def list_models():
    """List available models with pagination."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        format_type = request.args.get('format', 'json')

        models = get_paginated_models(page, per_page)

        if format_type == "simple":
            model_names = [getattr(m, 'name', str(m)) for m in models]
            return jsonify({"models": model_names})

        return jsonify({
            "models": models,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": len(models)
            }
        })

    except Exception as e:
        logger.error(f"Failed to fetch models: {str(e)}")
        return jsonify({"error": f"Failed to fetch models: {str(e)}"}), 500

@app.route("/chat", methods=["POST"])
def chat_completion():
    """Chat completion endpoint."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON data required"}), 400

        message = data.get('message')
        model = data.get('model', 'llama3.3-70b-instruct')
        max_tokens = data.get('max_tokens')

        if not message:
            return jsonify({"error": "Message is required"}), 400

        messages = [{"role": "user", "content": message}]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            stream=False
        )

        return jsonify({
            "response": response.choices[0].message.content,
            "model": model,
            "usage": getattr(response, 'usage', None)
        })

    except Exception as e:
        logger.error(f"Chat completion failed: {str(e)}")
        return jsonify({"error": f"Chat completion failed: {str(e)}"}), 500

@app.route("/chat/stream", methods=["POST"])
def chat_completion_stream():
    """Streaming chat completion endpoint."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON data required"}), 400

        message = data.get('message')
        model = data.get('model', 'llama3.3-70b-instruct')
        max_tokens = data.get('max_tokens')

        if not message:
            return jsonify({"error": "Message is required"}), 400

        messages = [{"role": "user", "content": message}]

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            stream=True
        )

        @stream_with_context
        def generate():
            try:
                for chunk in response:
                    if hasattr(chunk, 'choices') and chunk.choices:
                        content = chunk.choices[0].delta.content if hasattr(chunk.choices[0], 'delta') else ""
                        if content:
                            yield f"data: {json.dumps({'content': content})}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as e:
                logger.error(f"Streaming error: {str(e)}")
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return Response(
            generate(),
            content_type="text/event-stream",
            headers={"Cache-Control": "no-cache"}
        )

    except Exception as e:
        logger.error(f"Streaming chat failed: {str(e)}")
        return jsonify({"error": f"Streaming chat failed: {str(e)}"}), 500

@app.route("/images/generate", methods=["POST"])
def generate_image():
    """Image generation endpoint."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON data required"}), 400

        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        response = gradient_client.images.generate(prompt=prompt)

        return jsonify({
            "images": response.data if hasattr(response, 'data') else [],
            "prompt": prompt
        })

    except Exception as e:
        logger.error(f"Image generation failed: {str(e)}")
        return jsonify({"error": f"Image generation failed: {str(e)}"}), 500

@app.route("/agents")
def list_agents():
    """List available agents."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        # Try cache first
        cache_key = "agents_list"
        cached_result = cache.get(cache_key)
        if cached_result:
            return jsonify({"agents": cached_result})

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

        return jsonify({"agents": agent_data})

    except Exception as e:
        logger.error(f"Failed to fetch agents: {str(e)}")
        return jsonify({"error": f"Failed to fetch agents: {str(e)}"}), 500

@app.route("/agents/chat", methods=["POST"])
def agent_chat():
    """Chat with an agent."""
    rate_limit_response = check_rate_limit()
    if rate_limit_response:
        return rate_limit_response

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON data required"}), 400

        message = data.get('message')
        agent_endpoint = data.get('agent_endpoint')

        if not message:
            return jsonify({"error": "Message is required"}), 400

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

        return jsonify({
            "response": response.choices[0].message.content,
            "agent_endpoint": agent_endpoint
        })

    except Exception as e:
        logger.error(f"Agent chat failed: {str(e)}")
        return jsonify({"error": f"Agent chat failed: {str(e)}"}), 500

@app.route("/stats")
def get_stats():
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

        return jsonify(stats)

    except Exception as e:
        logger.error(f"Failed to get stats: {str(e)}")
        return jsonify({"error": f"Failed to get stats: {str(e)}"}), 500

@app.route("/cache/clear", methods=["POST"])
def clear_cache():
    """Clear the response cache."""
    try:
        cache.clear()
        return jsonify({"message": "Cache cleared successfully"})
    except Exception as e:
        logger.error(f"Failed to clear cache: {str(e)}")
        return jsonify({"error": f"Failed to clear cache: {str(e)}"}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Check for required environment variables
    required_vars = ["DIGITALOCEAN_ACCESS_TOKEN", "GRADIENT_MODEL_ACCESS_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set them before running the server.")
        exit(1)

    print("🚀 Starting Gradient AI Flask API server...")
    print("📖 API Documentation: http://localhost:5000/")
    print("🔗 Test endpoints:")
    print("   GET  /health")
    print("   GET  /models")
    print("   POST /chat")
    print("   POST /chat/stream")
    print("   POST /images/generate")
    print("   GET  /agents")
    print("   POST /agents/chat")
    print("   GET  /stats")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        threaded=True
    )