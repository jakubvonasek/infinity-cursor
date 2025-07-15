import pyautogui
import time
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QPoint

# disable failsafe
pyautogui.FAILSAFE = False

app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 400, 300)
window.show()

print("Testing cursor movement...")
print(f"Window size: {window.width()}x{window.height()}")

# test coordinate conversion
center_x, center_y = window.width() // 2, window.height() // 2
global_pos = window.mapToGlobal(QPoint(center_x, center_y))
print(f"Window center: ({center_x}, {center_y})")
print(f"Screen center: ({global_pos.x()}, {global_pos.y()})")

# move cursor to window center
pyautogui.moveTo(global_pos.x(), global_pos.y())
print(f"Cursor moved to: {pyautogui.position()}")

time.sleep(2)
print("Test complete!") 