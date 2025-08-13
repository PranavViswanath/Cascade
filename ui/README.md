# 🌊 Cascade - Modern UI

A beautiful, modern TypeScript React application for **Cascade** - the AI-powered research analysis platform. This application provides a sleek web interface for analyzing research claims using advanced AI agents.

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

## 🎯 **How Cascade Works**

### **Step 1: Input Your Research**
- 📄 **Upload PDF** - Drop any research paper
- ✍️ **Paste Claim** - Type your research hypothesis

### **Step 2: AI Agent Orchestration**
1. **Contradiction Detector** - Searches for papers that challenge your findings
2. **Citation Mapper** - Traces the impact chain of contradictory papers  
3. **Synthesis Engine** - Generates strategic research recommendations

### **Step 3: Strategic Insights**
- 🎯 **Contradictory Findings** - Papers that challenge your claim
- 🌊 **Citation Cascades** - How ideas spread through academia
- ⚡ **Research Directions** - Actionable next steps for your work

## 🎨 **UI Features**

### **Real-Time Analysis**
- ⚡ **Instant Results** - Get insights in seconds, not hours
- 🔄 **Live Updates** - Progressive UI with step-by-step progress
- 🌐 **Web Integration** - Real-time search via Perplexity API

### **Beautiful Interface**
- 🎨 **Modern UI** - Clean, professional design with gradients
- 📱 **Responsive** - Works on desktop and mobile
- ⚡ **Fast Performance** - Optimized for speed and reliability
- 🎭 **Smooth Animations** - Framer Motion powered transitions

## 🛠️ **Development**

### **Tech Stack**
- **Frontend**: React 18, TypeScript, Tailwind CSS, Framer Motion
- **Build Tool**: Vite
- **Styling**: Tailwind CSS with custom gradients
- **Animations**: Framer Motion
- **State Management**: React hooks

### **Key Components**
- `App.tsx` - Main application component
- `PaperCard.tsx` - Research paper display component
- `SynthesisCard.tsx` - Analysis results component
- `LoadingSpinner.tsx` - Animated loading component
- `api.ts` - API service layer

## 🚀 **Deployment**

### **Local Development**
```bash
npm run dev
```

### **Production Build**
```bash
npm run build
```

### **Preview Production Build**
```bash
npm run preview
```

## 📄 **License**

This project is licensed under the MIT License.

---

**Ready to revolutionize your research workflow?** 🚀

**[Get Started Now →](http://localhost:3000)**

---

*Built with ❤️ by researchers, for researchers*
