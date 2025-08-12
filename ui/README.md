# Research Integrity Network - Modern UI

A beautiful, modern TypeScript React application for the Research Integrity Network with sleek animations and state-of-the-art design. This application provides a modern web interface for analyzing research claims using AI agents.

## 🎨 Features

- **Modern Design**: Sleek, gradient-based UI with smooth animations
- **Real-time Feedback**: Beautiful loading spinners for each analysis step
- **Responsive Layout**: Works perfectly on desktop and mobile
- **TypeScript**: Fully typed for better development experience
- **Framer Motion**: Smooth animations and transitions
- **Tailwind CSS**: Modern utility-first styling
- **PDF Upload Support**: Drag and drop PDF files for analysis
- **Text Input Support**: Direct claim entry for quick analysis
- **Real AI Analysis**: Powered by Perplexity API for live web search and contradiction detection

## 🚀 Quick Start

### Prerequisites

1. **Install Node.js** (v18 or higher):
   - Download from [nodejs.org](https://nodejs.org/)
   - Or use Windows Package Manager: `winget install OpenJS.NodeJS`

2. **Install Git** (if not already installed):
   - Download from [git-scm.com](https://git-scm.com/)

3. **Set up environment variables**:
   - Copy `env.example` to `.env` in the root directory
   - Add your Perplexity API key to the `.env` file:
     ```
     PERPLEXITY_API_KEY=your_actual_api_key_here
     ```
   - Get your free API key from: https://www.perplexity.ai/settings/api

### Installation & Running

#### Step 1: Start the Python Backend
1. **Navigate to the project root**:
   ```bash
   cd research-demo
   ```

2. **Activate the Python virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server**:
   ```bash
   python ui/backend_server.py
   ```
   The backend will run on `http://localhost:8501`

#### Step 2: Start the React Frontend
1. **Open a new terminal** and navigate to the UI directory:
   ```bash
   cd ui
   ```

2. **Add Node.js to PATH** (if not already done):
   ```powershell
   $env:PATH = "C:\Program Files\nodejs;" + $env:PATH
   ```

3. **Install dependencies**:
   ```bash
   npm install
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   ```

5. **Open your browser** and go to `http://localhost:3000`

## 🏗️ Project Structure

```
research-demo/
├── ui/
│   ├── src/                    # React frontend
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
└── .env                      # Environment variables
```

## 🎯 User Interface

The application features a modern, intuitive interface:

### Main Interface
- **Header**: Clean logo and title with descriptive tagline
- **Input Selection**: Toggle between "Enter a claim" and "Upload a PDF"
- **PDF Upload Area**: Drag-and-drop interface with visual feedback
- **Text Input**: Large textarea for direct claim entry
- **Analysis Button**: Prominent call-to-action with loading states

### Visual Design
- **Color Scheme**: Blue gradient primary colors with clean whites and grays
- **Typography**: Modern, readable fonts with proper hierarchy
- **Spacing**: Generous whitespace for clean, uncluttered appearance
- **Animations**: Smooth transitions and loading states throughout

## 🎯 Workflow

The application provides a streamlined research analysis workflow:

1. **Input Selection**: Choose between text input or PDF upload
2. **Claim Entry**: Enter your research claim or upload a PDF document
3. **Analysis**: Click "🔎 Analyze Research Claim" to start the process
4. **Step 1 - Text Extraction**: Extract text from PDF (if uploaded)
5. **Step 2 - Detection**: Beautiful loading spinner while searching for contradictions via Perplexity
6. **Step 3 - Propagation**: Animated loading while mapping citation cascades
7. **Step 4 - Synthesis**: Loading animation while formulating research strategy
8. **Results**: Beautiful cards displaying all findings with smooth animations

## 🔧 Development

### Available Scripts

- `npm run dev` - Start React development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Backend API Endpoints

- `POST /detect_contradictions` - Find contradictory research papers
- `POST /propagate_citations` - Map citation cascades
- `POST /generate_synthesis` - Generate research strategy
- `POST /extract_text` - Extract text from PDF files

### Key Technologies

- **React 18** - Modern React with hooks
- **TypeScript** - Type safety and better DX
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **FastAPI** - Python backend API
- **Perplexity AI** - Real-time web search and analysis

## 🌐 API Integration

The UI communicates with the Python backend via REST API:

- **Error handling**: Graceful fallbacks for API failures
- **Loading states**: Beautiful loading animations
- **Type safety**: Full TypeScript integration
- **Real-time analysis**: Live web search via Perplexity API

## 🚀 Deployment

For production deployment:

```bash
# Build the frontend
cd ui
npm run build

# Start the backend server
python ui/backend_server.py
```

## 🎯 Current Status

✅ **Node.js Installation**: Successfully installed and configured  
✅ **Dependencies**: All React and Python dependencies installed  
✅ **Development Servers**: Both frontend and backend running  
✅ **UI Components**: Modern, responsive interface implemented  
✅ **PDF Upload**: Drag-and-drop functionality working  
✅ **Text Input**: Direct claim entry supported  
✅ **Backend API**: FastAPI server with AI agents  
✅ **Real Analysis**: Perplexity API integration for live web search  
✅ **Streamlit Removal**: Successfully removed all Streamlit dependencies  

---

**Note**: This modern UI provides a significantly enhanced user experience with beautiful animations, modern design principles, improved usability, and real AI-powered analysis capabilities.
