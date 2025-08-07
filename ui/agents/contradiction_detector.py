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
            "You are an expert scientific researcher. Identify recent academic papers or "
            "articles that directly address or contradict the following research claim. "
            "For each, provide the title and a brief excerpt supporting the contradiction. "
            "Only include papers found via real-time web search. Format each as: "
            "Title: [title] | Excerpt: [relevant text]"
        )

        response = client.chat.completions.create(
            model="sonar-reasoning",  # Uses Perplexity's real-time web search model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": claim},
            ],
            temperature=0.2,
        )

        # Parse the results—these are actual web-search-derived contradictions.
        results = []
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            if content:
                for line in content.strip().split("\n"):
                    if "Title:" in line:
                        parts = line.split("| Excerpt:")
                        title = parts[0].replace("Title:", "").strip()
                        excerpt = parts[1].strip() if len(parts) > 1 else ""
                        if title:  # Only add if title is not empty
                            results.append({"title": title, "excerpt": excerpt})

        return results
        
    except Exception as e:
        print(f"Error in detect_contradictions: {str(e)}")
        return []
