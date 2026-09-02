import sys
import math
import time
import threading
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QCursor, QIcon, QPainter, QPixmap
from PyQt6.QtCore import Qt, QPoint, QTimer

# Global variables
running = False
speed = 1.0  # Default speed (1 loop per second)
running_time = 0.0
idle_time = 0.0

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

class PerpetuumApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("./logo.png"))  # Set app logo
        self.setGeometry(100, 100, 400, 300)
        self.logo = QPixmap("./logo.png")
        self.logo_opacity = 0.0
        self.activateWindow()
        self.setFocus()

        self.entropy_timer = QTimer(self)
        self.entropy_timer.timeout.connect(self.update_entropy)
        self.entropy_timer.start(1000)
        self.update_entropy()

    def update_entropy(self):
        global running_time, idle_time
        if running:
            running_time += 1
        else:
            idle_time += 1
        total = running_time + idle_time
        pct = running_time / total * 100 if total else 0
        self.setWindowTitle(f"∞ {pct:.0f}% flow — {int(running_time)}s running / {int(idle_time)}s idle")
        self.logo_opacity = pct / 100
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.GlobalColor.black)
        painter.setOpacity(self.logo_opacity)
        x = (self.width() - self.logo.width()) // 2
        y = (self.height() - self.logo.height()) // 2
        painter.drawPixmap(x, y, self.logo)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.start_movement()
        elif event.key() == Qt.Key.Key_Space:
            self.stop_movement()

    def mousePressEvent(self, event):
        """Swallow clicks while the cursor is moving so they can't interrupt the flow."""
        if running:
            return
        super().mousePressEvent(event)

    def start_movement(self):
        global running
        if not running:
            running = True
            threading.Thread(target=move_cursor, args=(self,), daemon=True).start()

    def stop_movement(self):
        global running
        running = False

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PerpetuumApp()
    window.show()
    sys.exit(app.exec())