# Gradient Python SDK Examples

This directory contains examples demonstrating how to use the Gradient Python SDK with various frameworks and for different use cases.

## Available Examples

### Framework Integrations

These examples show how to integrate the Gradient Python SDK with popular web frameworks:

- **[Django Integration](django_integration.py)** - Simple Django views for chat completions, image generation, and agent listing
- **[Flask Integration](flask_integration.py)** - Flask routes demonstrating SDK usage with proper error handling
- **[FastAPI Integration](fastapi_integration.py)** - FastAPI endpoints with Pydantic models and async support

## Running Examples

Each example is a standalone Python script that can be run directly:

```bash
# Make sure you have the required environment variables set
export DIGITALOCEAN_ACCESS_TOKEN="your_token_here"
export GRADIENT_MODEL_ACCESS_KEY="your_model_key_here"
export GRADIENT_AGENT_ACCESS_KEY="your_agent_key_here"
export GRADIENT_AGENT_ENDPOINT="https://your-agent.agents.do-ai.run"

# Run an example
python examples/django_integration.py
```

## Framework-Specific Setup

### Django
The Django example shows how to create a Django view that uses the Gradient SDK for AI-powered responses.

### Flask
The Flask example demonstrates integrating Gradient SDK with Flask routes for web applications.

### FastAPI
The FastAPI example shows how to create async endpoints that leverage the Gradient SDK's async capabilities.

## Environment Variables

All examples require proper authentication setup:

- `DIGITALOCEAN_ACCESS_TOKEN` - For DigitalOcean API operations
- `GRADIENT_MODEL_ACCESS_KEY` - For serverless inference
- `GRADIENT_AGENT_ACCESS_KEY` - For agent-specific operations
- `GRADIENT_AGENT_ENDPOINT` - Your deployed agent endpoint

## Contributing

When adding new examples:

1. Follow the existing naming convention
2. Include comprehensive comments
3. Handle errors appropriately
4. Use environment variables for configuration
5. Add the example to this README