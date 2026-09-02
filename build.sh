#!/bin/bash

# Define app name
APP_NAME="Perpetuum"
ICON_FILE="./logo.png"
SCRIPT_FILE="main.py"
SPEC_FILE="InfinityCursor.spec"
ENTITLEMENTS_FILE="entitlements.plist"
APP_PATH="/Applications/$APP_NAME.app"

echo "🛠️  Cleaning old builds..."
rm -rf build dist "$SPEC_FILE"

# Ensure PyQt6 is installed
if ! python3 -c "import PyQt6" &> /dev/null; then
    echo "⚠️  PyQt6 not found. Installing..."
    pip install PyQt6
fi

echo "🚀 Generating PyInstaller spec file..."
cat > "$SPEC_FILE" <<EOL
# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['$SCRIPT_FILE'],
    pathex=[],
    binaries=[],
    datas=[('$ICON_FILE', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='$APP_NAME',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file='$ENTITLEMENTS_FILE',
    icon=['$ICON_FILE'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='$APP_NAME',
)
app = BUNDLE(
    coll,
    name='$APP_NAME.app',
    icon='$ICON_FILE',
    bundle_identifier="cz.jakubvonasek.perpetuum",
)
EOL

# Create entitlements file for macOS permissions
echo "🔐 Creating entitlements file..."
cat > "$ENTITLEMENTS_FILE" <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.automation.apple-events</key>
    <true/>
    <key>com.apple.security.device.input-monitoring</key>
    <true/>
</dict>
</plist>
EOL

echo "🚀 Building $APP_NAME with PyInstaller..."
pyinstaller "$SPEC_FILE"

# Check if build was successful
if [ -d "dist/$APP_NAME.app" ]; then
    echo "✅ Build successful!"

    # Move the app to Applications
    echo "📂 Moving to Applications..."
    mv "dist/$APP_NAME.app" /Applications/

    # Sign the app to prevent macOS security restrictions
    echo "🔏 Signing the application..."
    codesign --force --deep --sign - "$APP_PATH"

    echo "🎉 Done! You can now open $APP_NAME from Applications."
    echo "If cursor control doesn't work, grant Accessibility: System Settings → Privacy & Security → Accessibility → Add $APP_NAME"
else
    echo "❌ Build failed! Check for errors."
fi