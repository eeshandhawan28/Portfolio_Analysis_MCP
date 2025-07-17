"""
Test script to verify the application setup and MCP connection
"""

import os
import sys
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages can be imported"""
    print("🔍 Testing package imports...")
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError:
        print("❌ Streamlit not found. Run: pip install streamlit")
        return False
    
    try:
        import pandas
        print("✅ Pandas imported successfully")
    except ImportError:
        print("❌ Pandas not found. Run: pip install pandas")
        return False
    
    try:
        import plotly
        print("✅ Plotly imported successfully")
    except ImportError:
        print("❌ Plotly not found. Run: pip install plotly")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError:
        print("❌ Requests not found. Run: pip install requests")
        return False
    
    return True

def test_env_file():
    """Test environment file configuration"""
    print("\n🔍 Testing environment configuration...")
    
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        print("   Create .env file: cp .env.example .env")
        return False
    
    load_dotenv()
    
    api_key = os.getenv('KITE_API_KEY')
    api_secret = os.getenv('KITE_API_SECRET')
    
    if not api_key or api_key == 'your_api_key_here':
        print("⚠️ KITE_API_KEY not configured properly")
        print("   Edit .env file with your actual API key")
    else:
        print("✅ KITE_API_KEY configured")
    
    if not api_secret or api_secret == 'your_api_secret_here':
        print("⚠️ KITE_API_SECRET not configured properly")
        print("   Edit .env file with your actual API secret")
    else:
        print("✅ KITE_API_SECRET configured")
    
    mcp_url = os.getenv('MCP_SERVER_URL', 'http://localhost:8080/mcp')
    print(f"📡 MCP Server URL: {mcp_url}")
    
    return True

def test_mcp_connection():
    """Test MCP server connection"""
    print("\n🔍 Testing MCP server connection...")
    
    try:
        import requests
        from dotenv import load_dotenv
        
        load_dotenv()
        mcp_url = os.getenv('MCP_SERVER_URL', 'http://localhost:8080/mcp')
        
        # Simple connectivity test
        response = requests.get(mcp_url.replace('/mcp', '/'), timeout=5)
        
        if response.status_code == 200:
            print("✅ MCP server is reachable")
            return True
        else:
            print(f"⚠️ MCP server returned status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to MCP server")
        print("   Make sure Kite MCP server is running at the configured URL")
        print("   For local server: go run main.go in kite-mcp-server directory")
        print("   For hosted server: use https://mcp.kite.trade/mcp")
        return False
    except Exception as e:
        print(f"❌ Error testing MCP connection: {e}")
        return False

def test_application_files():
    """Test if all application files exist"""
    print("\n🔍 Testing application files...")
    
    required_files = [
        'src/app.py',
        'src/pages/portfolio_dashboard.py',
        'src/pages/order_management.py',
        'src/pages/market_data.py',
        'src/utils/kite_mcp_client.py',
        'src/utils/utils.py',
        'config/requirements.txt'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("🧪 Running Portfolio Management Application Tests\n")
    
    results = []
    
    # Test imports
    results.append(test_imports())
    
    # Test files
    results.append(test_application_files())
    
    # Test environment
    results.append(test_env_file())
    
    # Test MCP connection
    results.append(test_mcp_connection())
    
    print("\n" + "="*50)
    print("📋 Test Summary")
    print("="*50)
    
    if all(results):
        print("🎉 All tests passed! Your application is ready to run.")
        print("\n🚀 To start the application:")
        print("   streamlit run app.py")
        print("\n🌐 The app will open at: http://localhost:8501")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("\n📖 For help, check:")
        print("   - README.md for detailed setup instructions")
        print("   - QUICKSTART.md for quick setup guide")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
