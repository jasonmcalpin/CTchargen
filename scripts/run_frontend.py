"""
Script to run the CTchargen frontend development server.
"""
import os
import sys
import subprocess
import shutil

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def main():
    """Run the frontend development server."""
    print("Starting CTchargen frontend development server...")
    
    # Get the frontend directory
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web", "frontend")
    
    # Find npm in the PATH
    npm_path = shutil.which("npm")
    if not npm_path:
        print("Error: npm not found in PATH. Please install Node.js and npm.")
        sys.exit(1)
    
    print(f"Using npm from: {npm_path}")
    
    # Check if node_modules exists
    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):
        print("Installing frontend dependencies...")
        subprocess.run([npm_path, "install"], cwd=frontend_dir, env=os.environ.copy(), check=True)
    
    # Run the development server
    subprocess.run([npm_path, "run", "dev"], cwd=frontend_dir, env=os.environ.copy(), check=True)

if __name__ == "__main__":
    main()
