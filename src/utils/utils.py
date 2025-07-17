"""
Utility functions for the portfolio management application
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

def format_currency(amount: float, currency: str = "₹") -> str:
    """Format amount as currency"""
    if amount >= 10000000:  # 1 crore
        return f"{currency}{amount/10000000:.2f}Cr"
    elif amount >= 100000:  # 1 lakh
        return f"{currency}{amount/100000:.2f}L"
    elif amount >= 1000:  # 1 thousand
        return f"{currency}{amount/1000:.2f}K"
    else:
        return f"{currency}{amount:.2f}"

def format_percentage(value: float) -> str:
    """Format percentage with color coding"""
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"

def calculate_portfolio_metrics(holdings_data: List[Dict]) -> Dict[str, float]:
    """Calculate portfolio summary metrics"""
    if not holdings_data:
        return {
            'total_value': 0,
            'total_investment': 0,
            'total_pnl': 0,
            'total_pnl_percent': 0,
            'day_change': 0,
            'day_change_percent': 0
        }
    
    total_value = sum(holding.get('current_value', 0) for holding in holdings_data)
    total_investment = sum(holding.get('investment', 0) for holding in holdings_data)
    total_pnl = total_value - total_investment
    total_pnl_percent = (total_pnl / total_investment * 100) if total_investment > 0 else 0
    
    # Mock day change calculation
    day_change = total_value * 0.015  # Assume 1.5% day change
    day_change_percent = 1.5
    
    return {
        'total_value': total_value,
        'total_investment': total_investment,
        'total_pnl': total_pnl,
        'total_pnl_percent': total_pnl_percent,
        'day_change': day_change,
        'day_change_percent': day_change_percent
    }

def get_color_for_value(value: float) -> str:
    """Get color based on positive/negative value"""
    return "green" if value > 0 else "red" if value < 0 else "gray"

def generate_sample_data():
    """Generate sample data for demo purposes"""
    
    # Sample holdings
    holdings = [
        {
            'symbol': 'RELIANCE',
            'quantity': 50,
            'avg_price': 2450.50,
            'ltp': 2580.30,
            'current_value': 129015,
            'investment': 122525,
            'pnl': 6490,
            'pnl_percent': 5.3
        },
        {
            'symbol': 'TCS',
            'quantity': 25,
            'avg_price': 3250.75,
            'ltp': 3420.50,
            'current_value': 85512,
            'investment': 81269,
            'pnl': 4244,
            'pnl_percent': 5.2
        },
        {
            'symbol': 'INFY',
            'quantity': 30,
            'avg_price': 1520.25,
            'ltp': 1650.75,
            'current_value': 49522,
            'investment': 45607,
            'pnl': 3915,
            'pnl_percent': 8.6
        }
    ]
    
    # Sample orders
    orders = [
        {
            'order_id': '240115000123456',
            'symbol': 'NSE:RELIANCE',
            'type': 'BUY',
            'quantity': 50,
            'price': 2580.30,
            'status': 'COMPLETE',
            'time': '10:15:23'
        },
        {
            'order_id': '240115000123457',
            'symbol': 'NSE:TCS',
            'type': 'SELL',
            'quantity': 25,
            'price': 3420.50,
            'status': 'PENDING',
            'time': '11:30:45'
        }
    ]
    
    # Sample market data
    market_data = {
        'NIFTY50': {'value': 21456.80, 'change': 245.60, 'change_percent': 1.16},
        'SENSEX': {'value': 71283.50, 'change': 512.30, 'change_percent': 0.72},
        'BANKNIFTY': {'value': 48756.25, 'change': 187.45, 'change_percent': 0.39}
    }
    
    return {
        'holdings': holdings,
        'orders': orders,
        'market_data': market_data
    }

def validate_order_params(params: Dict[str, Any]) -> tuple[bool, str]:
    """Validate order parameters"""
    required_fields = ['symbol', 'transaction_type', 'quantity', 'order_type', 'product']
    
    for field in required_fields:
        if field not in params or not params[field]:
            return False, f"Missing required field: {field}"
    
    # Validate quantity
    if params['quantity'] <= 0:
        return False, "Quantity must be greater than 0"
    
    # Validate price for limit orders
    if params.get('order_type') == 'LIMIT' and params.get('price', 0) <= 0:
        return False, "Price must be greater than 0 for limit orders"
    
    return True, "Valid"

def create_mock_response(success: bool, data: Any = None, error: str = None) -> Dict:
    """Create mock MCP response"""
    return {
        'success': success,
        'data': data,
        'error': error
    }

def parse_instrument_token(symbol: str) -> Optional[int]:
    """Parse instrument token from symbol (mock implementation)"""
    # This is a mock implementation
    # In real implementation, this would look up from instruments list
    mock_tokens = {
        'NSE:RELIANCE': 738561,
        'NSE:TCS': 2953217,
        'NSE:INFY': 408065,
        'NSE:HDFCBANK': 341249,
        'NSE:ITC': 424961
    }
    return mock_tokens.get(symbol)

def generate_historical_data(symbol: str, days: int = 30) -> pd.DataFrame:
    """Generate mock historical data"""
    np.random.seed(42)
    dates = pd.date_range(end=datetime.now(), periods=days)
    
    # Starting price based on symbol
    base_prices = {
        'RELIANCE': 2500,
        'TCS': 3200,
        'INFY': 1500,
        'HDFCBANK': 1650,
        'ITC': 420
    }
    
    base_price = base_prices.get(symbol, 1000)
    prices = []
    current_price = base_price
    
    for date in dates:
        # Random walk with slight upward bias
        change_percent = np.random.normal(0.001, 0.02)  # 0.1% bias, 2% volatility
        change = current_price * change_percent
        
        open_price = current_price
        close_price = current_price + change
        high_price = max(open_price, close_price) * (1 + abs(np.random.normal(0, 0.01)))
        low_price = min(open_price, close_price) * (1 - abs(np.random.normal(0, 0.01)))
        volume = np.random.randint(100000, 2000000)
        
        prices.append({
            'date': date,
            'open': open_price,
            'high': high_price,
            'low': low_price,
            'close': close_price,
            'volume': volume
        })
        
        current_price = close_price
    
    return pd.DataFrame(prices)

def get_risk_metrics(holdings_data: List[Dict]) -> Dict[str, Any]:
    """Calculate portfolio risk metrics"""
    if not holdings_data:
        return {}
    
    # Calculate concentration risk
    total_value = sum(h.get('current_value', 0) for h in holdings_data)
    max_holding = max(h.get('current_value', 0) for h in holdings_data)
    concentration_ratio = (max_holding / total_value) * 100 if total_value > 0 else 0
    
    # Calculate sector diversification (mock)
    sectors = ['Technology', 'Finance', 'Energy', 'FMCG', 'Healthcare']
    sector_weights = [25, 30, 20, 15, 10]  # Mock weights
    
    # Risk score based on concentration
    risk_score = "Low"
    if concentration_ratio > 40:
        risk_score = "High"
    elif concentration_ratio > 25:
        risk_score = "Medium"
    
    return {
        'concentration_ratio': concentration_ratio,
        'max_holding_percent': concentration_ratio,
        'sector_diversification': dict(zip(sectors, sector_weights)),
        'risk_score': risk_score,
        'volatility': np.random.uniform(15, 25)  # Mock volatility
    }
