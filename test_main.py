from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_endpoint():
    # Using a sample PDF file in the data folder
    sample_pdf_path = "data/sample.pdf"
    
    with open(sample_pdf_path, "rb") as f:
        response = client.post(
            "/analyze",
            files={"file": ("sample.pdf", f, "application/pdf")},
            data={"query": "Analyze Tesla Q2 2025 financials"}
        )
    
    assert response.status_code == 200
    
    json_response = response.json()
    
    assert "status" in json_response
    assert json_response["status"] == "success"
    assert "analysis" in json_response
    assert "file_processed" in json_response
