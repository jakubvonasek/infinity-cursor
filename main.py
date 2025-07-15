import os
import sys
import math
import time
import threading
import pyautogui
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt6.QtGui import QFont, QCursor, QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer, QPoint

# Disable pyautogui failsafe
pyautogui.FAILSAFE = False

# Manually add environment variables
os.environ['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
os.environ['PYTHONPATH'] = sys.prefix

print(f"Current PATH: {os.environ['PATH']}")
print(f"Current PYTHONPATH: {os.environ['PYTHONPATH']}")

# Global variables
running = False
speed = 5.0

def move_cursor(window):
    global running, speed
    try:
        # use window-relative coordinates
        A, B = window.width() // 4, window.height() // 4
        center_x, center_y = window.width() // 2, window.height() // 2
        print(f"[debug] Window size: {window.width()}x{window.height()}, A={A}, B={B}")
        t = 0
        while running:
            x = center_x + A * math.cos(t * 0.1)  # slower rotation
            y = center_y + (B * math.sin(2 * t * 0.1) / 2)
            global_pos = window.mapToGlobal(QPoint(int(x), int(y)))
            pyautogui.moveTo(global_pos.x(), global_pos.y(), duration=0.01)  # smooth movement
            time.sleep(0.016)  # ~60fps
            t += 1  # speed-based step
    except Exception as e:
        print(f"[error] move_cursor failed: {e}")
        running = False

class InfinityCursorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("∞ Infinity Cursor")
        try:
            self.setWindowIcon(QIcon("./logo.png"))
        except FileNotFoundError:
            print("[warning] logo.png not found, skipping icon")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #121212; color: white;")

        font = QFont("Arial", 12, QFont.Weight.Bold)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        self.title_label = QLabel("∞ Infinity Cursor")
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.helper_label = QLabel("Press ENTER to start, SPACE to stop")
        self.helper_label.setFont(font)
        self.helper_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.helper_label)

        self.speed_label = QLabel("⏳ Speed")
        self.speed_label.setFont(font)
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.speed_label)

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(10)
        self.speed_slider.setMaximum(100)
        self.speed_slider.setValue(50)
        self.speed_slider.setStyleSheet("background: #1E1E1E; padding: 10px; border-radius: 5px;")
        self.speed_slider.valueChanged.connect(self.set_speed)
        layout.addWidget(self.speed_slider)

        self.debug_label = QLabel("🔍 Key Pressed: None")
        self.debug_label.setFont(font)
        self.debug_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.debug_label)

        self.setLayout(layout)

        self.activateWindow()
        self.setFocus()

    def keyPressEvent(self, event):
        key_name = event.text() or str(event.key())
        print(f"Key Pressed: {key_name}")
        self.debug_label.setText(f"🔍 Key Pressed: {key_name}")

        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            print(f"[key] {key_name} pressed, cursor at: {pyautogui.position()}")
            self.start_movement()
        elif event.key() == Qt.Key.Key_Space:
            self.stop_movement()

    def start_movement(self):
        global running
        if not running:
            running = True
            threading.Thread(target=move_cursor, args=(self,), daemon=True).start()

    def stop_movement(self):
        global running
        running = False

    def set_speed(self, value):
        global speed
        speed = value
        print(f"[speed] Set to {speed}x")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfinityCursorApp()
    window.show()
    window.activateWindow()
    window.setFocus()
    sys.exit(app.exec())