# 🔄 Features Comparison: Hosted vs Local MCP Server

## Overview

The portfolio management application can work with two different MCP server configurations, each offering different levels of functionality.

## 🌐 Hosted Server (mcp.kite.trade)

### Setup
```bash
# In your .env file
MCP_SERVER_URL=https://mcp.kite.trade/mcp
```

### ✅ Available Features

#### Portfolio Management
- ✅ **View Holdings**: Complete holdings with quantities, prices, P&L
- ✅ **View Positions**: Current day and overnight positions
- ✅ **Account Margins**: Available margins and limits
- ✅ **Mutual Fund Holdings**: MF portfolio tracking
- ✅ **Portfolio Analytics**: P&L calculations, allocation charts

#### Market Data
- ✅ **Real-time Quotes**: Live prices for watchlist stocks
- ✅ **Historical Data**: Basic historical price data
- ✅ **Market Overview**: Index values and market summary
- ✅ **OHLC Data**: Open, High, Low, Close data
- ✅ **LTP (Last Traded Price)**: Current market prices

#### Account Information
- ✅ **User Profile**: Account details and user information
- ✅ **Trade History**: Past completed trades
- ✅ **Order History**: Historical order information (view-only)

### ❌ Restricted Features

#### Trading Operations
- ❌ **Place Orders**: Cannot place new orders
- ❌ **Modify Orders**: Cannot modify existing orders  
- ❌ **Cancel Orders**: Cannot cancel pending orders
- ❌ **GTT Orders**: No Good Till Triggered order support

#### Advanced Features
- ❌ **Real-time Order Updates**: Limited order status tracking
- ❌ **Advanced Historical Data**: Limited interval options
- ❌ **Custom Alerts**: No order execution alerts

### 👍 Pros
- **Zero Setup**: No installation or configuration required
- **Always Available**: 24/7 uptime and reliability
- **No Maintenance**: Fully managed service
- **Quick Start**: Get started in minutes
- **No Dependencies**: No need for Go or additional software

### 👎 Cons
- **Read-Only**: Cannot execute trading operations
- **Limited Features**: Missing key trading functionality
- **Shared Resources**: Potential rate limiting
- **Less Customization**: Fixed server configuration

### 🎯 Best For
- **Learning**: Understanding the interface and features
- **Portfolio Monitoring**: Tracking investments without trading
- **Demo Purposes**: Showcasing the application
- **Development**: Testing non-trading features

---

## 🏠 Local Server (Self-Hosted)

### Setup
```bash
# Clone and setup Kite MCP server
git clone https://github.com/zerodha/kite-mcp-server
cd kite-mcp-server

# Configure
echo "KITE_API_KEY=your_key" > .env
echo "KITE_API_SECRET=your_secret" >> .env
echo "APP_MODE=http" >> .env

# Run
go run main.go

# In portfolio app .env
MCP_SERVER_URL=http://localhost:8080/mcp
```

### ✅ Full Feature Set

#### Complete Portfolio Management
- ✅ **All Hosted Features**: Everything from hosted server
- ✅ **Real-time Updates**: Live portfolio tracking
- ✅ **Custom Intervals**: All historical data intervals
- ✅ **Advanced Analytics**: Detailed performance metrics

#### Full Trading Capabilities
- ✅ **Place Orders**: All order types (Market, Limit, SL, SL-M)
- ✅ **Modify Orders**: Change price, quantity, order type
- ✅ **Cancel Orders**: Cancel any pending orders
- ✅ **Order Validation**: Pre-trade checks and validations

#### Advanced Order Management
- ✅ **GTT Orders**: Good Till Triggered orders
- ✅ **Bracket Orders**: CO (Cover Orders) support
- ✅ **AMO Orders**: After Market Orders
- ✅ **Iceberg Orders**: Large order slicing

#### Enhanced Market Data
- ✅ **All Intervals**: minute, 3min, 5min, 15min, 30min, 60min, day
- ✅ **Extended Historical**: Longer date ranges
- ✅ **Real-time Feeds**: Live market data streaming
- ✅ **Options Data**: Options chain and Greeks (if subscribed)

#### Professional Features
- ✅ **Custom Alerts**: Price and order alerts
- ✅ **Risk Management**: Position limits and checks
- ✅ **Advanced Charts**: Technical indicators
- ✅ **Export Data**: Download reports and data

### 👍 Pros
- **Complete Control**: Full API access and functionality
- **Real Trading**: Execute actual trades and manage portfolio
- **Better Performance**: Dedicated server resources
- **Customization**: Configure server settings
- **No Limitations**: Access to all Kite Connect features
- **Privacy**: Your data stays on your infrastructure

### 👎 Cons
- **Setup Required**: Need to install and configure Go server
- **Maintenance**: Responsible for server uptime and updates
- **Dependencies**: Requires Go 1.21+ and system resources
- **Complexity**: More moving parts to manage
- **Security**: Need to secure your own server

### 🎯 Best For
- **Active Trading**: Regular order placement and management
- **Portfolio Management**: Complete investment management
- **Production Use**: Real-world trading applications
- **Advanced Users**: Those comfortable with server management
- **Custom Solutions**: Building specialized trading tools

---

## 📊 Feature Matrix

| Feature Category | Hosted Server | Local Server |
|------------------|---------------|--------------|
| **Setup Complexity** | 🟢 None | 🟡 Moderate |
| **Portfolio Viewing** | ✅ Complete | ✅ Complete |
| **Market Data** | ✅ Basic | ✅ Advanced |
| **Order Placement** | ❌ Disabled | ✅ Full Support |
| **Order Management** | ❌ View Only | ✅ Complete |
| **GTT Orders** | ❌ None | ✅ Full Support |
| **Historical Data** | ✅ Limited | ✅ All Intervals |
| **Real-time Updates** | ✅ Basic | ✅ Advanced |
| **Custom Alerts** | ❌ None | ✅ Available |
| **Performance** | 🟡 Shared | 🟢 Dedicated |
| **Uptime** | 🟢 Managed | 🟡 Self-managed |
| **Cost** | 🟢 Free | 🟡 Infrastructure |

## 🚦 Recommendation Guide

### Choose **Hosted Server** if you:
- Want to quickly explore the application
- Only need portfolio monitoring
- Don't want to manage infrastructure
- Are learning about trading APIs
- Need a demo for presentations

### Choose **Local Server** if you:
- Plan to actively trade through the application
- Need complete order management
- Want advanced features and customization
- Are building a production trading system
- Have technical expertise to manage servers

## 🔄 Switching Between Modes

You can easily switch between hosted and local servers:

```bash
# Switch to hosted
echo "MCP_SERVER_URL=https://mcp.kite.trade/mcp" > .env

# Switch to local
echo "MCP_SERVER_URL=http://localhost:8080/mcp" > .env

# Restart application
./scripts/run.sh
```

The application will automatically detect the available features based on your MCP server configuration.
