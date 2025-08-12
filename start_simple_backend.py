#!/usr/bin/env python3
"""
Startup script for the simplified Research Integrity Network backend.
This script starts the Flask backend server that directly calls the AI agents.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Start the simplified backend server
    print("🚀 Starting Research Integrity Network (Simplified Backend)...")
    print("📍 Backend will be available at: http://localhost:8501")
    print("📍 Frontend should be running at: http://localhost:3000")
    print("📝 Make sure you have set up your .env file with PERPLEXITY_API_KEY")
    print("🔧 This version directly calls the agents without complex FastAPI setup")
    print("=" * 60)
    
    try:
        # Run the simplified backend server
        subprocess.run([sys.executable, "ui/simple_backend.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Backend server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting backend server: {e}")
        print("💡 Make sure you have installed Flask: pip install flask flask-cors")
        sys.exit(1)

if __name__ == "__main__":
    main()
