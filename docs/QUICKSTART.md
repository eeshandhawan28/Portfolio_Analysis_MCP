# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Setup
```bash
# Make setup script executable
chmod +x scripts/setup.sh

# Run setup (installs dependencies)
./scripts/setup.sh
```

### Step 2: Configure
```bash
# Edit .env file with your credentials
nano .env
```

Add your Kite Connect API credentials:
```
KITE_API_KEY=your_actual_api_key
KITE_API_SECRET=your_actual_api_secret
```

### Step 3: Start Kite MCP Server
```bash
# Option A: Use hosted version (limited features)
# Set MCP_SERVER_URL=https://mcp.kite.trade/mcp in .env

# Option B: Run locally (recommended)
git clone https://github.com/zerodha/kite-mcp-server
cd kite-mcp-server
echo "KITE_API_KEY=your_api_key" > .env
echo "KITE_API_SECRET=your_api_secret" >> .env
echo "APP_MODE=http" >> .env
go run main.go
```

### Step 4: Run Application
```bash
./scripts/run.sh
```

The app will open at http://localhost:8501

### Step 5: Authenticate
1. Click "Login to Kite Connect" in sidebar
2. Complete authentication in browser
3. Return to app and refresh

## 📱 Features Overview

- **Dashboard**: Portfolio overview, holdings, P&L
- **Orders**: Place and track orders
- **Market Data**: Live quotes, charts, analysis
- **Settings**: Configuration and preferences

Enjoy trading! 📈
