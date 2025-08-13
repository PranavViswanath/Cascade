![image](https://github.com/user-attachments/assets/f571398a-0609-423a-9423-272a28fde995)
# Cascade - AI Research Analysis

> **New finding just dropped? Find out what it means for your research team in seconds**

[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-blue.svg?style=for-the-badge&logo=react)](https://reactjs.org)

---

## Overview

Cascade is an AI-powered research analysis platform that helps researchers validate claims by detecting contradictions, mapping citation cascades, and generating strategic insights. Upload a research paper or paste a claim, and the system will:

1. **Detect Contradictions** - Find papers that challenge your findings
2. **Map Citation Cascades** - Trace how ideas spread through academia  
3. **Generate Strategic Insights** - Provide actionable research directions

Powered by NVIDIA NeMo and real-time Perplexity API integration.

---

## Problem

Research validation is time-consuming and often incomplete. Researchers need to:
- Manually search for contradictory findings
- Trace citation networks to understand impact
- Synthesize insights across multiple papers
- Stay current with rapidly evolving fields

Traditional literature review methods are slow, subjective, and miss important connections.

---

## Solution

Cascade automates research validation through a three-stage AI agent system:

### Stage 1: Contradiction Detection
- Analyzes your research claim using Perplexity API
- Identifies papers that directly contradict your findings
- Extracts key excerpts and reasoning

### Stage 2: Citation Mapping  
- For each contradictory paper, finds papers that cite it
- Maps the impact chain through academia
- Identifies research trends and directions

### Stage 3: Strategic Synthesis
- Combines contradiction and citation data
- Generates actionable research recommendations
- Highlights gaps and opportunities

---

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   AI Agents     │
│   (React/TS)    │◄──►│   (FastAPI)     │◄──►│   (Python)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
    ┌─────────┐            ┌─────────┐            ┌─────────┐
    │  Vite   │            │ Uvicorn │            │Perplexity│
    │  Dev    │            │ Server  │            │   API   │
    └─────────┘            └─────────┘            └─────────┘
```

### Tech Stack
- **Frontend**: React 18, TypeScript, Tailwind CSS, Framer Motion
- **Backend**: FastAPI, Python 3.8+, Uvicorn
- **AI**: Perplexity API, NVIDIA NeMo integration
- **Build**: Vite, npm

---

## Quick Start

### Prerequisites
- Python 3.8+ with virtual environment
- Node.js 18+
- Perplexity API Key ([get here](https://www.perplexity.ai/settings/api))

### Installation

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd research-demo
   pip install -r requirements.txt
   ```

2. **Configure API**:
   ```bash
   cp env.example .env
   # Add your Perplexity API key to .env
   ```

3. **Launch**:
   ```bash
   # Terminal 1: Start backend
   python ui/backend_server.py

   # Terminal 2: Start frontend  
   cd ui
   npm install
   npm run dev
   ```

4. **Access**: Open `http://localhost:3000`

---

## API Endpoints

- `POST /extract_text` - Extract text from PDF files
- `POST /detect_contradictions` - Find contradictory research papers
- `POST /propagate_citations` - Map citation cascades
- `POST /generate_synthesis` - Generate research strategy

---

## Features

### Real-Time Analysis
- Instant results via Perplexity API
- Progressive UI with step-by-step updates
- Live web search integration

### AI Agents
- Modular architecture with specialized agents
- NVIDIA NeMo orchestration
- Citation intelligence and network analysis

### User Interface
- PDF upload with drag-and-drop
- Text input for direct claims
- Responsive design for all devices

---

## Use Cases

### For Researchers
- Validate breakthrough claims before publication
- Identify gaps in existing research
- Understand citation impact of findings

### For Research Teams
- Collaborative literature review
- Automated contradiction detection
- Strategic research planning

### For Academic Institutions
- Quality assurance for research claims
- Resource optimization for high-impact areas
- Knowledge synthesis across domains

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **NVIDIA NeMo** - AI orchestration capabilities
- **Perplexity AI** - Real-time research search and analysis
- **Open Source Community** - Tools and libraries

---

*Built by researchers, for researchers*
