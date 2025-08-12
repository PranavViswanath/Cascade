# agents/contradiction_detector.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (ignore if .env file doesn't exist)
try:
    load_dotenv(override=True)
except Exception:
    pass  # Ignore errors loading .env file

# Get API key from environment variable
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not PERPLEXITY_API_KEY:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set. Please set it in your .env file.")

def detect_contradictions(claim: str) -> list:
    """
    Search the web for research papers or content that appears to
    contradict the given claim, using Perplexity API for real-time
    web search. Returns a list of paper titles and relevant excerpts.
    """
    # Input validation
    if not claim or not claim.strip():
        return []
    
    try:
        client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

        # Craft a prompt to find scientific papers that contradict your claim.
        # Perplexity will do live web search and extract sources.
        SYSTEM_PROMPT = (
            "Find academic papers that contradict this research claim. "
            "For each paper, respond with exactly this format:\n"
            "PAPER 1:\n"
            "Title: [paper title]\n"
            "Excerpt: [contradiction excerpt]\n\n"
            "PAPER 2:\n"
            "Title: [paper title]\n"
            "Excerpt: [contradiction excerpt]\n\n"
            "Find at least 2-3 papers that challenge this claim."
        )

        response = client.chat.completions.create(
            model="sonar",  # Use fastest, cheapest model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": claim},
            ],
            temperature=0.2,
        )

        # Parse the results with simpler logic
        results = []
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            print(f"🔍 Contradiction response: {content[:300]}...")
            
            if content:
                # Split by PAPER sections
                papers = content.split("PAPER")
                for paper_section in papers:
                    if "Title:" in paper_section and "Excerpt:" in paper_section:
                        lines = paper_section.strip().split("\n")
                        title = ""
                        excerpt = ""
                        
                        for line in lines:
                            if line.startswith("Title:"):
                                title = line.replace("Title:", "").strip()
                            elif line.startswith("Excerpt:"):
                                excerpt = line.replace("Excerpt:", "").strip()
                        
                        if title and excerpt:
                            results.append({"title": title, "excerpt": excerpt})
            
            # If still no results, try basic parsing
            if not results and "Title:" in content:
                lines = content.split("\n")
                for line in lines:
                    if line.startswith("Title:") or "Title:" in line:
                        # Simple extraction
                        title = line.split("Title:")[-1].strip()
                        if title:
                            results.append({"title": title, "excerpt": "Contradictory evidence found"})
            
            if not results:
                print(f"⚠️ Could not parse contradictions from response: {content[:500]}...")

        # Remove duplicates based on title
        unique_results = []
        seen_titles = set()
        for paper in results:
            title_lower = paper['title'].lower().strip()
            if title_lower not in seen_titles:
                seen_titles.add(title_lower)
                unique_results.append(paper)
        
        return unique_results
        
    except Exception as e:
        print(f"Error in detect_contradictions: {str(e)}")
        return []
