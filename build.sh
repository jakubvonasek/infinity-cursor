#!/bin/bash

# Define app name
APP_NAME="InfinityCursor"
ICON_FILE="./logo.png"
SCRIPT_FILE="main.py"

# Check for PyQt6
if ! python3 -c "import PyQt6" &> /dev/null; then
    echo "⚠️  PyQt6 not found. Installing..."
    pip install PyQt6
fi

echo "🛠️  Cleaning old builds..."
rm -rf build dist "$APP_NAME.spec"

echo "🚀 Building $APP_NAME..."
pyinstaller --onedir --windowed --name "$APP_NAME" --icon="$ICON_FILE" "$SCRIPT_FILE"

# Check if build was successful
if [ -d "dist/$APP_NAME.app" ]; then
    echo "✅ Build successful! Moving to Applications..."
    mv "dist/$APP_NAME.app" /Applications/
    echo "🎉 Done! You can now open $APP_NAME from Applications."
else
    echo "❌ Build failed! Check for errors."
fi
