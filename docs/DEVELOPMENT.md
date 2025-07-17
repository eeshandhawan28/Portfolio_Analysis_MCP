# 🛠️ Development Guide

## Project Structure

```
portfolio-management-app/
├── src/                     # 📁 Application source code
│   ├── app.py              # 🚀 Main Streamlit app with navigation
│   ├── pages/              # 📄 Individual application pages
│   │   ├── portfolio_dashboard.py  # Portfolio overview
│   │   ├── order_management.py     # Order forms and tracking
│   │   └── market_data.py          # Charts and market analysis
│   └── utils/              # 🔧 Utility modules
│       ├── kite_mcp_client.py     # MCP client library
│       └── utils.py               # Helper functions
├── config/                  # ⚙️ Configuration files
│   ├── requirements.txt    # Python dependencies
│   └── .env.example       # Environment template
├── scripts/                # 🔨 Automation scripts
│   ├── setup.sh           # One-time setup
│   ├── run.sh             # Application runner
│   └── test_setup.py      # Setup verification
└── docs/                   # 📚 Documentation
    ├── README.md          # Main documentation
    ├── QUICKSTART.md      # Quick setup guide
    ├── FEATURES.md        # Feature comparison
    └── DEPLOYMENT.md      # Deployment guide
```

## 🏃‍♂️ Development Workflow

### Initial Setup
```bash
# 1. Clone repository
git clone <your-repo>
cd portfolio-management-app

# 2. Setup development environment
./scripts/setup.sh

# 3. Configure environment
cp config/.env.example .env
# Edit .env with your API keys

# 4. Start development server
./scripts/run.sh
```

### Making Changes

#### Adding New Pages
1. Create new file in `src/pages/`
2. Add import in `src/app.py`
3. Add navigation option in sidebar

Example:
```python
# src/pages/new_feature.py
import streamlit as st

def display_new_feature():
    st.title("New Feature")
    # Your feature code here

# src/app.py
from pages.new_feature import display_new_feature

# Add to navigation
page = st.sidebar.radio("Go to", [
    "🏠 Dashboard", 
    "📋 Orders", 
    "📈 Market Data", 
    "✨ New Feature",  # Add here
    "⚙️ Settings"
])

if page == "✨ New Feature":
    display_new_feature()
```

#### Adding New MCP Functions
1. Update `src/utils/kite_mcp_client.py`
2. Add new method to `KiteMCPClient` class

Example:
```python
def get_new_data(self, params: Dict[str, Any]) -> MCPResponse:
    """Get new data from MCP server"""
    return self._make_request("new_tool_name", params)
```

#### Adding Utility Functions
1. Add to `src/utils/utils.py`
2. Import in pages that need them

### Testing Changes

```bash
# Test setup
python scripts/test_setup.py

# Run with debug mode
echo "DEBUG=True" >> .env
streamlit run src/app.py --server.runOnSave true

# Manual testing checklist:
# - Authentication flow works
# - All pages load without errors  
# - MCP client connects successfully
# - Demo data displays correctly
```

## 🔧 Code Architecture

### MCP Client (`src/utils/kite_mcp_client.py`)
- Handles all communication with MCP server
- Manages authentication and session state
- Provides typed responses with error handling

### Pages (`src/pages/`)
- **portfolio_dashboard.py**: Main portfolio view with charts
- **order_management.py**: Order forms and order/trade tables
- **market_data.py**: Market overview, charts, watchlists

### Utils (`src/utils/utils.py`)
- Helper functions for formatting, calculations
- Sample data generation for demo mode
- Portfolio metrics and risk calculations

### Main App (`src/app.py`)
- Navigation and page routing
- Session state management
- Overall application structure

## 📝 Coding Standards

### Python Style
- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

### Streamlit Best Practices
- Use session state for data persistence
- Cache expensive operations with `@st.cache_data`
- Handle errors gracefully with try/catch
- Provide user feedback for all operations

### Error Handling
```python
try:
    response = mcp_client.some_operation()
    if response.success:
        st.success("Operation successful!")
        # Handle success
    else:
        st.error(f"Operation failed: {response.error}")
except Exception as e:
    st.error(f"Unexpected error: {str(e)}")
```

## 🐛 Debugging

### Common Issues

**Import Errors**
```bash
# Check if in virtual environment
which python
# Should show venv/bin/python

# Reinstall dependencies
pip install -r config/requirements.txt
```

**MCP Connection Issues**
```bash
# Test MCP server directly
curl http://localhost:8080/

# Check MCP server logs
# Look for errors in server output
```

**Authentication Problems**
- Clear browser cookies for Kite Connect
- Check API key permissions in Kite Console
- Verify .env file has correct credentials

### Debug Mode
```bash
# Enable debug logging
echo "DEBUG=True" >> .env

# Run with verbose output
streamlit run src/app.py --logger.level debug
```

## 🧪 Adding Tests

### Unit Tests
Create `tests/` directory:
```python
# tests/test_utils.py
import unittest
from src.utils.utils import format_currency

class TestUtils(unittest.TestCase):
    def test_format_currency(self):
        self.assertEqual(format_currency(1000), "₹1.00K")
        self.assertEqual(format_currency(1000000), "₹1.00L")

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests
```python
# tests/test_mcp_client.py
import unittest
from src.utils.kite_mcp_client import KiteMCPClient

class TestMCPClient(unittest.TestCase):
    def setUp(self):
        self.client = KiteMCPClient("http://localhost:8080/mcp")
    
    def test_connection(self):
        # Test basic connectivity
        pass
```

## 📦 Building for Production

### Environment Configuration
```bash
# Production .env
KITE_API_KEY=prod_key
KITE_API_SECRET=prod_secret
MCP_SERVER_URL=https://your-mcp-server.com/mcp
DEBUG=False
```

### Performance Optimization
- Use `@st.cache_data` for expensive operations
- Implement pagination for large datasets
- Optimize chart rendering with data sampling
- Use lazy loading for non-critical components

### Security Checklist
- [ ] API keys in environment variables
- [ ] No sensitive data in logs
- [ ] Input validation on all forms
- [ ] HTTPS in production
- [ ] Regular dependency updates

## 🚀 Deployment

### Streamlit Cloud
1. Push to GitHub
2. Connect repository to Streamlit Cloud
3. Configure secrets in dashboard
4. Deploy automatically

### Self-Hosted
```bash
# Install production dependencies
pip install -r config/requirements.txt

# Run with production settings
streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0
```

## 📋 Maintenance

### Regular Tasks
- Update dependencies: `pip install -r config/requirements.txt --upgrade`
- Check for Kite Connect API updates
- Monitor application performance
- Review and rotate API keys

### Monitoring
- Set up logging for production
- Monitor API usage and limits
- Track user authentication issues
- Performance metrics collection

## 🤝 Contributing

### Pull Request Process
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Make changes with tests
4. Update documentation
5. Submit pull request

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No hardcoded credentials
- [ ] Error handling implemented
