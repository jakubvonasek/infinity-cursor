# 🎛️ Infinity Cursor

Infinity Cursor is a sleek, modern desktop app that smoothly moves your mouse in an infinity-shaped loop **inside the app window**. Designed with PyQt6, it features a minimalist dark theme and easy keyboard controls.

## 🚀 Features
- **Infinity symbol cursor movement** within the app window
- **Minimalist dark UI** with a modern aesthetic
- **Keyboard controls**:
  - `ENTER` → Start cursor movement
  - `SPACE` → Stop cursor movement
- **Adjustable speed** (from 0.5 to 2 loops per second)
- **Custom app icon** (`logo.png`)
- **Standalone macOS app build**

## 🖥️ Installation
### 🛠️ Requirements
- **Python 3.7+**
- **PyQt6**
- **PyInstaller** (for building the app)

### 📥 Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/infinity-cursor.git
cd infinity-cursor

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏗️ Building the App (macOS)
```bash
chmod +x build.sh
./build.sh
```
After building, **Infinity Cursor.app** will be moved to your `/Applications/` folder.

## 🏃‍♂️ Running the App
```bash
python main.py
```

## 📸 Screenshots
🚀 [Include a screenshot of the app here]

## 🤝 Contributing
Feel free to open issues or submit pull requests if you have improvements.

## 📜 License
MIT License. See `LICENSE` file for details.

## 🌟 Credits
Developed by **[Your Name]**. Inspired by smooth cursor automation with PyQt6.
