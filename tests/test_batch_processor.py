"""Tests for batch processing functionality."""

import time
import pytest
from gradient._utils import BatchProcessor


class TestBatchProcessor:
    """Test batch processing functionality."""

    def test_batch_processor_basic(self):
        """Test basic batch processing."""
        processor = BatchProcessor(batch_size=3)
        processed_batches = []

        def process_batch(batch):
            processed_batches.append(batch)
            return f"processed {len(batch)} items"

        processor.set_callback(process_batch)

        # Add items
        processor.add("item1")
        processor.add("item2")
        assert processor.size() == 2

        # Add third item to trigger auto-processing
        processor.add("item3")
        assert processor.size() == 0  # Should be cleared after processing
        assert len(processed_batches) == 1
        assert processed_batches[0] == ["item1", "item2", "item3"]

    def test_batch_processor_timeout(self):
        """Test batch processing with timeout."""
        processor = BatchProcessor(batch_size=10, timeout_seconds=0.1)
        processed_batches = []

        def process_batch(batch):
            processed_batches.append(batch)

        processor.set_callback(process_batch)

        # Add item and wait for timeout
        processor.add("item1")
        time.sleep(0.2)

        # Check timeout should process batch
        processor.check_timeout()
        assert len(processed_batches) == 1
        assert processed_batches[0] == ["item1"]

    def test_batch_processor_force_process(self):
        """Test force processing of batch."""
        processor = BatchProcessor(batch_size=10)
        processed_batches = []

        def process_batch(batch):
            processed_batches.append(batch)

        processor.set_callback(process_batch)

        # Add items without reaching batch size
        processor.add("item1")
        processor.add("item2")
        assert processor.size() == 2

        # Force process
        processor.force_process()
        assert processor.size() == 0
        assert len(processed_batches) == 1
        assert processed_batches[0] == ["item1", "item2"]

    def test_batch_processor_multiple_batches(self):
        """Test processing multiple batches."""
        processor = BatchProcessor(batch_size=2)
        processed_batches = []

        def process_batch(batch):
            processed_batches.append(batch)

        processor.set_callback(process_batch)

        # Add items to create multiple batches
        processor.add("item1")
        processor.add("item2")  # Triggers first batch
        processor.add("item3")
        processor.add("item4")  # Triggers second batch

        assert len(processed_batches) == 2
        assert processed_batches[0] == ["item1", "item2"]
        assert processed_batches[1] == ["item3", "item4"]