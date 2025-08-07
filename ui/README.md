# Research Integrity Network - Modern UI

A beautiful, modern TypeScript React application for the Research Integrity Network with sleek animations and state-of-the-art design.

## 🎨 Features

- **Modern Design**: Sleek, gradient-based UI with smooth animations
- **Real-time Feedback**: Beautiful loading spinners for each analysis step
- **Responsive Layout**: Works perfectly on desktop and mobile
- **TypeScript**: Fully typed for better development experience
- **Framer Motion**: Smooth animations and transitions
- **Tailwind CSS**: Modern utility-first styling

## 🚀 Quick Start

### Prerequisites

1. **Install Node.js** (v18 or higher):
   - Download from [nodejs.org](https://nodejs.org/)
   - Or use a package manager like Chocolatey: `choco install nodejs`

2. **Install Git** (if not already installed):
   - Download from [git-scm.com](https://git-scm.com/)

### Installation

1. **Navigate to the UI directory**:
   ```bash
   cd ui
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

4. **Open your browser** and go to `http://localhost:3000`

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

## 🎯 Workflow

The application maintains the exact same workflow as the original Streamlit app:

1. **Input Selection**: Choose between text input or PDF upload
2. **Claim Entry**: Enter your research claim or upload a PDF
3. **Analysis**: Click "Analyze Research Claim" to start the process
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

## 🎯 Next Steps

1. **Install Node.js** on your system
2. **Run the installation commands** above
3. **Start the development server**
4. **Enjoy the beautiful modern UI!**

The application will provide the same functionality as the Streamlit version but with a much more polished and professional appearance.

## 🚀 Deployment

For production deployment:

```bash
npm run build
```

This creates a `dist/` folder with optimized static files that can be deployed to any web server or CDN.

---

**Note**: This modern UI maintains 100% feature parity with the original Streamlit application while providing a significantly enhanced user experience with beautiful animations and modern design principles.
