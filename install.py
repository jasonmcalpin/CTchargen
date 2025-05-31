"""
Installation script for CTchargen.

This script sets up the project by:
1. Creating a virtual environment
2. Installing Python dependencies
3. Setting up the frontend
4. Creating necessary directories
"""
import os
import sys
import subprocess
import shutil
import platform

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def main():
    """Run the installation process."""
    print("Starting CTchargen installation...")
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Create virtual environment
    print("\nCreating virtual environment...")
    venv_path = os.path.join(project_root, "venv")
    if os.path.exists(venv_path):
        print("Virtual environment already exists.")
    else:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Virtual environment created.")
    
    # Determine the activate script based on the platform
    if platform.system() == "Windows":
        activate_script = os.path.join(venv_path, "Scripts", "activate")
        python_path = os.path.join(venv_path, "Scripts", "python")
        pip_path = os.path.join(venv_path, "Scripts", "pip")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")
        python_path = os.path.join(venv_path, "bin", "python")
        pip_path = os.path.join(venv_path, "bin", "pip")
    
    # Install Python dependencies
    print("\nInstalling Python dependencies...")
    backend_requirements = os.path.join(project_root, "web", "backend", "requirements.txt")
    if os.path.exists(backend_requirements):
        subprocess.run([pip_path, "install", "-r", backend_requirements], check=True)
        print("Backend dependencies installed.")
    else:
        print("Backend requirements file not found.")
    
    # Create output directory
    print("\nCreating output directory...")
    output_dir = os.path.join(project_root, "output")
    create_directory(output_dir)
    
    # Set up frontend
    print("\nSetting up frontend...")
    frontend_dir = os.path.join(project_root, "web", "frontend")
    if os.path.exists(os.path.join(frontend_dir, "package.json")):
        # Check if Node.js is installed
        try:
            subprocess.run(["node", "--version"], check=True, stdout=subprocess.PIPE)
            print("Node.js is installed.")
            
            # Install frontend dependencies
            print("Installing frontend dependencies...")
            subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
            print("Frontend dependencies installed.")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Node.js is not installed. Please install Node.js to set up the frontend.")
    else:
        print("Frontend package.json not found.")
    
    # Make run scripts executable on Unix-like systems
    if platform.system() != "Windows":
        print("\nMaking run scripts executable...")
        for script in ["run_backend.sh", "run_frontend.sh"]:
            script_path = os.path.join(project_root, script)
            if os.path.exists(script_path):
                os.chmod(script_path, 0o755)
                print(f"Made {script} executable.")
    
    print("\nInstallation completed successfully!")
    print("\nTo run the backend server:")
    if platform.system() == "Windows":
        print("  run_backend.bat")
    else:
        print("  ./run_backend.sh")
    
    print("\nTo run the frontend development server:")
    if platform.system() == "Windows":
        print("  run_frontend.bat")
    else:
        print("  ./run_frontend.sh")

if __name__ == "__main__":
    main()
