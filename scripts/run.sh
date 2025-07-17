#!/bin/bash

# Portfolio Management Application Runner

echo "🚀 Starting Portfolio Management Application..."
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠️ Virtual environment not found. Run ./scripts/setup.sh first."
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️ .env file not found. Creating from template..."
    cp config/.env.example .env
    echo "📝 Please edit .env file with your API credentials and restart."
    exit 1
fi

echo "🔍 Testing setup..."
python scripts/test_setup.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup verified! Starting Streamlit application..."
    echo "🌐 Opening http://localhost:8501"
    echo ""
    echo "📋 Navigation:"
    echo "   🏠 Dashboard  - Portfolio overview"
    echo "   📋 Orders     - Order management" 
    echo "   📈 Market     - Market data & charts"
    echo "   ⚙️ Settings   - Configuration"
    echo ""
    echo "🔐 Don't forget to authenticate with Kite Connect!"
    echo ""
    
    streamlit run src/app.py
else
    echo "❌ Setup test failed. Please fix the issues and try again."
    exit 1
fi
