import sys
import math
import time
import threading
import pyautogui
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt6.QtGui import QFont, QCursor, QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer, QPoint

# Global variables
running = False
speed = 1.0  # Default speed (1 loop per second)

def move_cursor(window):
    global running, speed
    A, B = window.width() // 4, window.height() // 4  # Width and height relative to the window
    center_x, center_y = window.width() // 2, window.height() // 2
    t = 0
    
    while running:
        x = center_x + A * math.cos(t)
        y = center_y + (B * math.sin(2 * t) / 2)
        window.setCursor(QCursor())  # Ensure cursor object exists
        window.cursor().setPos(window.mapToGlobal(QPoint(int(x), int(y))))
        t += 0.05
        time.sleep(1 / (speed * (2 * math.pi / 0.05)))  # Adjust sleep for whole loops

class InfinityCursorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("∞ Infinity Cursor")
        self.setWindowIcon(QIcon("./logo.png"))  # Set app logo
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #121212; color: white;")

        # Set font
        font = QFont("Arial", 12, QFont.Weight.Bold)

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        self.title_label = QLabel("∞ Infinity Cursor")
        self.title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        # Instruction Label
        self.helper_label = QLabel("Press ENTER to start, SPACE to stop")
        self.helper_label.setFont(font)
        self.helper_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.helper_label)

        # Speed Slider
        self.speed_label = QLabel("⏳ Speed")
        self.speed_label.setFont(font)
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.speed_label)

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)  # 0.5 loops per second
        self.speed_slider.setMaximum(4)  # 2 loops per second
        self.speed_slider.setValue(2)  # Default to 1 loop per second
        self.speed_slider.setStyleSheet("background: #1E1E1E; padding: 10px; border-radius: 5px;")
        self.speed_slider.valueChanged.connect(self.set_speed)
        layout.addWidget(self.speed_slider)

        self.setLayout(layout)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

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
        speed = value / 2  # Convert slider value to loops per second (0.5 - 2)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.stop_movement()
        elif event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.start_movement()

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfinityCursorApp()
    window.show()
    sys.exit(app.exec())
