# Research Integrity Network - Setup Guide

## 🧹 Project Cleanup Summary

The project has been successfully cleaned up to remove all Streamlit dependencies and ensure proper integration between the TypeScript frontend and Python backend agents.

### ✅ Changes Made

1. **Removed Streamlit Files**:
   - Deleted `ui/streamlit_app.py`
   - Removed `streamlit` from `requirements.txt`
   - Cleaned up duplicate files (`citation_propagator - Copy.py`)

2. **Updated Documentation**:
   - Updated main `README.md` with correct startup instructions
   - Updated `ui/README.md` to reflect current architecture
   - Removed all Streamlit references

3. **Added Convenience Scripts**:
   - `start_backend.py` - Cross-platform backend startup script
   - `start_backend.bat` - Windows-specific backend startup script

4. **Verified Integration**:
   - Backend server (`ui/backend_server.py`) properly configured with FastAPI
   - CORS middleware configured for frontend communication
   - All agent endpoints properly exposed

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** with virtual environment activated
2. **Node.js 18+** installed
3. **Perplexity API Key** (get from https://www.perplexity.ai/settings/api)

### Setup Steps

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env and add your PERPLEXITY_API_KEY
   ```

3. **Install frontend dependencies**:
   ```bash
   cd ui
   npm install
   ```

### Running the Application

#### Option 1: Using Convenience Scripts (Recommended)

1. **Start the backend** (Terminal 1):
   ```bash
   # Cross-platform
   python start_backend.py
   
   # Or on Windows
   start_backend.bat
   ```

2. **Start the frontend** (Terminal 2):
   ```bash
   cd ui
   npm run dev
   ```

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8501

#### Option 2: Manual Startup

1. **Start the backend** (Terminal 1):
   ```bash
   python ui/backend_server.py
   ```

2. **Start the frontend** (Terminal 2):
   ```bash
   cd ui
   npm run dev
   ```

## 🏗️ Current Architecture

```
research-demo/
├── ui/
│   ├── src/                    # React TypeScript frontend
│   │   ├── components/         # React components
│   │   ├── services/          # API services
│   │   └── types.ts           # TypeScript definitions
│   ├── agents/                # Python AI agents
│   │   ├── contradiction_detector.py
│   │   ├── citation_propagator.py
│   │   ├── severity_assessor.py
│   │   └── triage_agent.py
│   ├── backend_server.py      # FastAPI backend server
│   └── package.json           # Frontend dependencies
├── requirements.txt           # Python dependencies
├── start_backend.py          # Backend startup script
├── start_backend.bat         # Windows backend startup script
└── .env                      # Environment variables
```

## 🔧 API Endpoints

The backend provides the following REST API endpoints:

- `GET /` - Health check
- `POST /extract_text` - Extract text from PDF files
- `POST /detect_contradictions` - Find contradictory research papers
- `POST /propagate_citations` - Map citation cascades
- `POST /generate_synthesis` - Generate research strategy

## 🎯 Features

- **Modern TypeScript React Frontend**: Beautiful, responsive UI with animations
- **Real AI Analysis**: Powered by Perplexity API for live web search
- **PDF Upload Support**: Drag and drop PDF files for analysis
- **Text Input Support**: Direct claim entry for quick analysis
- **Modular Agent System**: Separate agents for different analysis tasks
- **FastAPI Backend**: High-performance Python backend with proper CORS support

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**:
   - Backend: Change port in `ui/backend_server.py` (line 123)
   - Frontend: Change port in `ui/vite.config.ts`

2. **API key not found**:
   - Ensure `.env` file exists in project root
   - Verify `PERPLEXITY_API_KEY` is set correctly

3. **CORS errors**:
   - Backend CORS is configured for `http://localhost:3000`
   - If using different port, update `ui/backend_server.py`

4. **Module not found errors**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`
   - For frontend: run `npm install` in `ui/` directory

### Getting Help

- Check the console output for error messages
- Verify all dependencies are installed
- Ensure environment variables are set correctly
- Check that both backend and frontend are running

---

**The application is now ready to use with a modern TypeScript frontend and Python backend agents!**
