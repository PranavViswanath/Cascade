```markdown
# Research Integrity Network

A modular, agentic system to detect when new research findings contradict established work, analyze the potential impact on future research, and synthesize clear, actionable directions for researchers. Built with Streamlit, Perplexity API, and ready for cloud deployment on NVIDIA GPUs.

---

## ⚡ **Quick Start**

1. **Clone this repository**:
   ```
   git clone https://github.com/YOURUSERNAME/research-integrity-network.git
   cd research-integrity-network
   ```
2. **Install dependencies**:
   ```
   pip install streamlit PyPDF2 openai
   ```
3. **Set your Perplexity API key** in the `agents/` files, or use environment variables.
4. **Run the demo**:
   ```
   streamlit run streamlit_app.py
   ```
5. **Open your browser** to the provided local URL (typically `http://localhost:8501`).

---

## 🏗 **Project Structure**

```
research-integrity-network/
├── agents/
│   ├── contradiction_detector.py    # Live web search for contradictory research
│   ├── citation_propagator.py       # Maps downstream discussion/impact
│   └── synthesis_agent.py           # Generates actionable research advice
├── streamlit_app.py                 # User interface for upload/analysis
└── README.md
```

---

## 🔍 **How It Works**

**1. Upload or Enter a Claim**  
Users can either paste a research claim or upload a PDF (e.g., a new preprint). The system extracts the main text and treats it as the claim to analyze.

**2. Detect Contradictions**  
Using the Perplexity API, the system searches the web for academic papers, articles, and discussions that directly address or contradict the uploaded claim. This is handled by `contradiction_detector.py`.

**3. Map Citation Impact**  
For each contradicted paper, the system attempts to find follow-up papers, articles, or discussions that cite or respond to it. This “citation cascade” helps researchers see where a new finding might ripple through the literature. Handled by `citation_propagator.py`.

**4. Synthesize Actionable Advice**  
Instead of a simple ranked list, the system generates a concise, direct narrative for the researcher:  
- **Summarizes** how the new claim interacts with prior work  
- **Highlights** key tensions or uncertainties in the field  
- **Recommends** 2–3 specific, concrete research directions  
All in clear, non-technical language. This is handled by `synthesis_agent.py`.

**5. Output**  
The researcher sees:  
- **Contradicted papers** and brief excerpts  
- **Relevant follow-up discussions** (if any)  
- **A research briefing**—clear advice on what to do next

---

## 🚀 **Deployment**

**For hackathons or cloud demos** (e.g., Brev, NVIDIA Launchable), use the included bash script to automate environment setup.  
- **Expose port 8501** for the Streamlit UI  
- **Script** installs dependencies, clones the repo, and launches the app

---

## 💡 **Demo Walkthrough**

1. **Launch the app** and upload a PDF (e.g., the Apple paper on LLM reasoning limitations) or enter a claim.
2. **Watch** as the system surfaces contradictory papers and maps potential impact.
3. **Read** the synthesized research briefing, which directly advises you on how your work might need to adapt—and what to explore next.
4. **Share** the live demo URL with judges or collaborators.

---

## 🤖 **Agentic Architecture**

- **Modular Python agents** for contradiction detection, impact propagation, and synthesis.
- **Live, web-powered reasoning**—no static corpus, just real-time research synthesis.
- **Ready for orchestration** (e.g., NVIDIA NeMo Agent Toolkit) as individual tools.
- **Streamlit UI** for quick, visually clear demo.

---

## 📜 **License**

MIT

---

**Questions?**  
Open an issue or reach out to the author.  
**Good luck, and happy researching!**
```
