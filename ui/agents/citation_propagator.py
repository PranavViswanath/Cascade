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
                "You are an expert scientific researcher. Find academic papers, articles, or publications that explicitly cite, reference, or build upon the following published work. Focus on papers that mention this work in their references, citations, or related work sections. For each citing paper, provide the title in this format: **\"Paper Title\"**. Only include papers that actually cite or reference the target paper, not the target paper itself."
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
                    if content:
                        # Simple parsing - look for **"Title"** format
                        lines = content.strip().split("\n")
                        for line in lines:
                            line = line.strip()
                            
                            # Look for **"Title"** format but exclude the paper being searched for
                            if '**"' in line and '"**' in line:
                                start = line.find('**"') + 3
                                end = line.find('"**', start)
                                if start > 2 and end > start:
                                    title = line[start:end].strip()
                                    # Don't include the paper being searched for itself
                                    if (title and len(title) > 10 and 
                                        title.lower() not in paper_title.lower() and
                                        paper_title.lower() not in title.lower()):
                                        citing_papers.append(title)
                    
                    # Debug: show what papers were found
                    if citing_papers:
                        print(f"✅ Found {len(citing_papers)} citing papers for {paper_title}: {citing_papers[:3]}")
                    else:
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

