# Gradient SDK Integration Examples

This directory contains integration examples showing how to use the Gradient SDK with popular Python web frameworks and tools.

## Available Examples

### Web Frameworks

#### [FastAPI Integration](fastapi_integration.py)
Complete FastAPI application demonstrating:
- REST API endpoints for chat completions, image generation, and agent interactions
- Streaming responses with Server-Sent Events
- Pagination support for large datasets
- Pydantic models for request/response validation
- Automatic API documentation generation

**Features:**
- Chat completion endpoints (`/chat`, `/chat/stream`)
- Image generation (`/images/generate`)
- Agent interactions (`/agents`, `/agents/chat`)
- Model listing with pagination (`/models`)
- Health checks and statistics

**To run:**
```bash
pip install fastapi uvicorn
export DIGITALOCEAN_ACCESS_TOKEN="your_token"
export GRADIENT_MODEL_ACCESS_KEY="your_key"
python examples/fastapi_integration.py
```

Visit `http://localhost:8000/docs` for interactive API documentation.

#### [Flask Integration](flask_integration.py)
Flask application showcasing:
- RESTful endpoints with proper error handling
- Streaming responses for real-time chat
- Caching and rate limiting integration
- JSON request/response handling
- Logging and monitoring

**Features:**
- All core Gradient SDK features
- Response caching (5-minute TTL)
- Rate limiting (60 requests/minute)
- Comprehensive error handling
- Request logging

**To run:**
```bash
pip install flask
export DIGITALOCEAN_ACCESS_TOKEN="your_token"
export GRADIENT_MODEL_ACCESS_KEY="your_key"
python examples/flask_integration.py
```

#### [Django Integration](django_integration.py)
Django views demonstrating:
- Django-style view functions
- Integration with Django's URL routing
- Streaming HTTP responses
- Django JSON encoder compatibility
- Settings-based configuration

**Features:**
- Django view functions for all endpoints
- URL configuration examples
- Django settings integration
- StreamingHttpResponse for real-time features

**To integrate:**
1. Copy view functions to your Django `views.py`
2. Add URL patterns to `urls.py`
3. Configure environment variables in Django settings
4. Run your Django development server

## Common Features Across Examples

All integration examples demonstrate:

### Core Gradient SDK Features
- **Chat Completions**: Text generation with various models
- **Image Generation**: AI-powered image creation
- **Agent Interactions**: Chat with deployed agents
- **Model Management**: List and query available models

### Advanced Utilities
- **Pagination**: Handle large datasets efficiently
- **Caching**: Reduce API calls with response caching
- **Rate Limiting**: Prevent API quota exhaustion
- **Streaming**: Real-time response handling
- **Error Handling**: Robust error management

### Production Considerations
- **Environment Variables**: Secure credential management
- **Logging**: Request/response monitoring
- **Health Checks**: Service availability monitoring
- **Statistics**: Usage metrics and insights

## Environment Variables

All examples require these environment variables:

```bash
# Required
DIGITALOCEAN_ACCESS_TOKEN="your_digitalocean_token"
GRADIENT_MODEL_ACCESS_KEY="your_model_access_key"

# Optional
GRADIENT_AGENT_ACCESS_KEY="your_agent_access_key"
GRADIENT_AGENT_ENDPOINT="https://your-agent.agents.do-ai.run"
```

## API Endpoints

### Common Endpoints Across Frameworks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/models` | List available models |
| POST | `/chat` | Chat completion |
| POST | `/chat/stream` | Streaming chat completion |
| POST | `/images/generate` | Generate images |
| GET | `/agents` | List agents |
| POST | `/agents/chat` | Chat with agent |
| GET | `/stats` | Usage statistics |
| POST | `/cache/clear` | Clear response cache |

### Request/Response Examples

#### Chat Completion
```json
POST /chat
{
  "message": "What is the capital of France?",
  "model": "llama3.3-70b-instruct",
  "max_tokens": 100
}

Response:
{
  "response": "The capital of France is Paris.",
  "model": "llama3.3-70b-instruct",
  "usage": {"prompt_tokens": 10, "completion_tokens": 8}
}
```

#### Image Generation
```json
POST /images/generate
{
  "prompt": "A beautiful sunset over mountains"
}

Response:
{
  "images": [...],
  "prompt": "A beautiful sunset over mountains"
}
```

#### Streaming Chat
```json
POST /chat/stream
{
  "message": "Tell me a story",
  "model": "llama3.3-70b-instruct"
}

Response: Server-Sent Events stream
data: {"content": "Once"}
data: {"content": " upon"}
data: {"content": " a"}
...
data: [DONE]
```

## Best Practices

### Error Handling
- Always check for required environment variables
- Implement proper HTTP status codes
- Log errors for debugging
- Provide meaningful error messages

### Performance
- Use caching for frequently accessed data
- Implement rate limiting to prevent quota exhaustion
- Consider pagination for large datasets
- Use streaming for real-time responses

### Security
- Never commit API keys to version control
- Use environment variables for credentials
- Implement proper authentication/authorization
- Validate input data thoroughly

### Monitoring
- Add health check endpoints
- Log API usage and errors
- Monitor response times
- Track usage statistics

## Contributing

When adding new integration examples:

1. Follow the existing code structure and patterns
2. Include comprehensive error handling
3. Add proper logging and monitoring
4. Document environment variable requirements
5. Provide clear setup and usage instructions
6. Test with real API credentials when possible

## Support

For issues with these examples:
1. Check that all required environment variables are set
2. Verify API credentials are valid
3. Review the Gradient SDK documentation
4. Check the framework-specific documentation
5. Open an issue in the Gradient Python repository