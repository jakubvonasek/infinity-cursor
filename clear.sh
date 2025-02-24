#!/bin/bash

# Define directories and files to remove
BUILD_DIRS=("build" "dist" "__pycache__")
SPEC_FILE="InfinityCursor.spec"
APP_NAME="InfinityCursor"

# Remove build directories
echo "🧹 Cleaning build directories..."
for dir in "${BUILD_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
        echo "Removed $dir"
    fi
done

# Remove .spec file
if [ -f "$SPEC_FILE" ]; then
    rm "$SPEC_FILE"
    echo "Removed $SPEC_FILE"
fi

# Remove app bundle from Applications (macOS)
if [ -d "/Applications/$APP_NAME.app" ]; then
    rm -rf "/Applications/$APP_NAME.app"
    echo "Removed /Applications/$APP_NAME.app"
fi

echo "✅ Project cleaned! It's now in a fresh state."