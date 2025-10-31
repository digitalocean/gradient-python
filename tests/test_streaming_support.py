"""Tests for streaming support functionality."""

import pytest
from gradient._utils import StreamProcessor, StreamCollector


class TestStreamProcessor:
    """Test stream processor functionality."""

    def test_stream_processor_basic(self):
        """Test basic stream processor functionality."""
        processor = StreamProcessor()

        # Add handler
        results = []
        def text_handler(event):
            results.append(f"processed: {event.get('text', '')}")
            return f"processed: {event.get('text', '')}"

        processor.add_handler("text", text_handler)

        # Process events
        event1 = {"type": "text", "text": "Hello"}
        event2 = {"type": "other", "data": "ignored"}
        event3 = {"type": "text", "text": "World"}

        result1 = processor.process_event(event1)
        result2 = processor.process_event(event2)
        result3 = processor.process_event(event3)

        assert result1 == "processed: Hello"
        assert result2 is None  # No handler for "other"
        assert result3 == "processed: World"
        assert results == ["processed: Hello", "processed: World"]

    def test_stream_processor_remove_handler(self):
        """Test removing event handlers."""
        processor = StreamProcessor()

        def handler(event):
            return "handled"

        processor.add_handler("test", handler)
        assert processor.process_event({"type": "test"}) == "handled"

        processor.remove_handler("test")
        assert processor.process_event({"type": "test"}) is None

    def test_stream_processor_process_stream(self):
        """Test processing entire stream."""
        processor = StreamProcessor()

        def text_handler(event):
            return event.get("text", "").upper()

        processor.add_handler("text", text_handler)

        stream = [
            {"type": "text", "text": "hello"},
            {"type": "other", "data": "ignored"},
            {"type": "text", "text": "world"}
        ]

        results = processor.process_stream(stream)
        assert results == ["HELLO", "WORLD"]

    def test_stream_processor_event_type_extraction(self):
        """Test event type extraction from different formats."""
        processor = StreamProcessor()

        # Test different event formats
        event1 = {"type": "custom"}
        event2 = type('MockEvent', (), {'event': 'mock'})()
        event3 = {"event": "dict_event"}
        event4 = "unknown_format"

        assert processor._get_event_type(event1) == "custom"
        assert processor._get_event_type(event2) == "mock"
        assert processor._get_event_type(event3) == "dict_event"
        assert processor._get_event_type(event4) == "unknown"


class TestStreamCollector:
    """Test stream collector functionality."""

    def test_stream_collector_basic(self):
        """Test basic stream collector functionality."""
        collector = StreamCollector()

        # Collect events
        event1 = {"type": "text", "text": "Hello"}
        event2 = {"type": "text", "text": "World"}
        event3 = {"type": "error", "message": "Something went wrong"}

        collector.collect(event1)
        collector.collect(event2)
        collector.collect(event3)

        # Check all events
        all_events = collector.get_events()
        assert len(all_events) == 3

        # Check filtered events
        text_events = collector.get_events("text")
        assert len(text_events) == 2
        assert all(e["type"] == "text" for e in text_events)

        error_events = collector.get_events("error")
        assert len(error_events) == 1
        assert error_events[0]["type"] == "error"

    def test_stream_collector_aggregation(self):
        """Test event aggregation."""
        collector = StreamCollector()

        # Collect events
        collector.collect({"type": "text", "text": "Hello"})
        collector.collect({"type": "text", "text": "World"})
        collector.collect({"type": "error", "message": "Error 1"})
        collector.collect({"type": "error", "message": "Error 2"})
        collector.collect({"type": "text", "text": "Again"})

        aggregated = collector.get_aggregated()

        # Check text events aggregation
        assert aggregated["text"]["count"] == 3
        assert len(aggregated["text"]["events"]) == 3
        assert aggregated["text"]["last_event"]["text"] == "Again"

        # Check error events aggregation
        assert aggregated["error"]["count"] == 2
        assert len(aggregated["error"]["events"]) == 2
        assert aggregated["error"]["last_event"]["message"] == "Error 2"

    def test_stream_collector_count_events(self):
        """Test event counting."""
        collector = StreamCollector()

        collector.collect({"type": "text"})
        collector.collect({"type": "text"})
        collector.collect({"type": "error"})
        collector.collect({"type": "text"})

        assert collector.count_events() == 4
        assert collector.count_events("text") == 3
        assert collector.count_events("error") == 1
        assert collector.count_events("unknown") == 0

    def test_stream_collector_clear(self):
        """Test clearing collected events."""
        collector = StreamCollector()

        collector.collect({"type": "text"})
        collector.collect({"type": "error"})

        assert collector.count_events() == 2
        assert len(collector.get_aggregated()) == 2

        collector.clear()

        assert collector.count_events() == 0
        assert len(collector.get_aggregated()) == 0