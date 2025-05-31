"""
Script to test the CTchargen installation.

This script checks if all the necessary components are installed and configured correctly.
"""
import os
import sys
import subprocess
import platform
import json

def check_python_version():
    """Check if Python version is compatible."""
    print(f"Python version: {platform.python_version()}")
    major, minor, _ = platform.python_version_tuple()
    if int(major) < 3 or (int(major) == 3 and int(minor) < 6):
        print("❌ Python version is too old. Python 3.6 or higher is required.")
        return False
    print("✅ Python version is compatible.")
    return True

def check_virtual_env():
    """Check if running in a virtual environment."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in a virtual environment.")
        return True
    print("❌ Not running in a virtual environment.")
    return False

def check_backend_dependencies():
    """Check if backend dependencies are installed."""
    try:
        import fastapi
        import uvicorn
        import pydantic
        print("✅ Backend dependencies are installed.")
        return True
    except ImportError as e:
        print(f"❌ Backend dependency missing: {e}")
        return False

def check_node_installation():
    """Check if Node.js is installed."""
    try:
        result = subprocess.run(["node", "--version"], check=True, capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"Node.js version: {version}")
        print("✅ Node.js is installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js is not installed or not in PATH.")
        return False

def check_frontend_dependencies():
    """Check if frontend dependencies are installed."""
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web", "frontend")
    node_modules = os.path.join(frontend_dir, "node_modules")
    if os.path.exists(node_modules):
        print("✅ Frontend dependencies are installed.")
        return True
    print("❌ Frontend dependencies are not installed.")
    return False

def check_config_file():
    """Check if config file exists and is valid."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    if not os.path.exists(config_path):
        print("❌ Config file not found.")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ Config file exists and is valid JSON.")
        return True
    except json.JSONDecodeError:
        print("❌ Config file exists but is not valid JSON.")
        return False

def check_output_directory():
    """Check if output directory exists."""
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")
    if os.path.exists(output_dir) and os.path.isdir(output_dir):
        print("✅ Output directory exists.")
        return True
    print("❌ Output directory does not exist.")
    return False

def main():
    """Run all checks."""
    print("Testing CTchargen installation...\n")
    
    checks = [
        ("Python version", check_python_version),
        ("Virtual environment", check_virtual_env),
        ("Backend dependencies", check_backend_dependencies),
        ("Node.js installation", check_node_installation),
        ("Frontend dependencies", check_frontend_dependencies),
        ("Configuration file", check_config_file),
        ("Output directory", check_output_directory),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 50)
    print("Installation Test Results:")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        all_passed = all_passed and result
        print(f"{name}: {status}")
    
    print("\nOverall result:", "✅ PASS" if all_passed else "❌ FAIL")
    
    if not all_passed:
        print("\nSome checks failed. Please fix the issues and run the test again.")
        print("You can run the installation script to fix most issues:")
        print("  python install.py")
    else:
        print("\nAll checks passed! The installation is complete and ready to use.")
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
