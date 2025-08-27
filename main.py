from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

from crew import create_financial_crew

def run_crew(query: str, file_path: str):
    financial_crew = create_financial_crew()
    result = financial_crew.kickoff({'query': query, 'file_path': file_path})
    return result

app = FastAPI(title="Financial Document Analyzer API")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""

    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        # Save uploaded file locally
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Default query if empty or None
        if not query:
            query = "Analyze this financial document for investment insights"

        # Run the Crew with given query and file path
        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        # Clean up file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass  # Silently ignore cleanup exceptions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
