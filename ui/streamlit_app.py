import sys
from pathlib import Path

import streamlit as st
from PyPDF2 import PdfReader
from agents.contradiction_detector import detect_contradictions
from agents.citation_propagator import propagate_citations
from agents.severity_assessor import generate_synthesis
#from agents.triage_agent import triage_contradictions

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

st.set_page_config(page_title="Research Integrity Network", layout="centered")

st.title("🕵️‍♂️ Research Integrity Network Demo")
st.caption("Find research contradictions, map citation impact, and prioritize what matters—all from either a claim or a paper PDF!")

# User choice: claim or PDF
input_type = st.radio(
    "How would you like to analyze a research claim?",
    ("Enter a claim", "Upload a PDF")
)

claim = None

if input_type == "Enter a claim":
    claim = st.text_input("Enter your research claim (ex: 'LLMs are not good at reasoning'):")
elif input_type == "Upload a PDF":
    uploaded_file = st.file_uploader("Upload your research paper as PDF", type=["pdf"])
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        claim = pdf_text  # use extracted text as the claim to analyze

# Hard-coded sample papers dataset
papers = [
    {"title": "LLMs excel at reasoning", "abstract": "A large-scale study shows LLMs are strong at reasoning tasks."},
    {"title": "Limitations of LLM reasoning", "abstract": "Some limitations exist, needs further research."}
]

if st.button("🔎 Analyze Research Claim") and claim:
    # Initialize variables to prevent NameError
    contradictions = []
    citation_cascades = {}
    
    try:
        # Step 1: Detect contradictions
        contradictions = detect_contradictions(claim)
        st.markdown("### 1️⃣ Relevant Papers Found")
        if contradictions and len(contradictions) > 0:
            for paper in contradictions:
                with st.expander(paper["title"]):
                    st.write(paper["excerpt"])
        else:
            st.info("No contradictory papers found.")
            contradictions = []  # Ensure it's an empty list

        # Step 2: Propagate citations from contradicted papers
        if contradictions and len(contradictions) > 0:
            with st.spinner("Searching for citation cascades via Perplexity..."):
                citation_cascades = propagate_citations(contradictions)
            st.markdown("### 2️⃣ Citation Cascades from Contradicted Papers")
            if citation_cascades:
                for paper_title, citing_papers in citation_cascades.items():
                    st.write(f"**{paper_title}** is cited by:")
                    if citing_papers and len(citing_papers) > 0:
                        for citing_text in citing_papers:
                            st.write(f"• {citing_text}")
                    else:
                        st.write("_No citing papers found via web search_")
            else:
                st.info("No citation cascades found.")
        else:
            st.info("No citation cascades to show.")
            citation_cascades = {}  # Ensure it's an empty dict

        # FINAL STEP: Generate the full research synthesis
        with st.spinner("Synthesizing findings into a research strategy using NeMotron..."):
            # The Synthesis Agent takes all prior context to generate the final output
            synthesis_text = generate_synthesis(claim, contradictions, citation_cascades)
            
        st.markdown("### 💡 Recommended Research Strategy")
        st.markdown(synthesis_text) # Display the final, high-quality narrative

        st.markdown("---")
        st.success("Analysis Complete!")

        # Optional: Allow users to see the raw data the synthesis was based on
        with st.expander("View Raw Data Found by Agents"):
            st.json({"claim": claim, "papers_found": contradictions, "related_discussions": citation_cascades})
            
    except Exception as e:
        st.error(f"An error occurred during analysis: {str(e)}")
        st.info("Please try again with a different claim or check your internet connection.")
