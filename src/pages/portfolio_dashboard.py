"""
Portfolio Dashboard - Main Streamlit application for portfolio management
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Import our MCP client
from utils.kite_mcp_client import KiteMCPClient, MCPResponse

# Page configuration
st.set_page_config(
    page_title="Portfolio Manager - Kite MCP",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .status-connected {
        color: #28a745;
        font-weight: bold;
    }
    .status-error {
        color: #dc3545;
        font-weight: bold;
    }
    .sidebar-section {
        margin: 1rem 0;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'mcp_client' not in st.session_state:
        server_url = os.getenv('MCP_SERVER_URL', 'http://localhost:8080/mcp')
        st.session_state.mcp_client = KiteMCPClient(server_url)
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'profile_data' not in st.session_state:
        st.session_state.profile_data = None
    
    if 'holdings_data' not in st.session_state:
        st.session_state.holdings_data = None
    
    if 'positions_data' not in st.session_state:
        st.session_state.positions_data = None

def display_connection_status():
    """Display MCP server connection status"""
    st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.sidebar.markdown("### 🔗 Connection Status")
    
    try:
        # Try to make a simple request to check connection
        response = st.session_state.mcp_client.get_profile()
        if response.success:
            st.sidebar.markdown('<span class="status-connected">✅ Connected & Authenticated</span>', unsafe_allow_html=True)
            st.session_state.authenticated = True
            return True
        else:
            st.sidebar.markdown('<span class="status-error">❌ Authentication Required</span>', unsafe_allow_html=True)
            st.session_state.authenticated = False
            return False
    except Exception as e:
        st.sidebar.markdown('<span class="status-error">❌ Server Unavailable</span>', unsafe_allow_html=True)
        st.sidebar.error(f"Error: {str(e)}")
        st.session_state.authenticated = False
        return False
    finally:
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

def handle_authentication():
    """Handle Kite Connect authentication"""
    st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.sidebar.markdown("### 🔐 Authentication")
    
    if st.sidebar.button("🚀 Login to Kite Connect", type="primary"):
        with st.spinner("Initiating login..."):
            response = st.session_state.mcp_client.login()
            
            if response.success:
                st.sidebar.success("✅ Login URL generated!")
                st.sidebar.markdown("**Click the link below to authenticate:**")
                st.sidebar.markdown(response.data, unsafe_allow_html=True)
                st.sidebar.info("After completing login in your browser, refresh this page.")
            else:
                st.sidebar.error(f"❌ Login failed: {response.error}")
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

def load_profile_data():
    """Load user profile data"""
    if st.session_state.authenticated and st.session_state.profile_data is None:
        response = st.session_state.mcp_client.get_profile()
        if response.success:
            st.session_state.profile_data = response.data

def display_profile_info():
    """Display user profile information"""
    if st.session_state.profile_data:
        profile = st.session_state.profile_data
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("👤 User", profile.get('user_name', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("📧 Email", profile.get('email', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("🏢 Broker", profile.get('broker', 'Zerodha'))
            st.markdown('</div>', unsafe_allow_html=True)

def load_portfolio_data():
    """Load portfolio data (holdings and positions)"""
    if st.session_state.authenticated:
        if st.session_state.holdings_data is None:
            response = st.session_state.mcp_client.get_holdings()
            if response.success:
                st.session_state.holdings_data = response.data
        
        if st.session_state.positions_data is None:
            response = st.session_state.mcp_client.get_positions()
            if response.success:
                st.session_state.positions_data = response.data

def display_portfolio_summary():
    """Display portfolio summary metrics"""
    st.markdown("### 📊 Portfolio Summary")
    
    # Sample data for demonstration
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💰 Total Value", "₹5,45,250", "12.5%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📈 Day's P&L", "₹8,750", "1.6%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🎯 Total P&L", "₹45,250", "9.1%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📊 Holdings", "12", "2")
        st.markdown('</div>', unsafe_allow_html=True)

def create_sample_holdings_data():
    """Create sample holdings data for demonstration"""
    return pd.DataFrame({
        'Symbol': ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ITC', 'SBIN', 'BHARTIARTL', 'KOTAKBANK'],
        'Quantity': [50, 25, 30, 40, 100, 75, 60, 35],
        'Avg Price': [2450.50, 3250.75, 1520.25, 1680.90, 425.60, 520.30, 845.20, 1750.80],
        'LTP': [2580.30, 3420.50, 1650.75, 1720.40, 445.80, 545.60, 880.90, 1820.30],
        'P&L': [6490, 4244, 3915, 1580, 2020, 1898, 2142, 2431],
        'P&L %': [5.3, 13.1, 8.6, 2.4, 4.7, 4.9, 4.2, 4.0]
    })

def display_holdings_table():
    """Display holdings in a table format"""
    st.markdown("### 🏠 Holdings")
    
    # Use sample data for demonstration
    df = create_sample_holdings_data()
    
    # Calculate current value
    df['Current Value'] = df['Quantity'] * df['LTP']
    df['Investment'] = df['Quantity'] * df['Avg Price']
    
    # Format the dataframe for display
    display_df = df[['Symbol', 'Quantity', 'Avg Price', 'LTP', 'Current Value', 'P&L', 'P&L %']].copy()
    
    # Style the dataframe
    styled_df = display_df.style.format({
        'Avg Price': '₹{:.2f}',
        'LTP': '₹{:.2f}',
        'Current Value': '₹{:,.0f}',
        'P&L': '₹{:,.0f}',
        'P&L %': '{:.1f}%'
    }).applymap(
        lambda x: 'color: green' if isinstance(x, (int, float)) and x > 0 
        else 'color: red' if isinstance(x, (int, float)) and x < 0 
        else '', subset=['P&L', 'P&L %']
    )
    
    st.dataframe(styled_df, use_container_width=True)
    
    return df

def create_portfolio_charts(df):
    """Create portfolio visualization charts"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🥧 Portfolio Allocation")
        fig_pie = px.pie(
            df, 
            values='Current Value', 
            names='Symbol',
            title="Holdings by Value"
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("#### 📊 P&L Analysis")
        fig_bar = px.bar(
            df,
            x='Symbol',
            y='P&L',
            title="Profit & Loss by Stock",
            color='P&L',
            color_continuous_scale=['red', 'yellow', 'green']
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

def display_market_movers():
    """Display top gainers and losers"""
    st.markdown("### 📈 Market Movers")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🟢 Top Gainers")
        gainers_data = pd.DataFrame({
            'Symbol': ['ADANIPORTS', 'POWERGRID', 'NTPC', 'COALINDIA'],
            'LTP': [875.30, 245.60, 285.40, 395.20],
            'Change %': [8.5, 6.2, 5.8, 4.9]
        })
        
        styled_gainers = gainers_data.style.format({
            'LTP': '₹{:.2f}',
            'Change %': '+{:.1f}%'
        }).applymap(lambda x: 'color: green', subset=['Change %'])
        
        st.dataframe(styled_gainers, use_container_width=True)
    
    with col2:
        st.markdown("#### 🔴 Top Losers")
        losers_data = pd.DataFrame({
            'Symbol': ['BAJFINANCE', 'MARUTI', 'ASIANPAINT', 'NESTLEIND'],
            'LTP': [6250.80, 9845.60, 3285.40, 2195.20],
            'Change %': [-3.2, -2.8, -2.1, -1.9]
        })
        
        styled_losers = losers_data.style.format({
            'LTP': '₹{:.2f}',
            'Change %': '{:.1f}%'
        }).applymap(lambda x: 'color: red', subset=['Change %'])
        
        st.dataframe(styled_losers, use_container_width=True)

def display_quick_actions():
    """Display quick action buttons"""
    st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.sidebar.markdown("### ⚡ Quick Actions")
    
    if st.sidebar.button("🔄 Refresh Data"):
        # Clear cached data to force refresh
        st.session_state.holdings_data = None
        st.session_state.positions_data = None
        st.session_state.profile_data = None
        st.experimental_rerun()
    
    if st.sidebar.button("📊 View Orders"):
        st.sidebar.info("Orders panel would open here")
    
    if st.sidebar.button("💹 Place Order"):
        st.sidebar.info("Order placement form would open here")
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">📈 Portfolio Manager</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Powered by Kite Connect MCP Server</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("🎛️ Control Panel")
    
    # Display connection status
    is_connected = display_connection_status()
    
    # Authentication section
    if not is_connected:
        handle_authentication()
        st.warning("⚠️ Please authenticate with Kite Connect to view your portfolio data.")
        st.info("👆 Use the login button in the sidebar to get started.")
        
        # Show demo data
        st.markdown("### 🎯 Demo Portfolio (Sample Data)")
        st.info("This is sample data. Connect to your Kite account to see real portfolio data.")
        display_portfolio_summary()
        df = display_holdings_table()
        create_portfolio_charts(df)
        display_market_movers()
        
    else:
        # Load data
        load_profile_data()
        load_portfolio_data()
        
        # Display quick actions
        display_quick_actions()
        
        # Main content
        if st.session_state.profile_data:
            display_profile_info()
            st.markdown("---")
        
        display_portfolio_summary()
        df = display_holdings_table()
        create_portfolio_charts(df)
        display_market_movers()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>Built with ❤️ using Streamlit and Kite Connect MCP Server</p>
        <p><small>⚠️ This is a demo application. Always verify data before making trading decisions.</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
