# 📈 Portfolio Management Application

A modern, feature-rich portfolio management application built with Streamlit that integrates with the Zerodha Kite Connect API through the Model Context Protocol (MCP). This application provides real-time portfolio tracking, market data analysis, and order management capabilities.

## 🚀 Quick Start

### Method 1: Automated Setup (Recommended)
```bash
# 1. Setup everything automatically
./scripts/setup.sh

# 2. Add your Kite Connect API keys
nano .env

# 3. Start the application  
./scripts/run.sh
```

### Method 2: Manual Setup
```bash
# 1. Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r config/requirements.txt

# 2. Configure environment
cp config/.env.example .env
# Edit .env with your API credentials

# 3. Run application
streamlit run src/app.py
```

## 🏗️ Project Structure

```
portfolio-management-app/
├── 📁 src/                          # Source code
│   ├── app.py                       # Main Streamlit application
│   ├── 📁 pages/                    # Application pages
│   │   ├── portfolio_dashboard.py   # Portfolio overview & holdings
│   │   ├── order_management.py      # Order placement & tracking
│   │   └── market_data.py          # Market data & charts
│   └── 📁 utils/                    # Utility modules
│       ├── kite_mcp_client.py      # MCP client library
│       └── utils.py                # Helper functions
├── 📁 config/                       # Configuration files
│   ├── requirements.txt            # Python dependencies
│   └── .env.example               # Environment template
├── 📁 scripts/                      # Setup & run scripts
│   ├── setup.sh                   # Automated setup
│   ├── run.sh                     # Application runner
│   └── test_setup.py              # Setup verification
├── 📁 docs/                        # Documentation
│   ├── README.md                  # Detailed documentation
│   ├── QUICKSTART.md             # 5-minute setup guide
│   ├── FEATURES.md               # Feature comparison
│   ├── DEPLOYMENT.md             # Deployment guide
│   └── DEVELOPMENT.md            # Development guide
└── README.md                      # This file
```

## 🔗 MCP Server Setup

You can use the Kite MCP server in two ways:

### Option A: Hosted Server (Quick Start - Limited Features)

**Setup:**
```bash
# In your .env file:
MCP_SERVER_URL=https://mcp.kite.trade/mcp
```

**Features Available:**
- ✅ Portfolio viewing (holdings, positions)
- ✅ Market data (quotes, historical data)
- ✅ Account information
- ❌ Order placement (disabled for security)
- ❌ Order modification/cancellation
- ❌ GTT order management

**Pros:**
- No setup required
- Always available
- No need for local server

**Cons:**
- Trading operations disabled
- Read-only access
- Shared resource limitations

### Option B: Local Server (Full Features)

**Setup:**
```bash
# 1. Clone the Kite MCP server
git clone https://github.com/zerodha/kite-mcp-server
cd kite-mcp-server

# 2. Configure with your API keys
echo "KITE_API_KEY=your_api_key" > .env
echo "KITE_API_SECRET=your_api_secret" >> .env
echo "APP_MODE=http" >> .env
echo "APP_PORT=8080" >> .env

# 3. Run the server
go run main.go

# 4. In your portfolio app .env:
MCP_SERVER_URL=http://localhost:8080/mcp
```

**Features Available:**
- ✅ Complete portfolio management
- ✅ Full market data access
- ✅ Order placement & management
- ✅ Order modification & cancellation
- ✅ GTT order management
- ✅ Real-time updates
- ✅ Historical data with custom intervals

**Pros:**
- Full API access
- Real trading capabilities
- Better performance
- No rate limiting from shared usage

**Cons:**
- Requires local setup
- Need to manage server yourself
- Requires Go installation

## 🔑 API Configuration

### Getting Kite Connect API Keys

