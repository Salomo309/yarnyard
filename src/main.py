import sys
from PyQt6.QtWidgets import QApplication

from app import app
from views import displayManager

def initServer():
    # backend here
    app.run(debug=True)

if __name__ == '__main__':
    window = QApplication(sys.argv)
    view = displayManager.PageController()
    sys.exit(window.exec())