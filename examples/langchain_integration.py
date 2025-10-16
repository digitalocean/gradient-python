#!/usr/bin/env python3
"""
Gradient LangChain Integration Example

This example demonstrates how to use Gradient with LangChain for building
AI-powered applications with conversational memory and tool usage.
"""

import os
from typing import List, Dict, Any

try:
    from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
    from langchain_core.tools import tool
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    from langchain.memory import ConversationBufferMemory
    from langchain.chains import ConversationChain
except ImportError:
    print("LangChain not installed. Install with: pip install langchain langchain-core")
    exit(1)

from gradient import Gradient


class GradientLangChainLLM:
    """LangChain-compatible wrapper for Gradient chat completions."""

    def __init__(self, client: Gradient, model: str = "llama3.3-70b-instruct", **kwargs):
        self.client = client
        self.model = model
        self.default_params = kwargs

    def __call__(self, messages: List[BaseMessage], **kwargs) -> str:
        """Generate a response from a list of messages."""

        # Convert LangChain messages to Gradient format
        gradient_messages = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                gradient_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, AIMessage):
                gradient_messages.append({"role": "assistant", "content": msg.content})
            else:
                # Handle system messages or other types
                gradient_messages.append({"role": "user", "content": str(msg.content)})

        # Merge parameters
        params = {**self.default_params, **kwargs}

        # Make the API call
        response = self.client.chat.completions.create(
            messages=gradient_messages,
            model=self.model,
            **params
        )

        return response.choices[0].message.content

    async def acall(self, messages: List[BaseMessage], **kwargs) -> str:
        """Async version of __call__."""
        # Convert LangChain messages to Gradient format
        gradient_messages = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                gradient_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, AIMessage):
                gradient_messages.append({"role": "assistant", "content": msg.content})
            else:
                gradient_messages.append({"role": "user", "content": str(msg.content)})

        # Merge parameters
        params = {**self.default_params, **kwargs}

        # Make the async API call
        response = await self.client.chat.completions.create(
            messages=gradient_messages,
            model=self.model,
            **params
        )

        return response.choices[0].message.content


# Define some example tools
@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    # This is a mock implementation - in reality you'd call a weather API
    return f"The weather in {location} is sunny and 72°F."


@tool
def calculate(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e}"


def create_gradient_chain_with_tools():
    """Create a LangChain chain with Gradient and tools."""

    # Initialize Gradient client
    client = Gradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
    )

    # Create the LLM wrapper
    llm = GradientLangChainLLM(client, temperature=0.7)

    # Create a prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI assistant with access to tools.

    Current conversation:
    {history}

    Human: {input}

    Assistant: Let me help you with that.

    First, I should understand what you need. You have access to these tools:
    - get_weather: Get weather information for a location
    - calculate: Calculate mathematical expressions

    Think step by step about whether you need to use any tools, then provide your response.
    """)

    # Create the chain
    chain = (
        RunnablePassthrough.assign(
            history=lambda x: x.get("history", "")
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


def create_conversation_with_memory():
    """Create a conversational chain with memory."""

    # Initialize Gradient client
    client = Gradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"),
    )

    # Create the LLM wrapper
    llm = GradientLangChainLLM(client, temperature=0.7)

    # Create memory
    memory = ConversationBufferMemory()

    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    return conversation


def main():
    """Main example function."""

    print("Gradient LangChain Integration Examples")
    print("=" * 50)

    # Check for required environment variables
    if not os.environ.get("GRADIENT_MODEL_ACCESS_KEY"):
        print("Please set GRADIENT_MODEL_ACCESS_KEY environment variable")
        return

    print("\n1. Simple Chat Completion")
    print("-" * 30)

    client = Gradient(model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"))
    llm = GradientLangChainLLM(client)

    messages = [HumanMessage(content="What is the capital of France?")]
    response = llm(messages)
    print(f"Human: {messages[0].content}")
    print(f"Assistant: {response}")

    print("\n2. Conversational Chain with Memory")
    print("-" * 40)

    try:
        conversation = create_conversation_with_memory()

        print("Conversation 1:")
        response1 = conversation.predict(input="My name is Alice.")
        print(f"Assistant: {response1}")

        print("\nConversation 2:")
        response2 = conversation.predict(input="What's my name?")
        print(f"Assistant: {response2}")

    except Exception as e:
        print(f"Conversation example failed: {e}")

    print("\n3. Chain with Tools (Mock Example)")
    print("-" * 35)

    try:
        chain = create_gradient_chain_with_tools()

        # Example with tool usage hint
        result = chain.invoke({
            "input": "What's 15 + 27?",
            "history": ""
        })
        print(f"Query: What's 15 + 27?")
        print(f"Response: {result}")

    except Exception as e:
        print(f"Chain example failed: {e}")

    print("\n4. Async Example")
    print("-" * 20)

    import asyncio

    async def async_example():
        client = Gradient(model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"))
        llm = GradientLangChainLLM(client)

        messages = [HumanMessage(content="Tell me a short joke.")]
        response = await llm.acall(messages)
        print(f"Human: {messages[0].content}")
        print(f"Assistant: {response}")

    try:
        asyncio.run(async_example())
    except Exception as e:
        print(f"Async example failed: {e}")


if __name__ == "__main__":
    main()