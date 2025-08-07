# agents/synthesis_agent.py
import os
import re
from openai import OpenAI

PERPLEXITY_API_KEY = "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"

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
            "You are a senior researcher giving direct advice to a colleague. "
            "Respond ONLY with the final advice - no thinking process, no analysis steps. "
            "Write exactly one paragraph starting with 'Based on this new research...' "
            "then add 2-3 bullet points with specific next steps, ending with 'Good luck!' "
            "Be conversational and supportive. If no contradictory papers were found, "
            "focus on suggesting research directions and potential areas to explore."
        )

        user_prompt = (
            f"New research uploaded: {claim[:300]}...\n\n"
            f"Related work found:\n{papers_context}\n"
            f"{citation_context}\n\n"
            f"Give direct advice to the researcher about research directions."
        )

        response = client.chat.completions.create(
            model="sonar",  # Try the basic sonar model first
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
            max_tokens=250
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
        return "Based on this new research, I recommend focusing on exploring the claim through systematic literature review and experimental validation. Consider reaching out to experts in the field for collaboration opportunities. Good luck!"
