import os
import sys
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("TAVILY_API_KEY", "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")
os.environ.setdefault("OPENAI_API_KEY", "test")
from backend.server import backend_app

@pytest.fixture

def client():
    with backend_app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"status": "Running"}
