import importlib
import subprocess

def check_openai():
    """
    Checks if the OpenAI package is installed. If not, it installs it.
    """
    try:
        importlib.import_module('openai')
        print("✅ Necessary packages are installed!")
    except ModuleNotFoundError:
        print("⏳ Necessary packages are not installed, we will install it...")
        try:
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("✅ The packages were installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Problem encountered trying to install the packages.")