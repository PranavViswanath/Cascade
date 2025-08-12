from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import sys
import os
from pathlib import Path

# Add the ui directory to the Python path so we can import the agents
sys.path.append(str(Path(__file__).parent))

# Import the agent functions
from agents.contradiction_detector import detect_contradictions
from agents.citation_propagator import propagate_citations
from agents.severity_assessor import generate_synthesis
from PyPDF2 import PdfReader
import io

app = FastAPI(title="Research Integrity Network API", version="1.0.0")

# Add CORS middleware to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response validation
class ContradictionRequest(BaseModel):
    claim: str

class ContradictionResponse(BaseModel):
    contradictions: List[Dict[str, str]]

class CitationRequest(BaseModel):
    contradictions: List[Dict[str, str]]

class CitationResponse(BaseModel):
    citation_cascades: Dict[str, List[str]]

class SynthesisRequest(BaseModel):
    claim: str
    contradictions: List[Dict[str, str]]
    citationCascades: Dict[str, List[str]]

class SynthesisResponse(BaseModel):
    synthesis: str

class TextExtractionResponse(BaseModel):
    text: str

class AnalyzeRequest(BaseModel):
    claim: str

class AnalyzeResponse(BaseModel):
    claim: str
    contradictions: List[Dict[str, str]]
    citation_cascades: Dict[str, List[str]]
    synthesis: str

@app.get("/")
async def root():
    return {"message": "Research Integrity Network API is running"}

@app.post("/extract_text", response_model=TextExtractionResponse)
async def extract_text_from_pdf(pdf_file: UploadFile = File(...)):
    """
    Extract text from uploaded PDF file
    """
    try:
        if not pdf_file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="File must be a PDF")
        
        # Read the PDF file
        pdf_content = await pdf_file.read()
        pdf_reader = PdfReader(io.BytesIO(pdf_content))
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        return TextExtractionResponse(text=text.strip())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text from PDF: {str(e)}")

@app.post("/detect_contradictions", response_model=ContradictionResponse)
async def detect_contradictions_endpoint(request: ContradictionRequest):
    """
    Detect contradictions for a given research claim
    """
    try:
        contradictions = detect_contradictions(request.claim)
        return ContradictionResponse(contradictions=contradictions)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detecting contradictions: {str(e)}")

@app.post("/propagate_citations", response_model=CitationResponse)
async def propagate_citations_endpoint(request: CitationRequest):
    """
    Propagate citations for contradicted papers
    """
    try:
        citation_cascades = propagate_citations(request.contradictions)
        return CitationResponse(citation_cascades=citation_cascades)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error propagating citations: {str(e)}")

@app.post("/generate_synthesis", response_model=SynthesisResponse)
async def generate_synthesis_endpoint(request: SynthesisRequest):
    """
    Generate synthesis based on claim, contradictions, and citation cascades
    """
    try:
        synthesis = generate_synthesis(request.claim, request.contradictions, request.citationCascades)
        return SynthesisResponse(synthesis=synthesis)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating synthesis: {str(e)}")

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_claim_endpoint(request: AnalyzeRequest):
    """
    Unified endpoint that runs the full analysis pipeline
    """
    try:
        print(f"🔍 Backend: Starting analysis for claim: {request.claim[:100]}...")
        
        # Step 1: Detect contradictions
        print("🔍 Backend: Step 1 - Detecting contradictions...")
        contradictions = detect_contradictions(request.claim)
        print(f"🔍 Backend: Found {len(contradictions)} contradictions")
        
        # Step 2: Propagate citations
        print("🔍 Backend: Step 2 - Propagating citations...")
        citation_cascades = propagate_citations(contradictions)
        print(f"🔍 Backend: Found citations for {len(citation_cascades)} papers")
        
        # Step 3: Generate synthesis
        print("🔍 Backend: Step 3 - Generating synthesis...")
        synthesis = generate_synthesis(request.claim, contradictions, citation_cascades)
        print("🔍 Backend: Analysis complete!")
        
        return AnalyzeResponse(
            claim=request.claim,
            contradictions=contradictions,
            citation_cascades=citation_cascades,
            synthesis=synthesis
        )
    
    except Exception as e:
        print(f"🔍 Backend: Error in analyze_claim_endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error analyzing claim: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8502)

