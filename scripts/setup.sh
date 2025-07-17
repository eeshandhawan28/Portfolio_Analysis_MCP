#!/bin/bash

# Portfolio Management Application Setup Script

echo "🚀 Setting up Portfolio Management Application..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✅ Python 3 found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    echo "Please install pip3"
    exit 1
fi

echo "✅ pip3 found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python packages..."
pip install -r config/requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp config/.env.example .env
    echo "✅ .env file created. Please edit it with your API credentials."
else
    echo "⚠️ .env file already exists"
fi

# Create run script
cat > run.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting Portfolio Management Application..."
source venv/bin/activate
streamlit run app.py
EOF

chmod +x run.sh

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your Kite Connect API credentials"
echo "2. Ensure Kite MCP Server is running (http://localhost:8080/mcp)"
echo "3. Run the application:"
echo "   ./scripts/run.sh"
echo ""
echo "🌐 The app will open at http://localhost:8501"
echo ""
echo "📖 For more information, see README.md"
