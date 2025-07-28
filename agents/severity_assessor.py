# agents/synthesis_agent.py
import os
import re
from openai import OpenAI

PERPLEXITY_API_KEY = "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"

def generate_synthesis(claim, contradicted_papers, citation_cascades):
    """
    Generates a direct, practical research briefing for researchers.
    """
    client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

    # Build context from findings
    papers_context = ""
    for paper in contradicted_papers:
        title = paper.get("title", "Unknown")
        excerpt = paper.get("excerpt", "N/A")
        papers_context += f"- {title}: {excerpt}\n"

    SYSTEM_PROMPT = (
        "You are a senior researcher giving direct advice to a colleague. "
        "Respond ONLY with the final advice - no thinking process, no analysis steps. "
        "Write exactly one paragraph starting with 'Based on this new research...' "
        "then add 2-3 bullet points with specific next steps, ending with 'Good luck!' "
        "Be conversational and supportive."
    )

    user_prompt = (
        f"New research uploaded: {claim[:300]}...\n\n"
        f"Related work found:\n{papers_context}\n\n"
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
    output = response.choices[0].message.content
    
    # Remove everything between <think> and </think> tags
    cleaned_output = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL | re.IGNORECASE)
    
    # If the output still starts with thinking indicators, extract just the advice part
    if "based on" in cleaned_output.lower():
        # Find the start of the actual advice
        advice_start = cleaned_output.lower().find("based on")
        if advice_start > 0:
            cleaned_output = cleaned_output[advice_start:]
    
    return cleaned_output.strip()
