# Research Integrity Network

## Overview  
The **Research Integrity Network** is a modular, agentic system built in Python that helps researchers analyze new claims in real time. Simply upload a PDF research paper or paste in a research claim, and the system instantly searches the web for related and contradictory evidence, traces the downstream impact of those findings, and synthesizes a clear, actionable summary. The tool highlights where the scientific field may need to adapt and suggests concrete next steps—streamlining research review, critical discussion, and knowledge synthesis.

## Setup

1. **Clone the repository** or download the project files.
2. **Install dependencies** by running: `pip install -r requirements.txt`
3. **Set up environment variables**:
   - Copy `env.example` to `.env`
   - Add your Perplexity API key to the `.env` file:
     ```
     PERPLEXITY_API_KEY=your_actual_api_key_here
     ```
   - Get your free API key from: https://www.perplexity.ai/settings/api
4. **Start the backend server**: 
   - **Option A**: Run `python start_backend.py` (cross-platform)
   - **Option B**: Run `start_backend.bat` (Windows)
   - **Option C**: Run `python ui/backend_server.py` directly
5. **Start the frontend** (in a new terminal): 
   ```bash
   cd ui
   npm install
   npm run dev
   ```
6. **Open** `http://localhost:3000` in your browser to access the app.

## How It Works

- **Upload a research paper (PDF)** or **paste a research claim**.
- The system **searches the web** for papers, analyses, and discussions that support, contradict, or respond to your claim.
- For each relevant result, it **maps the citation and discussion cascade**, showing how ideas have spread and evolved.
- Finally, it **synthesizes a research briefing**—clearly highlighting key conflicts, gaps, and actionable insights for researchers.
- **Easy cloud deployment** (compatible with Brev, NVIDIA, Jupyter) and ready for live demos.

## License

MIT

**Questions?** Open an issue.  
**Good luck, and happy researching!**
