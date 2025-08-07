# agents/citation_propagator.py
import os
from openai import OpenAI

PERPLEXITY_API_KEY = "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"  # or "YOUR_KEY_HERE"

def propagate_citations(contradicted_papers):
    """For each contradicted paper, find recent papers or articles citing it using Perplexity web search."""
    # Input validation
    if not contradicted_papers or not isinstance(contradicted_papers, list) or len(contradicted_papers) == 0:
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
                response = client.chat.completions.create(
                    model="sonar-reasoning",  # Or "sonar-small-chat"; experiment for accuracy
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": f"Find papers citing: {paper_title}"},
                    ],
                    temperature=0.2,
                )

                # Parse the results—these are actual web-search-derived citations
                citing_papers = []
                if response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    if content:
                        for line in content.strip().split("\n"):
                            if "Title:" in line:
                                parts = line.split("| Excerpt:")
                                title = parts[0].replace("Title:", "").strip()
                                excerpt = parts[1].strip() if len(parts) > 1 else ""
                                if title:  # Only add if title is not empty
                                    citing_papers.append(f"{title}: {excerpt}")

                citation_cascades[paper_title] = citing_papers
                
            except Exception as e:
                print(f"Error processing paper '{paper_title}': {str(e)}")
                citation_cascades[paper_title] = []

        return citation_cascades
        
    except Exception as e:
        print(f"Error in propagate_citations: {str(e)}")
        return {}

