import sys
import math
import time
import threading
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QCursor, QIcon
from PyQt6.QtCore import Qt, QPoint

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

class PerpetuumApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("«« ÷÷ PERPETUUM ÷÷ »»")
        self.setWindowIcon(QIcon("./logo.png"))  # Set app logo
        self.setGeometry(100, 100, 400, 300)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(
            "background-color: #121212;"
            "background-image: url(./logo.png); background-position: center; background-repeat: no-repeat;"
        )
        self.activateWindow()
        self.setFocus()

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