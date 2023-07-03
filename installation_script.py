import subprocess
# Check if tqdm is installed
try:
    import tqdm
except ImportError:
    print("Installing tqdm...")
    subprocess.run(["pip", "install", "tqdm"])

from tqdm import tqdm

# Check if Homebrew is installed and update it if necessary
brew_installed = subprocess.run(["which", "brew"], capture_output=True, text=True).stdout.strip()
if brew_installed:
    print("Homebrew is already installed.")
    subprocess.run(["brew", "update"])
else:
    print("Installing Homebrew...")
    subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])

# Install or update Carthage
carthage_installed = subprocess.run(["which", "carthage"], capture_output=True, text=True).stdout.strip()
if carthage_installed:
    print("Carthage is already installed.")
    subprocess.run(["brew", "upgrade", "carthage"])
else:
    print("Installing Carthage...")
    subprocess.run(["brew", "install", "carthage"])

# Install or update Node.js
node_installed = subprocess.run(["which", "node"], capture_output=True, text=True).stdout.strip()
if node_installed:
    print("Node.js is already installed.")
    subprocess.run(["brew", "upgrade", "node"])
else:
    print("Installing Node.js...")
    subprocess.run(["brew", "install", "node"])

# Install or update appium-doctor
appium_doctor_installed = subprocess.run(["which", "appium-doctor"], capture_output=True, text=True).stdout.strip()
if appium_doctor_installed:
    print("appium-doctor is already installed.")
    subprocess.run(["npm", "install", "-g", "appium-doctor"])
else:
    print("Installing appium-doctor...")
    subprocess.run(["npm", "install", "-g", "appium-doctor"])

# Install or update Appium
appium_installed = subprocess.run(["which", "appium"], capture_output=True, text=True).stdout.strip()
if appium_installed:
    print("Appium is already installed.")
    subprocess.run(["npm", "install", "-g", "appium"])
else:
    print("Installing Appium...")
    subprocess.run(["npm", "install", "-g", "appium"])

# Install or update Appium Inspector
appium_inspector_installed = subprocess.run(["which", "appium-inspector"], capture_output=True, text=True).stdout.strip()
if appium_inspector_installed:
    print("Appium Inspector is already installed.")
    subprocess.run(["npm", "install", "-g", "appium-inspector"])
else:
    print("Installing Appium Inspector...")
    subprocess.run(["npm", "install", "-g", "appium-inspector"])

# Check if Xcode is installed and update it if necessary
xcode_installed = subprocess.run(["which", "xcode-select"], capture_output=True, text=True).stdout.strip()
if xcode_installed:
    print("Xcode command line tools are already installed.")
else:
    print("Installing Xcode command line tools...")
    subprocess.run(["xcode-select", "--install"])

print("Installation and updates completed successfully.")
