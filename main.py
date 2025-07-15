import sys
import random
import time
import webbrowser
import pyautogui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QGridLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon, QFont

class Perpetuum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("∞ Perpetuum - Eternea Update")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setWindowIcon(QIcon('logo.png'))
        self.is_running = False
        self.default_urls = [
            "https://news.ycombinator.com",
            "https://www.bbc.com",
            "https://www.stackoverflow.com",
            "https://www.github.com",
            "https://www.reddit.com"
        ]
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Title
        title_label = QLabel("∞ Eternea")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # URL configuration section
        url_label = QLabel("Configure URLs:")
        url_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        url_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(url_label)

        # URL edit boxes in grid
        url_grid = QGridLayout()
        self.url_inputs = []
        for i, url in enumerate(self.default_urls):
            label = QLabel(f"URL {i+1}:")
            label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            label.setStyleSheet("margin-right: 10px;")
            input_box = QLineEdit(url)
            input_box.setStyleSheet("background: #1a1a1a; padding: 10px; border-radius: 5px; color: #cccccc;")
            url_grid.addWidget(label, i, 0)
            url_grid.addWidget(input_box, i, 1)
            self.url_inputs.append(input_box)
        layout.addLayout(url_grid)

        # Status label
        self.status_label = QLabel("Status: Stopped")
        self.status_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        # Buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start (Enter)")
        self.start_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.start_button.setStyleSheet("background: #1E1E1E; padding: 10px; border-radius: 5px; color: white;")
        self.start_button.clicked.connect(self.start_simulation)
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop (Space)")
        self.stop_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.stop_button.setStyleSheet("background: #1E1E1E; padding: 10px; border-radius: 5px; color: white;")
        self.stop_button.clicked.connect(self.stop_simulation)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)

        # Activity log
        log_label = QLabel("Activity Log:")
        log_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        log_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(log_label)

        self.log_area = QTextEdit()
        self.log_area.setStyleSheet("background: #1E1E1E; padding: 10px; border-radius: 5px; color: white;")
        self.log_area.setMaximumHeight(150)
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        # Timer for random actions
        self.timer = QTimer()
        self.timer.timeout.connect(self.perform_random_action)

    def log_activity(self, message):
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.log_area.append(log_entry)
        # auto-scroll to bottom
        self.log_area.verticalScrollBar().setValue(self.log_area.verticalScrollBar().maximum())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.start_simulation()
        elif event.key() == Qt.Key.Key_Space:
            self.stop_simulation()

    def start_simulation(self):
        if not self.is_running:
            self.is_running = True
            self.status_label.setText("Status: Running")
            self.log_activity("Simulation started")
            # Get URLs from input boxes
            self.urls = [input_box.text().strip() for input_box in self.url_inputs if input_box.text().strip()]
            if not self.urls:
                self.urls = self.default_urls
            # skewed toward longer intervals: 10s to 3min, weighted toward longer times
            min_time = 10000  # 10 seconds
            max_time = 180000  # 3 minutes
            # use exponential distribution to skew toward longer times
            random_time = int(min_time + (max_time - min_time) * (random.random() ** 0.3))
            self.timer.start(random_time)

    def stop_simulation(self):
        if self.is_running:
            self.is_running = False
            self.status_label.setText("Status: Stopped")
            self.log_activity("Simulation stopped")
            self.timer.stop()

    def perform_random_action(self):
        if not self.is_running:
            return
        actions = [
            self.open_random_url,
            self.switch_tab,
            self.simulate_scroll
        ]
        random.choice(actions)()
        # skewed toward longer intervals: 10s to 3min, weighted toward longer times
        min_time = 10000  # 10 seconds
        max_time = 180000  # 3 minutes
        # use exponential distribution to skew toward longer times
        random_time = int(min_time + (max_time - min_time) * (random.random() ** 0.3))
        self.timer.start(random_time)

    def open_random_url(self):
        if self.urls:
            url = random.choice(self.urls)
            webbrowser.open(url)
            self.log_activity(f"Opened URL: {url}")

    def switch_tab(self):
        pyautogui.hotkey('ctrl', 't') if sys.platform == 'darwin' else pyautogui.hotkey('ctrl', 'tab')
        self.log_activity("Switched tab")

    def simulate_scroll(self):
        scroll_amount = random.randint(-300, 300)
        pyautogui.scroll(scroll_amount)
        self.log_activity(f"Scrolled {scroll_amount}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Perpetuum()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec())