# agents/synthesis_agent.py
import os
import re
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

def generate_synthesis(claim, contradicted_papers, citation_cascades):
    """
    Generates a direct, practical research briefing for researchers.
    """
    # Input validation
    if not claim or not claim.strip():
        return "No research claim provided. Please enter a valid research claim to analyze."
    
    try:
        client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

        # Build context from findings
        papers_context = ""
        if contradicted_papers and isinstance(contradicted_papers, list) and len(contradicted_papers) > 0:
            for paper in contradicted_papers:
                if isinstance(paper, dict):
                    title = paper.get("title", "Unknown")
                    excerpt = paper.get("excerpt", "N/A")
                    papers_context += f"- {title}: {excerpt}\n"
        else:
            papers_context = "No contradictory papers found in the literature search."

        # Add citation context if available
        citation_context = ""
        if citation_cascades and isinstance(citation_cascades, dict) and len(citation_cascades) > 0:
            citation_context = "\nCitation cascades found:\n"
            for paper_title, citing_papers in citation_cascades.items():
                if citing_papers and len(citing_papers) > 0:
                    citation_context += f"- {paper_title} is cited by {len(citing_papers)} other works\n"
                else:
                    citation_context += f"- {paper_title} has limited citation impact\n"
        else:
            citation_context = "\nNo significant citation cascades found."

        SYSTEM_PROMPT = (
            "You are a strategic research advisor helping researchers navigate conflicting findings and identify high-impact opportunities. "
            "Based on the contradictory papers and their citation cascades, provide a compelling final verdict with actionable next steps. "
            "Structure your response as:\n\n"
            "🚨 **FINAL VERDICT: [Brief assessment of the research landscape]**\n\n"
            "🎯 **TOPICS TO EXPLORE TODAY:**\n"
            "- [Specific research direction 1]\n"
            "- [Specific research direction 2]\n"
            "- [Specific research direction 3]\n\n"
            "⚡ **STRATEGIC INSIGHT:** [One key takeaway about the field]\n\n"
            "Make it exciting, actionable, and emphasize the urgency of these opportunities!"
        )

        # Extract just the titles for simpler analysis
        paper_titles = []
        if contradicted_papers and isinstance(contradicted_papers, list):
            for paper in contradicted_papers:
                if isinstance(paper, dict) and "title" in paper:
                    paper_titles.append(paper["title"])
        
        titles_text = "\n".join([f"- {title}" for title in paper_titles]) if paper_titles else "No contradictory papers found"

        user_prompt = (
            f"Research claim: {claim[:200]}...\n\n"
            f"Contradictory papers found:\n{titles_text}\n\n"
            f"Citation cascades:\n{citation_context}\n\n"
            f"Provide a strategic research briefing with actionable next steps."
        )

        response = client.chat.completions.create(
            model="sonar",  # Use same model as other agents
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
        )

        # Clean the response aggressively to remove thinking process
        if response.choices and len(response.choices) > 0:
            output = response.choices[0].message.content
        else:
            return "Unable to generate synthesis. Please try again."
        
        # Remove everything between <think> and </think> tags
        cleaned_output = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL | re.IGNORECASE)
        
        # If the output still starts with thinking indicators, extract just the advice part
        if "based on" in cleaned_output.lower():
            # Find the start of the actual advice
            advice_start = cleaned_output.lower().find("based on")
            if advice_start > 0:
                cleaned_output = cleaned_output[advice_start:]
        
        return cleaned_output.strip()
        
    except Exception as e:
        print(f"Error in generate_synthesis: {str(e)}")
        return "Unable to generate research strategy. Please try again."
