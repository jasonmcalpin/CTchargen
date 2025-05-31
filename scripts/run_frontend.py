"""
Script to run the CTchargen frontend development server.
"""
import os
import sys
import subprocess

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def main():
    """Run the frontend development server."""
    print("Starting CTchargen frontend development server...")
    
    # Get the frontend directory
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web", "frontend")
    
    # Check if node_modules exists
    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):
        print("Installing frontend dependencies...")
        subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
    
    # Run the development server
    subprocess.run(["npm", "run", "dev"], cwd=frontend_dir, check=True)

if __name__ == "__main__":
    main()
