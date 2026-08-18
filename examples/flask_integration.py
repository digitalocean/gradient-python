#!/usr/bin/env python3
"""
Flask Integration Example for Gradient Python SDK

This example demonstrates how to integrate the Gradient Python SDK
with a Flask application to create AI-powered endpoints.

Requirements:
- Flask
- gradient (this SDK)

Setup:
1. Install dependencies: pip install flask gradient
2. Set environment variables (see below)
3. Run: python flask_integration.py

Environment Variables Required:
- DIGITALOCEAN_ACCESS_TOKEN
- GRADIENT_MODEL_ACCESS_KEY
"""

import os
from flask import Flask, request, jsonify

# Gradient SDK imports
from gradient import Gradient

app = Flask(__name__)

# Initialize Gradient client
gradient_client = Gradient(
    access_token=os.getenv("DIGITALOCEAN_ACCESS_TOKEN"),
    model_access_key=os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
)


@app.route('/api/chat', methods=['POST'])
def chat_completion():
    """
    Flask endpoint for chat completions using Gradient SDK.

    Expects JSON payload:
    {
        "messages": [{"role": "user", "content": "Hello!"}],
        "model": "llama3.3-70b-instruct"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON payload required"}), 400

        messages = data.get("messages", [])
        model = data.get("model", "llama3.3-70b-instruct")

        if not messages:
            return jsonify({"error": "Messages are required"}), 400

        response = gradient_client.chat.completions.create(
            messages=messages,
            model=model,
        )

        return jsonify({
            "response": response.choices[0].message.content,
            "model": response.model,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/images/generate', methods=['POST'])
def image_generation():
    """
    Flask endpoint for image generation using Gradient SDK.

    Expects JSON payload:
    {
        "prompt": "A beautiful sunset over mountains"
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON payload required"}), 400

        prompt = data.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        response = gradient_client.images.generate(prompt=prompt)

        return jsonify({
            "image_url": response.data[0].url,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/agents', methods=['GET'])
def list_agents():
    """
    Flask endpoint to list available agents.

    Query parameters:
    - limit: Maximum number of agents to return (default: 10)
    """
    try:
        limit = int(request.args.get("limit", 10))

        response = gradient_client.agents.list(limit=limit)

        return jsonify({
            "agents": [
                {
                    "uuid": agent.uuid,
                    "name": agent.name,
                }
                for agent in response.agents
            ]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)