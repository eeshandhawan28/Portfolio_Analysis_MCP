# Portfolio Management Application with Kite MCP

A modern portfolio management application built with Streamlit that integrates with the Zerodha Kite MCP Server for real-time trading and portfolio management.

## 🚀 Features

- **Real-time Portfolio Tracking**: View holdings, positions, and P&L
- **Market Data**: Live quotes, historical charts, and market movers
- **Order Management**: Place, modify, and track orders
- **Interactive Dashboard**: Beautiful visualizations and charts
- **Multi-page Navigation**: Organized interface with different sections
- **MCP Integration**: Seamless connection to Kite Connect API via MCP

## 📋 Prerequisites

Before running this application, you need:

1. **Kite Connect API Credentials**
   - Get your API key and secret from [Kite Connect](https://kite.trade/connect/login)

2. **Kite MCP Server**
   - Clone and run the [Kite MCP Server](https://github.com/zerodha/kite-mcp-server)
   - Or use the hosted version at `https://mcp.kite.trade/mcp`

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd MCP
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env file with your API credentials
   ```

4. **Set up Kite MCP Server** (if running locally)
   ```bash
   # In a separate terminal
   git clone https://github.com/zerodha/kite-mcp-server
   cd kite-mcp-server
   
   # Create .env file with your Kite credentials
   echo "KITE_API_KEY=your_api_key" > .env
   echo "KITE_API_SECRET=your_api_secret" >> .env
   echo "APP_MODE=http" >> .env
   
   # Run the server
   go run main.go
   ```

## 🏃‍♂️ Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will open at `http://localhost:8501`

3. **Authenticate**
   - Click "Login to Kite Connect" in the sidebar
   - Complete the authentication process
   - Return to the app and refresh

## 📱 Application Structure

```
MCP/
├── app.py                    # Main multi-page application
├── portfolio_dashboard.py    # Portfolio overview and holdings
├── order_management.py       # Order placement and tracking
├── market_data.py           # Market data and charts
├── kite_mcp_client.py       # MCP client library
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 🎯 Application Pages

### 🏠 Dashboard
- Portfolio summary with key metrics
- Holdings table with P&L analysis
- Portfolio allocation charts
- Market movers (gainers/losers)

### 📋 Orders
- **Place Order**: Form to place new orders
- **Order Book**: View all your orders
- **Trade History**: Track completed trades

### 📈 Market Data
- Market overview with major indices
- Interactive stock charts with candlesticks
- Personal watchlist
- Sector performance analysis

### ⚙️ Settings
- MCP server configuration
- API credentials management
- Display preferences
- Alert settings

## 🔐 Authentication Flow

1. **Start Application**: Open the Streamlit app
2. **Check Connection**: App checks MCP server connection
3. **Login Required**: If not authenticated, shows login button
4. **Get Login URL**: MCP server generates Kite Connect login URL
5. **Browser Authentication**: User completes login in browser
6. **Auto-refresh**: Return to app and refresh to see authenticated state

## 📊 Data Features

### Portfolio Data
- Real-time holdings and positions
- P&L calculations and percentages
- Portfolio allocation visualization
- Current market values

### Market Data
- Live quotes and LTP
- Historical price charts
- Market indices tracking
- Sector performance analysis

### Order Management
- Place orders with validation
- Real-time order status
- Trade history and analytics
- Order modification capabilities

## 🛡️ Security Features

- **No API Key Storage**: Credentials stored in environment variables
- **MCP Authentication**: Secure token-based authentication
- **Session Management**: Automatic session handling
- **Error Handling**: Comprehensive error handling and user feedback

## 🎨 UI Features

- **Responsive Design**: Works on desktop and mobile
- **Interactive Charts**: Plotly-powered visualizations
- **Real-time Updates**: Live data refresh capabilities
- **Color Coding**: Intuitive green/red profit/loss indicators
- **Modern Styling**: Clean and professional interface

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Kite Connect API Keys
KITE_API_KEY=your_api_key_here
KITE_API_SECRET=your_api_secret_here

# MCP Server Configuration
MCP_SERVER_URL=http://localhost:8080/mcp
MCP_SERVER_MODE=http

# Application Configuration
DEBUG=False
```

### MCP Server Options
- **Local Server**: Run your own instance with full API access
- **Hosted Server**: Use `https://mcp.kite.trade/mcp` (read-only operations)

## 📈 Demo Mode

The application includes demo data for testing:
- Sample portfolio holdings
- Mock market data
- Simulated orders and trades
- Real-time-like updates

When not authenticated, the app shows demo data with clear indicators.

## 🚨 Important Notes

1. **Trading Risks**: This is a demo application. Always verify data before making trading decisions.

2. **API Limits**: Be aware of Kite Connect API rate limits and usage policies.

3. **Data Accuracy**: Real-time data may have slight delays. Use official Kite platforms for critical trading.

4. **Security**: Never share your API credentials. Keep them secure and rotate regularly.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational and demonstration purposes. Please review Zerodha's terms of service for API usage.

## 🆘 Support

For issues related to:
- **This Application**: Create an issue in this repository
- **Kite MCP Server**: Visit the [official repository](https://github.com/zerodha/kite-mcp-server)
- **Kite Connect API**: Check [Kite Connect documentation](https://kite.trade/docs/connect/)

## 🙏 Acknowledgments

- [Zerodha](https://zerodha.com/) for the Kite Connect API
- [Kite MCP Server](https://github.com/zerodha/kite-mcp-server) team
- [Streamlit](https://streamlit.io/) for the amazing framework
- [Plotly](https://plotly.com/) for interactive visualizations
