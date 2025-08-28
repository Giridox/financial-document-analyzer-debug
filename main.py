from fastapi import FastAPI, UploadFile, File, HTTPException
from crewai import Crew, Process
from agents import financial_analyst, document_processor
from task import process_financial_document, analyze_financial_document
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Financial Document Analyzer", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API"}


@app.post("/analyze-document/")
async def analyze_document(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_file_path = tmp_file.name

        # Create crew with tasks using correct task names
        crew = Crew(
            agents=[document_processor, financial_analyst],
            tasks=[process_financial_document, analyze_financial_document],
            process=Process.sequential,
            verbose=True
        )

        # Run the analysis
        result = crew.kickoff(inputs={'document_path': tmp_file_path})

        # Clean up temporary file
        os.unlink(tmp_file_path)

        return {
            "status": "success",
            "analysis": result.raw,
            "file_name": file.filename
        }

    except Exception as e:
        # Clean up on error
        if 'tmp_file_path' in locals():
            try:
                os.unlink(tmp_file_path)
            except:
                pass
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Financial Document Analyzer"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
