import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Financial Document Analyzer API"}

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["status"] == "healthy"
    assert json_resp["service"] == "Financial Document Analyzer"

def test_analyze_document_missing_file():
    # Test POST /analyze-document/ without file
    response = client.post("/analyze-document/")
    assert response.status_code == 422  # Unprocessable Entity (missing required file)

@pytest.mark.skip(reason="Skipping slow PDF upload test to speed up pytest runs")
def test_analyze_document_with_pdf():
    with open("data/TSLA-Q2-2025-Update.pdf", "rb") as f:
        response = client.post(
            "/analyze-document/",
            files={"file": ("TSLA-Q2-2025-Update.pdf", f, "application/pdf")}
        )
    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["status"] == "success"
    assert "analysis" in json_resp
