#!/usr/bin/env python3
"""
Simple backend server for Research Integrity Network
Directly calls the agents without complex FastAPI setup
"""

import os
import sys
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
import io
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
load_dotenv(env_path, override=True)

# Add the ui directory to the Python path so we can import the agents
sys.path.append(str(Path(__file__).parent))

# Import the agent functions
from agents.contradiction_detector import detect_contradictions
from agents.citation_propagator import propagate_citations
from agents.severity_assessor import generate_synthesis

app = Flask(__name__)
CORS(app)  # Allow all origins for simplicity

def extract_text_from_pdf(pdf_content):
    """Extract text from PDF content"""
    try:
        pdf_reader = PdfReader(io.BytesIO(pdf_content))
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return ""

@app.route('/')
def root():
    return {"message": "Research Integrity Network API is running"}

@app.route('/analyze', methods=['POST'])
def analyze_claim():
    """Main endpoint that runs the full analysis pipeline"""
    try:
        data = request.get_json()
        claim = data.get('claim', '').strip()
        
        if not claim:
            return jsonify({"error": "No claim provided"}), 400
        
        print(f"🔍 Analyzing claim: {claim[:100]}...")
        
        # Check if API key is loaded
        import os
        api_key = os.getenv("PERPLEXITY_API_KEY")
        print(f"🔑 API Key loaded: {'Yes' if api_key and api_key != 'your_perplexity_api_key_here' else 'No'}")
        if api_key:
            print(f"🔑 API Key starts with: {api_key[:10]}...")
        
        # Step 1: Detect contradictions
        print("📊 Step 1: Detecting contradictions...")
        contradictions = detect_contradictions(claim)
        print(f"Found {len(contradictions)} contradictory papers")
        if contradictions:
            for i, paper in enumerate(contradictions):
                print(f"  Paper {i+1}: {paper.get('title', 'No title')[:50]}...")
        
        # Step 2: Propagate citations
        citation_cascades = {}
        if contradictions:
            print("📚 Step 2: Propagating citations...")
            citation_cascades = propagate_citations(contradictions)
            print(f"Found citation cascades for {len(citation_cascades)} papers")
        
        # Step 3: Generate synthesis
        print("💡 Step 3: Generating synthesis...")
        synthesis = generate_synthesis(claim, contradictions, citation_cascades)
        
        # Return all results
        result = {
            "claim": claim,
            "contradictions": contradictions,
            "citation_cascades": citation_cascades,
            "synthesis": synthesis
        }
        
        print("✅ Analysis complete!")
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error in analysis: {str(e)}")
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

@app.route('/extract_text', methods=['POST'])
def extract_text():
    """Extract text from uploaded PDF"""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({"error": "File must be a PDF"}), 400
        
        # Read the PDF file
        pdf_content = file.read()
        text = extract_text_from_pdf(pdf_content)
        
        return jsonify({"text": text})
        
    except Exception as e:
        print(f"Error extracting text: {str(e)}")
        return jsonify({"error": f"Error extracting text: {str(e)}"}), 500

if __name__ == "__main__":
    print("🚀 Starting Research Integrity Network Backend...")
    print("📍 Backend will be available at: http://localhost:8501")
    print("📍 Frontend should be running at: http://localhost:3000")
    print("📝 Make sure you have set up your .env file with PERPLEXITY_API_KEY")
    print("=" * 60)
    
    app.run(host="0.0.0.0", port=8501, debug=True)
