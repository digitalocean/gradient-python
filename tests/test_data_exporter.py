"""Tests for data export functionality."""

import tempfile
import os
import pytest
from gradient._utils import DataExporter


class TestDataExporter:
    """Test data export functionality."""

    def test_export_json_string(self):
        """Test JSON export to string."""
        exporter = DataExporter()
        data = {"name": "test", "value": 123}

        result = exporter.export_json(data)
        assert result is not None
        assert '"name": "test"' in result
        assert '"value": 123' in result

    def test_export_json_file(self):
        """Test JSON export to file."""
        exporter = DataExporter()
        data = {"items": [1, 2, 3]}

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_path = f.name

        try:
            result = exporter.export_json(data, temp_path)
            assert result is None  # Should return None when saving to file

            # Verify file contents
            with open(temp_path, 'r') as f:
                content = f.read()
                assert '"items": [1, 2, 3]' in content

        finally:
            os.unlink(temp_path)

    def test_export_csv_string(self):
        """Test CSV export to string."""
        exporter = DataExporter()
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]

        result = exporter.export_csv(data)
        assert result is not None
        assert "name,age" in result
        assert "Alice,30" in result
        assert "Bob,25" in result

    def test_export_csv_file(self):
        """Test CSV export to file."""
        exporter = DataExporter()
        data = [{"id": 1, "status": "active"}]

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            temp_path = f.name

        try:
            result = exporter.export_csv(data, temp_path)
            assert result is None

            # Verify file contents
            with open(temp_path, 'r') as f:
                content = f.read()
                assert "id,status" in content
                assert "1,active" in content

        finally:
            os.unlink(temp_path)

    def test_flatten_response(self):
        """Test response flattening for nested data."""
        exporter = DataExporter()

        nested_data = {
            "user": {
                "name": "John",
                "profile": {
                    "age": 30,
                    "hobbies": ["reading", "coding"]
                }
            },
            "active": True
        }

        flattened = exporter._flatten_response(nested_data)

        # Check flattened keys exist
        assert "user.name" in flattened
        assert "user.profile.age" in flattened
        assert "user.profile.hobbies[0]" in flattened
        assert "user.profile.hobbies[1]" in flattened
        assert "active" in flattened

        # Check values
        assert flattened["user.name"] == "John"
        assert flattened["user.profile.age"] == 30
        assert flattened["active"] is True