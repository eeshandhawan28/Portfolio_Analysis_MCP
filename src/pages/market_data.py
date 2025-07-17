"""
Market Data Module - Handle real-time market data and analysis
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import numpy as np

def display_market_overview():
    """Display market overview with indices"""
    st.markdown("### 📊 Market Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("NIFTY 50", "21,456.80", "+245.60 (+1.16%)")
    
    with col2:
        st.metric("SENSEX", "71,283.50", "+512.30 (+0.72%)")
    
    with col3:
        st.metric("BANK NIFTY", "48,756.25", "+187.45 (+0.39%)")
    
    with col4:
        st.metric("NIFTY IT", "32,145.60", "+428.90 (+1.35%)")

def create_sample_candlestick_data():
    """Create sample candlestick data"""
    dates = pd.date_range(start='2024-01-01', end='2024-01-15', freq='D')
    np.random.seed(42)
    
    open_price = 2500
    prices = []
    
    for i in range(len(dates)):
        change = np.random.normal(0, 50)
        open_val = open_price
        close_val = open_price + change
        high_val = max(open_val, close_val) + abs(np.random.normal(0, 20))
        low_val = min(open_val, close_val) - abs(np.random.normal(0, 20))
        
        prices.append({
            'Date': dates[i],
            'Open': open_val,
            'High': high_val,
            'Low': low_val,
            'Close': close_val,
            'Volume': np.random.randint(100000, 1000000)
        })
        
        open_price = close_val
    
    return pd.DataFrame(prices)

def display_stock_chart():
    """Display interactive stock chart"""
    st.markdown("### 📈 Stock Chart")
    
    # Sample stock selection
    selected_stock = st.selectbox("Select Stock", 
                                 ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ITC"])
    
    # Create sample data
    df = create_sample_candlestick_data()
    
    # Create candlestick chart
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(f'{selected_stock} Price Chart', 'Volume'),
        row_width=[0.7, 0.3]
    )
    
    # Add candlestick
    fig.add_trace(
        go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name=selected_stock
        ),
        row=1, col=1
    )
    
    # Add volume bars
    fig.add_trace(
        go.Bar(
            x=df['Date'],
            y=df['Volume'],
            name='Volume',
            marker_color='lightblue'
        ),
        row=2, col=1
    )
    
    fig.update_layout(
        title=f'{selected_stock} - Price and Volume',
        xaxis_rangeslider_visible=False,
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

def display_watchlist():
    """Display user watchlist"""
    st.markdown("### 👀 Watchlist")
    
    watchlist_data = pd.DataFrame({
        'Symbol': ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ITC', 'SBIN'],
        'LTP': [2580.30, 3420.50, 1650.75, 1720.40, 445.80, 545.60],
        'Change': [45.20, 125.30, 85.50, 15.60, 12.40, 18.90],
        'Change %': [1.78, 3.80, 5.46, 0.92, 2.86, 3.59],
        'Volume': [1250000, 850000, 2100000, 1800000, 3200000, 4500000]
    })
    
    # Color coding for change
    def color_change(val):
        return 'color: green' if val > 0 else 'color: red'
    
    styled_watchlist = watchlist_data.style.applymap(
        color_change, subset=['Change', 'Change %']
    ).format({
        'LTP': '₹{:.2f}',
        'Change': '{:+.2f}',
        'Change %': '{:+.2f}%',
        'Volume': '{:,}'
    })
    
    st.dataframe(styled_watchlist, use_container_width=True)

def display_sector_performance():
    """Display sector performance"""
    st.markdown("### 🏭 Sector Performance")
    
    sectors_data = pd.DataFrame({
        'Sector': ['IT', 'Banking', 'Pharma', 'Auto', 'FMCG', 'Metals', 'Energy', 'Realty'],
        'Change %': [2.45, 1.23, -0.87, 3.12, 0.56, -1.45, 1.89, 4.23],
        'Top Stock': ['TCS', 'HDFCBANK', 'SUNPHARMA', 'MARUTI', 'ITC', 'TATAPOWER', 'RELIANCE', 'DLF']
    })
    
    # Create horizontal bar chart
    fig = go.Figure()
    
    colors = ['green' if x > 0 else 'red' for x in sectors_data['Change %']]
    
    fig.add_trace(go.Bar(
        y=sectors_data['Sector'],
        x=sectors_data['Change %'],
        orientation='h',
        marker_color=colors,
        text=sectors_data['Change %'],
        texttemplate='%{text:.2f}%',
        textposition='outside'
    ))
    
    fig.update_layout(
        title='Sector Performance Today',
        xaxis_title='Change %',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
