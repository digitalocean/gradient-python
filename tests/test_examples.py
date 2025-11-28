"""Tests for example integrations to ensure they work correctly."""

from __future__ import annotations

import os
import pytest
from unittest.mock import Mock, patch, MagicMock

# Skip all tests if environment variables are not set
pytestmark = pytest.mark.skipif(
    not os.getenv("DIGITALOCEAN_ACCESS_TOKEN") or not os.getenv("GRADIENT_MODEL_ACCESS_KEY"),
    reason="Requires DIGITALOCEAN_ACCESS_TOKEN and GRADIENT_MODEL_ACCESS_KEY environment variables"
)


class TestDjangoIntegration:
    """Test Django integration example functions."""

    def test_django_example_imports(self):
        """Test that Django integration example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Django example module
            spec = importlib.util.spec_from_file_location(
                "django_integration",
                "examples/django_integration.py"
            )
            django_module = importlib.util.module_from_spec(spec)
            sys.modules["django_integration"] = django_module

            spec.loader.exec_module(django_module)

            # Check that key functions exist
            assert hasattr(django_module, 'chat_completion')
            assert hasattr(django_module, 'image_generation')
            assert hasattr(django_module, 'list_agents')

        except Exception as e:
            pytest.fail(f"Django integration example has errors: {e}")

    def test_flask_example_imports(self):
        """Test that Flask integration example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Flask example module
            spec = importlib.util.spec_from_file_location(
                "flask_integration",
                "examples/flask_integration.py"
            )
            flask_module = importlib.util.module_from_spec(spec)
            sys.modules["flask_integration"] = flask_module

            spec.loader.exec_module(flask_module)

            # Check that Flask app exists
            assert hasattr(flask_module, 'app')

        except Exception as e:
            pytest.fail(f"Flask integration example has errors: {e}")

    def test_fastapi_example_imports(self):
        """Test that FastAPI integration example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the FastAPI example module
            spec = importlib.util.spec_from_file_location(
                "fastapi_integration",
                "examples/fastapi_integration.py"
            )
            fastapi_module = importlib.util.module_from_spec(spec)
            sys.modules["fastapi_integration"] = fastapi_module

            spec.loader.exec_module(fastapi_module)

            # Check that FastAPI app exists
            assert hasattr(fastapi_module, 'app')

        except Exception as e:
            pytest.fail(f"FastAPI integration example has errors: {e}")


class TestStreamlitIntegration:
    """Test Streamlit integration example."""

    def test_streamlit_example_imports(self):
        """Test that Streamlit integration example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Streamlit example module
            spec = importlib.util.spec_from_file_location(
                "streamlit_integration",
                "examples/streamlit_integration.py"
            )
            streamlit_module = importlib.util.module_from_spec(spec)
            sys.modules["streamlit_integration"] = streamlit_module

            spec.loader.exec_module(streamlit_module)

            # Check that key functions exist
            assert hasattr(streamlit_module, 'chat_completion')
            assert hasattr(streamlit_module, 'generate_image')
            assert hasattr(streamlit_module, 'list_agents')

        except Exception as e:
            pytest.fail(f"Streamlit integration example has errors: {e}")


class TestGradioIntegration:
    """Test Gradio integration example."""

    def test_gradio_example_imports(self):
        """Test that Gradio integration example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Gradio example module
            spec = importlib.util.spec_from_file_location(
                "gradio_integration",
                "examples/gradio_integration.py"
            )
            gradio_module = importlib.util.module_from_spec(spec)
            sys.modules["gradio_integration"] = gradio_module

            spec.loader.exec_module(gradio_module)

            # Check that key functions exist
            assert hasattr(gradio_module, 'chat_completion')
            assert hasattr(gradio_module, 'generate_image')
            assert hasattr(gradio_module, 'list_agents')
            assert hasattr(gradio_module, 'create_demo')

        except Exception as e:
            pytest.fail(f"Gradio integration example has errors: {e}")


class TestStreamlitIntegration:
    """Test Streamlit integration example."""

    def test_streamlit_example_imports(self):
        """Test that Streamlit example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Streamlit example module
            spec = importlib.util.spec_from_file_location(
                "streamlit_integration",
                "examples/streamlit_integration.py"
            )
            streamlit_module = importlib.util.module_from_spec(spec)
            sys.modules["streamlit_integration"] = streamlit_module

            spec.loader.exec_module(streamlit_module)

            # Check that key functions exist
            assert hasattr(streamlit_module, 'chat_completion')
            assert hasattr(streamlit_module, 'generate_image')
            assert hasattr(streamlit_module, 'list_agents')

        except Exception as e:
            pytest.fail(f"Streamlit integration example has errors: {e}")


