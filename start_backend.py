#!/usr/bin/env python3
"""
Startup script for the Cascade - AI Research Analysis backend server.
This script starts the FastAPI backend server that provides the API endpoints
for the TypeScript frontend to communicate with the AI agents.
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
    
    # Start the backend server
    print("🚀 Starting Cascade - AI Research Analysis Backend Server...")
    print("📍 Backend will be available at: http://localhost:8501")
    print("📍 Frontend should be running at: http://localhost:3000")
    print("📝 Make sure you have set up your .env file with PERPLEXITY_API_KEY")
    print("=" * 60)
    
    try:
        # Run the backend server
        subprocess.run([sys.executable, "ui/backend_server.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Backend server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting backend server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
