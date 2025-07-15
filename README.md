# ♾️ Perpetuum

Perpetuum is a lightweight desktop application designed to keep your screen active by simulating mouse movement in an infinity-shaped loop **within the app window**. Built with PyQt6, it features a minimalist dark theme and simple keyboard controls to evade activity monitoring by certain applications.

## 🚀 Purpose
This app prevents your computer from going idle by continuously moving the mouse cursor in a smooth, infinity-shaped pattern within its window, helping you bypass apps that track user activity or enforce screen timeouts.

## 🛠️ Features
- **Simulated mouse movement** in an infinity loop to keep your screen active
- **Confined to app window** to avoid interfering with other applications
- **Minimalist dark UI** for a clean, modern look
- **Keyboard controls**:
  - `ENTER` → Start mouse movement
  - `SPACE` → Stop mouse movement
- **Adjustable loop speed** (0.5 to 2 loops per second)
- **Custom app icon** (`logo.png`)
- **Standalone macOS app build**

## 🖥️ Installation
### 📋 Requirements
- **Python 3.7+**
- **PyQt6**
- **PyInstaller** (for building the standalone app)

### 📥 Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/perpetuum.git
cd perpetuum

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏗️ Building the App (macOS)
```bash
chmod +x build.sh
./build.sh
```
The built **Perpetuum.app** will be moved to your `/Applications/` folder.

⚠️ **Important step!** ⚠️
After building the app, you will need to go to:
**System Settings > Privacy & Security > Accessibility** and add Perpetuum to the list.
Otherwise the app will not have access to your mouse controlls and will not work.

## 🏃‍♂️ Running the App
```bash
python main.py
```

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance functionality or fix bugs.

## 📜 License
MIT License. See `LICENSE` file for details.

## 🌟 Credits
Developed by **Jakub Vonasek**. Powered by PyQt6 for seamless cursor automation.
