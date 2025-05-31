"""
Script to run the CTchargen backend server.
"""
import os
import sys
import uvicorn

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def main():
    """Run the backend server."""
    print("Starting CTchargen backend server...")
    uvicorn.run(
        "web.backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

if __name__ == "__main__":
    main()