class TestGradioIntegration:
    """Test Gradio integration example."""

    def test_gradio_example_imports(self):
        """Test that Gradio example can be imported without errors."""
        try:
            import sys
            import importlib.util

            # Load the Gradio example module
            spec = importlib.util.spec_from_file_location(
                "gradio_integration",
                "examples/gradio_integration.py"
            )
            gradio_module = importlib.util.module_from_spec(spec)
            sys.modules["gradio_integration"] = gradio_module

            spec.loader.exec_module(gradio_module)

            # Check that key functions exist
            assert hasattr(gradio_module, 'chat_completion')
            assert hasattr(gradio_module, 'generate_image')
            assert hasattr(gradio_module, 'list_agents')
            assert hasattr(gradio_module, 'create_demo')

        except Exception as e:
            pytest.fail(f"Gradio integration example has errors: {e}")


class TestExampleREADME:
    """Test that the examples README is properly structured."""

    def test_readme_exists_and_has_content(self):
        """Test that README.md exists and has substantial content."""
        readme_path = "examples/README.md"

        assert os.path.exists(readme_path), "examples/README.md should exist"

        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check that it has substantial content
        assert len(content) > 500, "README should have substantial content"

        # Check for key sections
        assert "## Available Examples" in content
        assert "## Framework Integrations" in content
        assert "## Running Examples" in content
        assert "## Environment Variables" in content

        # Check that all examples are mentioned
        assert "Django Integration" in content
        assert "Flask Integration" in content
        assert "FastAPI Integration" in content
        assert "Streamlit Integration" in content
        assert "Gradio Integration" in content
        assert "CLI Example" in content


class TestExampleFileStructure:
    """Test that example files have proper structure."""

    def test_all_example_files_exist(self):
        """Test that all example files exist."""
        example_files = [
            "examples/README.md",
            "examples/django_integration.py",
            "examples/flask_integration.py",
            "examples/fastapi_integration.py",
        ]

        for file_path in example_files:
            assert os.path.exists(file_path), f"Example file {file_path} should exist"

    def test_example_files_have_shebang(self):
        """Test that Python example files have proper shebang."""
        python_files = [
            "examples/django_integration.py",
            "examples/flask_integration.py",
            "examples/fastapi_integration.py",
        ]

        for file_path in python_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                assert first_line.startswith("#!/usr/bin/env python"), \
                    f"{file_path} should have proper shebang"

    def test_example_files_have_docstrings(self):
        """Test that example files have module docstrings."""
        python_files = [
            "examples/django_integration.py",
            "examples/flask_integration.py",
            "examples/fastapi_integration.py",
        ]

        for file_path in python_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

                # Check for module docstring
                lines = content.split('\n')
                assert len(lines) > 3, f"{file_path} should have content"

                # Look for docstring pattern
                docstring_found = False
                in_docstring = False
                for line in lines[:20]:  # Check first 20 lines
                    stripped = line.strip()
                    if stripped.startswith('"""') and not in_docstring:
                        in_docstring = True
                        docstring_found = True
                    elif stripped.endswith('"""') and in_docstring:
                        in_docstring = False
                        break

                assert docstring_found, f"{file_path} should have a module docstring"