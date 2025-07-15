# 🎛️ Perpetuum

Perpetuum is a sleek, modern desktop app designed to simulate user activity by randomly browsing URLs, switching tabs, scrolling, and typing to mimic active work behavior. Built with PyQt6, it features a minimalist dark theme and easy keyboard controls to evade network AI monitoring systems that track employee activity.

## 🚀 Features
- **Randomized user activity simulation**:
  - Opens random URLs from a user-defined list
  - Switches browser tabs
  - Simulates scrolling
  - Mimics typing
- **Minimalist dark UI** with a modern aesthetic
- **Keyboard controls**:
  - `ENTER` → Start simulation
  - `SPACE` → Stop simulation
- **Customizable URL list** via text input
- **Randomized timing** (actions occur every 5-15 seconds)
- **Custom app icon** (`logo.png`)
- **Standalone macOS app build**

## 🖥️ Installation
### 🛠️ Requirements
- **Python 3.7+**
- **PyQt6**
- **PyInstaller** (for building the app)
- **pyautogui**

### 📥 Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/Perpetuum.git
cd worksim

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 📜 requirements.txt
```
PyQt6
pyautogui
PyInstaller
```

## 🏗️ Building the App (macOS)
```bash
chmod +x build.sh
./build.sh
```
After building, **Perpetuum.app** will be moved to your `/Applications/` folder.

**Important**: Go to **System Preferences > Security & Privacy > Privacy > Accessibility** and allow the app to control your computer for mouse and keyboard simulation.

## 🏃‍♂️ Running the App
```bash
python main.py
```

## 🎮 Usage
1. Enter a comma-separated list of URLs in the input field (or use default URLs).
2. Press `ENTER` to start the simulation.
3. Press `SPACE` to stop the simulation.
4. The app will randomly perform actions (open URLs, switch tabs, scroll, or type) every 5-15 seconds.

## 📸 Screenshots
🚀 [Include a screenshot of the app here]

## 🤝 Contributing
Feel free to open issues or submit pull requests if you have improvements.

## 📜 License
MIT License. See `LICENSE` file for details.

## 🌟 Credits
Developed by **[Your Name]**. Inspired by the need to simulate active work behavior with PyQt6 and pyautogui.
