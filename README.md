# 🌊 Cascade - AI Research Analysis

> **New finding just dropped? Find out what it means for your research team in seconds**

[![Cascade Demo](https://img.shields.io/badge/Demo-Live%20Preview-blue?style=for-the-badge&logo=react)](http://localhost:3000)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-blue.svg?style=for-the-badge&logo=react)](https://reactjs.org)

---

## 🚀 **What is Cascade?**

**Cascade** is an AI-powered research analysis platform that instantly maps the impact chain of your research claims. Upload a paper or paste a claim, and watch as our AI agents orchestrate to:

- 🔍 **Detect Contradictions** - Find papers that challenge your findings
- 🌊 **Map Citation Cascades** - Trace how ideas ripple through academia  
- ⚡ **Generate Strategic Insights** - Get actionable research directions

**Powered by NVIDIA NeMo** and real-time Perplexity API integration.

---

## 🎯 **Why Cascade?**

### **For Researchers**
- **Instant Validation** - Know within seconds if your breakthrough has been debunked
- **Citation Intelligence** - See exactly who's building on (or contradicting) your work
- **Strategic Planning** - Get clear next steps for your research direction

### **For Research Teams**
- **Collaborative Analysis** - Share findings and get team-wide insights
- **Literature Review** - Automate the tedious process of finding related work
- **Impact Assessment** - Understand the broader implications of your research

### **For Academic Institutions**
- **Quality Assurance** - Ensure research claims are thoroughly vetted
- **Resource Optimization** - Focus research efforts on high-impact areas
- **Knowledge Synthesis** - Bridge gaps between different research domains

---

## 🛠️ **Quick Start**

### **1. Clone & Setup**
```bash
git clone <repository-url>
cd research-demo
pip install -r requirements.txt
```

### **2. Configure API**
```bash
cp env.example .env
# Add your Perplexity API key to .env
# Get free key: https://www.perplexity.ai/settings/api
```

### **3. Launch Cascade**
```bash
# Terminal 1: Start backend
python ui/backend_server.py

# Terminal 2: Start frontend  
cd ui
npm install
npm run dev
```

### **4. Experience the Magic**
Open `http://localhost:3000` and upload your research paper or paste a claim!

---

## 🔬 **How It Works**

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

---

## 🎨 **Features**

### **Real-Time Analysis**
- ⚡ **Instant Results** - Get insights in seconds, not hours
- 🔄 **Live Updates** - Progressive UI with step-by-step progress
- 🌐 **Web Integration** - Real-time search via Perplexity API

### **Advanced AI Agents**
- 🤖 **Modular Architecture** - Specialized agents for each analysis step
- 🧠 **NVIDIA NeMo Powered** - State-of-the-art AI orchestration
- 📊 **Citation Intelligence** - Deep understanding of academic networks

### **Beautiful Interface**
- 🎨 **Modern UI** - Clean, professional design
- 📱 **Responsive** - Works on desktop and mobile
- ⚡ **Fast Performance** - Optimized for speed and reliability

---

## 🏗️ **Architecture**

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

### **Tech Stack**
- **Frontend**: React 18, TypeScript, Tailwind CSS, Framer Motion
- **Backend**: FastAPI, Python 3.8+, Uvicorn
- **AI**: Perplexity API, NVIDIA NeMo integration
- **Build**: Vite, npm

---

## 🚀 **Deployment**

### **Local Development**
```bash
# Backend
python ui/backend_server.py

# Frontend  
cd ui && npm run dev
```

### **Production Ready**
- ✅ **Docker Support** - Containerized deployment
- ✅ **Cloud Compatible** - Works on AWS, GCP, Azure
- ✅ **Scalable** - Handles multiple concurrent users

---

## 🤝 **Contributing**

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Development Guidelines**
- 🧪 **Test Everything** - Ensure all features work correctly
- 📝 **Document Changes** - Update docs for new features
- 🎨 **Follow Style** - Maintain consistent code formatting

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **NVIDIA NeMo** - For powerful AI orchestration capabilities
- **Perplexity AI** - For real-time research search and analysis
- **Open Source Community** - For the amazing tools that make this possible

---

## 📞 **Support**

- 🐛 **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- 📧 **Email**: [your-email@domain.com]

---

## ⭐ **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/your-repo&type=Date)](https://star-history.com/#your-username/your-repo&Date)

---

**Ready to revolutionize your research workflow?** 🚀

**[Get Started Now →](http://localhost:3000)**

---

*Built with ❤️ by researchers, for researchers*
