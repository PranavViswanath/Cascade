# Research Integrity Network - Modern UI

A beautiful, modern TypeScript React application for the Research Integrity Network with sleek animations and state-of-the-art design.

## 🎨 Features

- **Modern Design**: Sleek, gradient-based UI with smooth animations
- **Real-time Feedback**: Beautiful loading spinners for each analysis step
- **Responsive Layout**: Works perfectly on desktop and mobile
- **TypeScript**: Fully typed for better development experience
- **Framer Motion**: Smooth animations and transitions
- **Tailwind CSS**: Modern utility-first styling
- **PDF Upload Support**: Drag and drop PDF files for analysis
- **Text Input Support**: Direct claim entry for quick analysis

## 🚀 Quick Start

### Prerequisites

1. **Install Node.js** (v18 or higher):
   - Download from [nodejs.org](https://nodejs.org/)
   - Or use Windows Package Manager: `winget install OpenJS.NodeJS`

2. **Install Git** (if not already installed):
   - Download from [git-scm.com](https://git-scm.com/)

### Installation & Running

1. **Navigate to the UI directory**:
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
ui/
├── src/
│   ├── components/          # React components
│   │   ├── LoadingSpinner.tsx
│   │   ├── PaperCard.tsx
│   │   └── SynthesisCard.tsx
│   ├── services/           # API services
│   │   └── api.ts
│   ├── types.ts            # TypeScript type definitions
│   ├── App.tsx            # Main application component
│   ├── main.tsx           # React entry point
│   └── index.css          # Global styles
├── public/                # Static assets
├── package.json           # Dependencies and scripts
├── vite.config.ts         # Vite configuration
├── tailwind.config.js     # Tailwind CSS configuration
└── tsconfig.json          # TypeScript configuration
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
4. **Step 1 - Detection**: Beautiful loading spinner while searching for contradictions via Perplexity
5. **Step 2 - Propagation**: Animated loading while mapping citation cascades
6. **Step 3 - Synthesis**: Loading animation while formulating research strategy with NVIDIA NeMo
7. **Results**: Beautiful cards displaying all findings with smooth animations

## 🎨 Design Features

### Loading Animations
- **Step-specific icons**: Different icons for each analysis phase
- **Smooth transitions**: Framer Motion animations throughout
- **Progress indicators**: Visual feedback for each step

### Modern UI Elements
- **Gradient backgrounds**: Beautiful color schemes
- **Glass morphism**: Modern translucent effects
- **Hover animations**: Interactive card hover effects
- **Responsive design**: Works on all screen sizes

### Color Scheme
- **Primary**: Blue gradient (#3B82F6 to #1E40AF)
- **Success**: Green (#10B981)
- **Warning**: Orange (#F59E0B)
- **Error**: Red (#EF4444)
- **Neutral**: Gray scale for text and backgrounds

## 🔧 Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Key Technologies

- **React 18** - Modern React with hooks
- **TypeScript** - Type safety and better DX
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **Lucide React** - Beautiful icons

## 🌐 API Integration

The UI is designed to work with the Python backend. The API service (`src/services/api.ts`) includes:

- **Error handling**: Graceful fallbacks for API failures
- **Loading states**: Beautiful loading animations
- **Mock data**: For development and demonstration
- **Type safety**: Full TypeScript integration

## 🚀 Deployment

For production deployment:

```bash
npm run build
```

This creates a `dist/` folder with optimized static files that can be deployed to any web server or CDN.

## 🎯 Current Status

✅ **Node.js Installation**: Successfully installed and configured  
✅ **Dependencies**: All React dependencies installed  
✅ **Development Server**: Running on http://localhost:3000  
✅ **UI Components**: Modern, responsive interface implemented  
✅ **PDF Upload**: Drag-and-drop functionality working  
✅ **Text Input**: Direct claim entry supported  

---

**Note**: This modern UI provides a significantly enhanced user experience compared to the original Streamlit application, with beautiful animations, modern design principles, and improved usability.
