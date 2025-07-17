# 🚀 Deployment Guide

## Local Development Deployment

### Quick Setup (5 minutes)
```bash
# 1. Setup everything
./scripts/setup.sh

# 2. Add your API keys to .env
nano .env

# 3. Choose your server mode:

# Option A: Use hosted server (limited features)
# Set in .env: MCP_SERVER_URL=https://mcp.kite.trade/mcp

# Option B: Use local server (full features)
# Set in .env: MCP_SERVER_URL=http://localhost:8080/mcp
# Then run Kite MCP server separately

# 4. Start the application
./scripts/run.sh
```

### Local Kite MCP Server Setup
```bash
# In a separate terminal/directory
git clone https://github.com/zerodha/kite-mcp-server
cd kite-mcp-server

# Configure
cat > .env << EOF
KITE_API_KEY=your_api_key
KITE_API_SECRET=your_api_secret
APP_MODE=http
APP_PORT=8080
APP_HOST=localhost
EOF

# Run (requires Go 1.21+)
go run main.go
```

## Production Deployment

### Using Streamlit Cloud
1. Push code to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add secrets in Streamlit Cloud dashboard:
   ```
   KITE_API_KEY = "your_key"
   KITE_API_SECRET = "your_secret"
   MCP_SERVER_URL = "https://mcp.kite.trade/mcp"
   ```

### Using Heroku
1. Create `Procfile`:
   ```
   web: streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set KITE_API_KEY=your_key
   heroku config:set KITE_API_SECRET=your_secret
   heroku config:set MCP_SERVER_URL=https://mcp.kite.trade/mcp
   git push heroku main
   ```

### Using Docker (if needed)
```bash
# Build image
docker build -t portfolio-app .

# Run container
docker run -p 8501:8501 \
  -e KITE_API_KEY=your_key \
  -e KITE_API_SECRET=your_secret \
  -e MCP_SERVER_URL=https://mcp.kite.trade/mcp \
  portfolio-app
```

## Security Considerations

### For Production
- Use HTTPS only
- Store secrets securely
- Enable authentication
- Monitor API usage
- Set up logging

### API Key Security
- Never commit API keys to git
- Use environment variables
- Rotate keys regularly
- Monitor usage patterns
