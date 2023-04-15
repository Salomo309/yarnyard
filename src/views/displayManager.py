from PyQt6 import QtWidgets
import sys

from views.windows.menuWindow import MenuWindow
from views.windows.artikelWindow import ArtikelWindow
from views.forms.jurnalForm import JurnalForm
from views.forms.todolistForm import TodolistForm

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
        self.jurnalForm = JurnalForm()
        self.todolistForm = TodolistForm()
        
        # Add the windows to the stacked widget
        self.stackedWidget.addWidget(self.menuWindow)           # 0
        self.stackedWidget.addWidget(self.artikelWindow)        # 1
        self.stackedWidget.addWidget(self.jurnalForm)           # 2
        self.stackedWidget.addWidget(self.todolistForm)           # 3
        
    def setUpListener(self):
        self.menuWindow.channel.connect(self.handleMenuWindow)
        self.artikelWindow.channel.connect(self.handleArtikelWindow)
        self.jurnalForm.channel.connect(self.handleJurnalForm)
        self.todolistForm.channel.connect(self.handleTodolistForm)
    
    def handleMenuWindow(self, page):
        if page == "artikel":
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(3)
    
    def handleArtikelWindow(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
        
    def handleJurnalForm(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
            
    def handleTodolistForm(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
