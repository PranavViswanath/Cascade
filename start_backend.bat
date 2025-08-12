@echo off
echo 🚀 Starting Research Integrity Network Backend Server...
echo 📍 Backend will be available at: http://localhost:8501
echo 📍 Frontend should be running at: http://localhost:3000
echo 📝 Make sure you have set up your .env file with PERPLEXITY_API_KEY
echo ============================================================

python ui/backend_server.py

pause