1. **Visit [Kite Connect](https://kite.trade/connect/login)**
2. **Create a new app** or use existing one
3. **Note down your API Key and API Secret**
4. **Configure in .env file:**

```bash
# Required for both hosted and local server
KITE_API_KEY=your_actual_api_key_here
KITE_API_SECRET=your_actual_api_secret_here

# Choose your MCP server mode
MCP_SERVER_URL=http://localhost:8080/mcp          # For local server
# MCP_SERVER_URL=https://mcp.kite.trade/mcp      # For hosted server

# Application settings
DEBUG=False
```

## 📱 Application Features

### 🏠 Dashboard
- **Portfolio Summary**: Total value, P&L, day's change
- **Holdings Table**: Detailed view with current prices and P&L
- **Interactive Charts**: Portfolio allocation pie chart, P&L bar chart
- **Market Movers**: Top gainers and losers
- **Real-time Updates**: Live portfolio values

### 📋 Orders
- **Place Orders**: Complete order form with validation
  - Market/Limit/Stop Loss orders
  - All exchanges (NSE, BSE, MCX, NFO, BFO)
  - Multiple product types (CNC, MIS, NRML)
- **Order Book**: View all orders with real-time status
- **Trade History**: Complete trading history with details
- **Order Management**: Modify and cancel pending orders (local server only)

### 📈 Market Data
- **Market Overview**: Major indices (NIFTY, SENSEX, BANK NIFTY)
- **Interactive Charts**: Candlestick charts with volume
- **Watchlist**: Personal stock watchlist with live prices
- **Sector Analysis**: Sector performance tracking
- **Historical Data**: Custom date ranges and intervals

### ⚙️ Settings
- **MCP Configuration**: Server URL and connection settings
- **API Management**: Secure credential management
- **Display Options**: Theme and refresh settings
- **Notifications**: Alert preferences

## 🛡️ Security Features

- **Secure Authentication**: OAuth-based Kite Connect authentication
- **Environment Variables**: API keys stored securely in .env files
- **Session Management**: Automatic session handling and refresh
- **Error Handling**: Comprehensive error handling with user feedback
- **Input Validation**: All order parameters validated before submission

## 🎯 Feature Comparison

| Feature | Hosted Server | Local Server |
|---------|---------------|--------------|
| **Portfolio Viewing** | ✅ Full Access | ✅ Full Access |
| **Market Data** | ✅ Full Access | ✅ Full Access |
| **Historical Data** | ✅ Limited intervals | ✅ All intervals |
| **Order Placement** | ❌ Disabled | ✅ Enabled |
| **Order Management** | ❌ Disabled | ✅ Enabled |
| **GTT Orders** | ❌ Disabled | ✅ Enabled |
| **Real-time Updates** | ✅ Yes | ✅ Yes |
| **Setup Complexity** | 🟢 None | 🟡 Moderate |
| **Performance** | 🟡 Shared | 🟢 Dedicated |
| **Reliability** | 🟢 High | 🟡 Self-managed |

## 🚦 Authentication Flow

### Initial Setup
1. **Start Application**: Launch with `./scripts/run.sh`
2. **Check Connection**: App verifies MCP server connectivity
3. **Login Required**: Shows login button if not authenticated

### Authentication Process
1. **Click Login**: "Login to Kite Connect" button in sidebar
2. **Get URL**: MCP server generates secure Kite Connect login URL
3. **Browser Auth**: Complete 2FA authentication in browser
4. **Return to App**: Refresh the application page
5. **Authenticated**: Access all portfolio features

### Session Management
- **Automatic Refresh**: Sessions refreshed automatically
- **Secure Storage**: Tokens managed by MCP server
- **Error Recovery**: Automatic re-authentication on session expiry

## 🧪 Testing & Development

### Verify Setup
```bash
# Test your installation
python scripts/test_setup.py
```

### Demo Mode
When not authenticated, the app shows:
- Sample portfolio data
- Mock market information
- Demo order forms
- All UI features with placeholder data

### Development Mode
```bash
# Enable debug logging
echo "DEBUG=True" >> .env

# Run with hot reload
streamlit run src/app.py --server.runOnSave true
```

## 📊 Data Sources & Updates

### Portfolio Data
- **Source**: Kite Connect API via MCP
- **Update Frequency**: Real-time on user action
- **Includes**: Holdings, positions, margins, mutual funds

### Market Data
- **Source**: Kite Connect market feeds
- **Update Frequency**: Real-time quotes
- **Includes**: Live prices, OHLC, volume, historical data

### Order Data
- **Source**: Kite Connect order API
- **Update Frequency**: Real-time
- **Includes**: Order status, trade confirmations, history

## ⚡ Performance Optimizations

- **Caching**: Intelligent data caching to reduce API calls
- **Lazy Loading**: Components load data only when needed
- **Pagination**: Large datasets automatically paginated
- **Error Recovery**: Robust error handling with retry logic
- **Resource Management**: Efficient memory and CPU usage

## 🔧 Troubleshooting

### Common Issues

**"MCP Server Unavailable"**
```bash
# Check if server is running (for local setup)
curl http://localhost:8080/

# For hosted server, check internet connection
curl https://mcp.kite.trade/
```

**"Authentication Required"**
- Click "Login to Kite Connect" in sidebar
- Complete 2FA in browser
- Refresh the application page

**"Import Errors"**
```bash
# Reinstall dependencies
pip install -r config/requirements.txt

# Activate virtual environment
source venv/bin/activate
```

**"Permission Denied on Scripts"**
```bash
# Make scripts executable
chmod +x scripts/*.sh
```

### Getting Help

- **Application Issues**: Create an issue in this repository
- **Kite MCP Server**: Visit [official repository](https://github.com/zerodha/kite-mcp-server)
- **Kite Connect API**: Check [documentation](https://kite.trade/docs/connect/)

## 📈 Usage Tips

### Best Practices
1. **Start with Demo**: Familiarize yourself with the interface using demo data
2. **Verify Data**: Always cross-check critical information with official Kite platforms
3. **Test Orders**: Start with small quantities when testing order placement
4. **Monitor Limits**: Be aware of API rate limits and daily quotas
5. **Keep Updated**: Regularly update both the app and MCP server

### Recommended Workflow
1. **Morning Setup**: Check portfolio and market overview
2. **Market Analysis**: Use charts and sector performance for decisions  
3. **Order Management**: Place and monitor orders through the interface
4. **Evening Review**: Analyze day's trades and P&L

## ⚠️ Important Disclaimers

- **Demo Application**: This is primarily for educational and demonstration purposes
- **Trading Risks**: Always verify data before making trading decisions
- **No Warranties**: Use at your own risk; no guarantees on data accuracy
- **API Compliance**: Ensure compliance with Zerodha's terms of service
- **Security**: Keep API credentials secure and rotate them regularly

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

## 📄 License

This project is for educational purposes. Please review Zerodha's terms of service for API usage.

## 🙏 Acknowledgments

- **[Zerodha](https://zerodha.com/)** for the Kite Connect API
- **[Kite MCP Server Team](https://github.com/zerodha/kite-mcp-server)** for the MCP implementation
- **[Streamlit](https://streamlit.io/)** for the amazing web framework
- **[Plotly](https://plotly.com/)** for interactive visualizations

---

**Ready to start trading smarter? Get started with `./scripts/setup.sh`!** 🚀
