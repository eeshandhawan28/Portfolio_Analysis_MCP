"""
Multi-page Streamlit application for Portfolio Management
"""

import streamlit as st
from pages.portfolio_dashboard import main as portfolio_main
from pages.order_management import display_order_form, display_orders_table, display_trades_table
from pages.market_data import display_market_overview, display_stock_chart, display_watchlist, display_sector_performance

# Page configuration
st.set_page_config(
    page_title="Portfolio Manager - Kite MCP",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application with navigation"""
    
    # Sidebar navigation
    st.sidebar.title("📊 Navigation")
    
    page = st.sidebar.radio(
        "Go to",
        ["🏠 Dashboard", "📋 Orders", "📈 Market Data", "⚙️ Settings"]
    )
    
    if page == "🏠 Dashboard":
        portfolio_main()
    
    elif page == "📋 Orders":
        st.title("📋 Order Management")
        
        tab1, tab2, tab3 = st.tabs(["Place Order", "Order Book", "Trade History"])
        
        with tab1:
            display_order_form()
        
        with tab2:
            display_orders_table()
        
        with tab3:
            display_trades_table()
    
    elif page == "📈 Market Data":
        st.title("📈 Market Data & Analysis")
        
        display_market_overview()
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            display_stock_chart()
        
        with col2:
            display_watchlist()
            st.markdown("---")
            display_sector_performance()
    
    elif page == "⚙️ Settings":
        st.title("⚙️ Settings")
        
        st.markdown("### 🔧 Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### MCP Server Settings")
            server_url = st.text_input("MCP Server URL", value="http://localhost:8080/mcp")
            st.selectbox("Connection Mode", ["HTTP", "SSE", "Stdio"])
            
            st.markdown("#### Display Settings")
            st.selectbox("Theme", ["Light", "Dark"])
            st.slider("Refresh Interval (seconds)", 5, 60, 30)
        
        with col2:
            st.markdown("#### API Configuration")
            st.text_input("API Key", type="password", placeholder="Enter your Kite API key")
            st.text_input("API Secret", type="password", placeholder="Enter your Kite API secret")
            
            st.markdown("#### Alerts")
            st.checkbox("Price Alerts")
            st.checkbox("Order Notifications")
            st.checkbox("Portfolio Updates")
        
        if st.button("💾 Save Settings"):
            st.success("Settings saved successfully!")

if __name__ == "__main__":
    main()
