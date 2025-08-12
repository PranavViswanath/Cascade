# agents/citation_propagator.py
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

def propagate_citations(contradicted_papers):
    """For each contradicted paper, find recent papers or articles citing it using Perplexity web search."""
    print(f"🔍 Citation Agent: Received {len(contradicted_papers) if contradicted_papers else 0} papers")
    print(f"🔍 Citation Agent: Papers data: {contradicted_papers}")
    
    # Input validation
    if not contradicted_papers or not isinstance(contradicted_papers, list) or len(contradicted_papers) == 0:
        print("🔍 Citation Agent: No valid papers received")
        return {}
    

    try:
        client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")
        citation_cascades = {}

        for paper in contradicted_papers:
            # Validate paper structure
            if not isinstance(paper, dict) or "title" not in paper:
                continue
                
            paper_title = paper.get("title", "").strip()
            if not paper_title:
                continue
                
            # Craft a prompt to find papers/articles citing this specific work
            SYSTEM_PROMPT = (
                "You are an expert scientific researcher. Identify any academic papers, articles, web discussions, or blogs that reference or mention the following published work—even informally. For each, provide the title, source, and a brief excerpt or mention pulled from the search result. Format each as: Title: [title] | Source: [link or context] | Excerpt: [relevant text]"
            )

            try:
                print(f"🔍 Citation Agent: Searching citations for: {paper_title}")
                # Use same cheap model as agent 1
                response = client.chat.completions.create(
                    model="sonar",  # Use same model as contradiction detector
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": f"Find papers citing: {paper_title}"},
                    ],
                    temperature=0.2,
                )
                print(f"🔍 Citation Agent: Got response for {paper_title}")

                # Parse the results—these are actual web-search-derived citations
                citing_papers = []
                if response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    print(f"🔍 Citation Agent: Response content for {paper_title}: {content[:300]}...")
                    if content and "Title:" in content:
                        lines = content.strip().split("\n")
                        for line in lines:
                            line = line.strip()
                            if line.startswith("Title:"):
                                if "| Source:" in line or "| Excerpt:" in line:
                                    # Parse format: Title: X | Source: Y | Excerpt: Z
                                    parts = line.split("|")
                                    title = parts[0].replace("Title:", "").strip()
                                    if title:
                                        citing_papers.append(title)
                                else:
                                    # Simple title format
                                    title = line.replace("Title:", "").strip()
                                    if title:
                                        citing_papers.append(title)
                    
                    # If no papers found, log it but keep empty list
                    if not citing_papers:
                        print(f"⚠️ No citing papers found for: {paper_title}")

                # Remove duplicates from citing papers
                unique_citing_papers = []
                seen_papers = set()
                for paper in citing_papers:
                    paper_lower = paper.lower().strip()
                    if paper_lower not in seen_papers:
                        seen_papers.add(paper_lower)
                        unique_citing_papers.append(paper)
                
                citation_cascades[paper_title] = unique_citing_papers
                
            except Exception as e:
                print(f"⚠️ Error processing paper '{paper_title}': {str(e)}")
                print(f"⚠️ Error type: {type(e)}")
                print(f"⚠️ Full error details: {repr(e)}")
                citation_cascades[paper_title] = []

        return citation_cascades
        
    except Exception as e:
        print(f"Error in propagate_citations: {str(e)}")
        return {}

