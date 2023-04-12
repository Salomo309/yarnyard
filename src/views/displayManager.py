from PyQt6 import QtWidgets
import sys

from views.menuWindow import MenuWindow
from views.artikelWindow import ArtikelWindow

class PageController:
    def __init__(self):
        super().__init__()
        self.setUpPages()
        self.setUpListener()
        self.stackedWidget.show()
        
    def setUpPages(self):
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.stackedWidget.resize(960, 600)
        
        self.menuWindow = MenuWindow()
        self.artikelWindow = ArtikelWindow()
        
        # Add the windows to the stacked widget
        self.stackedWidget.addWidget(self.menuWindow)           # 0
        self.stackedWidget.addWidget(self.artikelWindow)        # 1
        
    def setUpListener(self):
        self.menuWindow.channel.connect(self.handleMenuWindow)
        self.artikelWindow.channel.connect(self.handleArtikelWindow)
    
    def handleMenuWindow(self, page):
        if page == "artikel":
            # self.menuWindow.close()
            # self.artikelWindow.show()
            self.stackedWidget.setCurrentIndex(1)
            # self.artikelWindow.setUpArtikelWindow()
    
    def handleArtikelWindow(self):
        # self.artikelWindow.close()
        # self.menuWindow.show()
        self.stackedWidget.setCurrentIndex(0)