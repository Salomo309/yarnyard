import PyQt6
from PyQt6.QtWidgets import QApplication
import sys

from views.menuWindow import MenuWindow

class PageController:
    def __init__(self):
        super().__init__()
        self.menuWindow = MenuWindow()
        self.menuWindow.show()