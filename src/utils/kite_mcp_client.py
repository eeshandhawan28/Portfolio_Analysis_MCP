"""
Kite MCP Client - A client library to interact with the Kite MCP Server
"""

import requests
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class MCPResponse:
    """Response from MCP server"""
    success: bool
    data: Any
    error: Optional[str] = None

class KiteMCPClient:
    """Client to interact with Kite MCP Server"""
    
    def __init__(self, server_url: str = "http://localhost:8080/mcp"):
        """
        Initialize the MCP client
        
        Args:
            server_url: URL of the MCP server
        """
        self.server_url = server_url
        self.session_id = None
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _make_request(self, tool_name: str, arguments: Dict[str, Any] = None) -> MCPResponse:
        """
        Make a request to the MCP server
        
        Args:
            tool_name: Name of the MCP tool to call
            arguments: Arguments to pass to the tool
            
        Returns:
            MCPResponse object
        """
        if arguments is None:
            arguments = {}
            
        payload = {
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        try:
            response = requests.post(
                self.server_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Extract content from MCP response
                if 'result' in result and 'content' in result['result']:
                    content = result['result']['content']
                    if content and len(content) > 0:
                        text_content = content[0].get('text', '')
                        try:
                            # Try to parse as JSON
                            data = json.loads(text_content)
                            return MCPResponse(success=True, data=data)
                        except json.JSONDecodeError:
                            # Return as text if not JSON
                            return MCPResponse(success=True, data=text_content)
                
                return MCPResponse(success=False, error="Invalid response format")
            else:
                return MCPResponse(success=False, error=f"HTTP {response.status_code}: {response.text}")
                
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return MCPResponse(success=False, error=str(e))
    
    def login(self) -> MCPResponse:
        """Login to Kite Connect API"""
        return self._make_request("login")
    
    def get_profile(self) -> MCPResponse:
        """Get user profile information"""
        return self._make_request("get_profile")
    
    def get_holdings(self, limit: int = None) -> MCPResponse:
        """Get portfolio holdings"""
        args = {}
        if limit:
            args['limit'] = limit
        return self._make_request("get_holdings", args)
    
    def get_positions(self, limit: int = None) -> MCPResponse:
        """Get current positions"""
        args = {}
        if limit:
            args['limit'] = limit
        return self._make_request("get_positions", args)
    
    def get_margins(self) -> MCPResponse:
        """Get account margins"""
        return self._make_request("get_margins")
    
    def get_orders(self, limit: int = None) -> MCPResponse:
        """Get all orders"""
        args = {}
        if limit:
            args['limit'] = limit
        return self._make_request("get_orders", args)
    
    def get_trades(self, limit: int = None) -> MCPResponse:
        """Get trading history"""
        args = {}
        if limit:
            args['limit'] = limit
        return self._make_request("get_trades", args)
    
    def get_quotes(self, instruments: List[str]) -> MCPResponse:
        """Get real-time quotes for instruments"""
        return self._make_request("get_quotes", {"instruments": instruments})
    
    def get_ltp(self, instruments: List[str]) -> MCPResponse:
        """Get last traded price for instruments"""
        return self._make_request("get_ltp", {"instruments": instruments})
    
    def search_instruments(self, query: str, filter_on: str = "tradingsymbol") -> MCPResponse:
        """Search for trading instruments"""
        return self._make_request("search_instruments", {
            "query": query,
            "filter_on": filter_on
        })
    
    def get_historical_data(self, instrument_token: int, from_date: str, 
                          to_date: str, interval: str = "day") -> MCPResponse:
        """Get historical price data"""
        return self._make_request("get_historical_data", {
            "instrument_token": instrument_token,
            "from_date": from_date,
            "to_date": to_date,
            "interval": interval
        })
    
    def place_order(self, variety: str, exchange: str, tradingsymbol: str,
                   transaction_type: str, quantity: int, product: str,
                   order_type: str, price: float = 0.0) -> MCPResponse:
        """Place a new order"""
        return self._make_request("place_order", {
            "variety": variety,
            "exchange": exchange,
            "tradingsymbol": tradingsymbol,
            "transaction_type": transaction_type,
            "quantity": quantity,
            "product": product,
            "order_type": order_type,
            "price": price
        })
