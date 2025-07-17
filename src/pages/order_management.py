"""
Order Management Module - Handle order placement and management
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from utils.kite_mcp_client import KiteMCPClient

def display_order_form():
    """Display order placement form"""
    st.markdown("### 📝 Place Order")
    
    with st.form("order_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            symbol = st.text_input("Symbol", placeholder="e.g., NSE:INFY")
            transaction_type = st.selectbox("Transaction Type", ["BUY", "SELL"])
            quantity = st.number_input("Quantity", min_value=1, value=1)
            price = st.number_input("Price", min_value=0.0, value=0.0, step=0.05)
        
        with col2:
            exchange = st.selectbox("Exchange", ["NSE", "BSE", "MCX", "NFO", "BFO"])
            order_type = st.selectbox("Order Type", ["LIMIT", "MARKET", "SL", "SL-M"])
            product = st.selectbox("Product", ["CNC", "MIS", "NRML"])
            variety = st.selectbox("Variety", ["regular", "co", "amo"])
        
        submitted = st.form_submit_button("🚀 Place Order", type="primary")
        
        if submitted:
            st.warning("⚠️ Order placement requires authentication. This is a demo.")
            st.info(f"Demo Order: {transaction_type} {quantity} shares of {symbol} at ₹{price}")

def display_orders_table():
    """Display orders table"""
    st.markdown("### 📋 Order Book")
    
    # Sample orders data
    orders_data = pd.DataFrame({
        'Order ID': ['240115000123456', '240115000123457', '240115000123458'],
        'Symbol': ['NSE:RELIANCE', 'NSE:TCS', 'NSE:INFY'],
        'Type': ['BUY', 'SELL', 'BUY'],
        'Quantity': [50, 25, 30],
        'Price': [2580.30, 3420.50, 1650.75],
        'Status': ['COMPLETE', 'PENDING', 'REJECTED'],
        'Time': ['10:15:23', '11:30:45', '14:22:18']
    })
    
    # Style the status column
    def color_status(val):
        if val == 'COMPLETE':
            return 'color: green'
        elif val == 'PENDING':
            return 'color: orange'
        elif val == 'REJECTED':
            return 'color: red'
        return ''
    
    styled_orders = orders_data.style.applymap(color_status, subset=['Status']).format({
        'Price': '₹{:.2f}'
    })
    
    st.dataframe(styled_orders, use_container_width=True)

def display_trades_table():
    """Display trades table"""
    st.markdown("### 💼 Trade History")
    
    # Sample trades data
    trades_data = pd.DataFrame({
        'Trade ID': ['T240115001', 'T240115002', 'T240115003', 'T240115004'],
        'Symbol': ['NSE:RELIANCE', 'NSE:TCS', 'NSE:INFY', 'NSE:SBIN'],
        'Type': ['BUY', 'SELL', 'BUY', 'SELL'],
        'Quantity': [50, 25, 30, 75],
        'Price': [2580.30, 3420.50, 1650.75, 545.60],
        'Value': [129015, 85512, 49522, 40920],
        'Date': ['2024-01-15', '2024-01-15', '2024-01-14', '2024-01-14']
    })
    
    styled_trades = trades_data.style.format({
        'Price': '₹{:.2f}',
        'Value': '₹{:,.0f}'
    })
    
    st.dataframe(styled_trades, use_container_width=True)
