from PyQt6 import QtWidgets
import sys

# Windows
from views.windows.menuWindow import MenuWindow
from views.windows.artikelWindow import ArtikelWindow
from views.windows.detailTanamanWindow import DetailTanamanWindow
from views.windows.todolistWindow import TodolistWindow

# Forms
from views.forms.jurnalForm import JurnalForm
from views.forms.todolistForm import TodolistForm
from views.forms.tanamanForm import TanamanForm


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
        self.todolistWindow = TodolistWindow()
        self.detailTanamanWindows = {}

        self.jurnalForm = JurnalForm()
        self.todolistForm = TodolistForm()
        self.tanamanForm = TanamanForm()

        # Add the windows to the stacked widget
        self.stackedWidget.addWidget(self.menuWindow)           # 0
        self.stackedWidget.addWidget(self.artikelWindow)        # 1
        # self.stackedWidget.addWidget(self.detailTanamanWindow)
        self.stackedWidget.addWidget(self.todolistWindow)       # 2

        self.stackedWidget.addWidget(self.jurnalForm)           # 3
        self.stackedWidget.addWidget(self.todolistForm)         # 4
        self.stackedWidget.addWidget(self.tanamanForm)          # 5

    def setUpListener(self):
        self.menuWindow.channel.connect(self.handleMenuWindow)
        self.artikelWindow.channel.connect(self.handleArtikelWindow)
        # self.detailTanamanWindows.channel.connect(self.handleDetailTanamanWindow)
        self.todolistWindow.channel.connect(self.handleTodolistWindow)

        self.jurnalForm.channel.connect(self.handleJurnalForm)
        self.todolistForm.channel.connect(self.handleTodolistForm)
        self.tanamanForm.channel.connect(self.handleTanamanForm)

    def handleMenuWindow(self, page, idTanaman=None):
        if page == "artikel":
            self.stackedWidget.setCurrentIndex(1)
        elif page == "todolist":
            self.stackedWidget.setCurrentIndex(5)
        else:
            idTanaman = 1
            if idTanaman in self.detailTanamanWindows:
                self.stackedWidget.setCurrentIndex(
                    self.detailTanamanWindows[idTanaman])
            else:
                detailTanamanWindow = DetailTanamanWindow(idTanaman)
                self.detailTanamanWindows[idTanaman] = self.stackedWidget.addWidget(
                    detailTanamanWindow)
                self.stackedWidget.setCurrentIndex(
                    self.detailTanamanWindows[idTanaman])
                detailTanamanWindow.channel.connect(
                    self.handleDetailTanamanWindow)

    def handleArtikelWindow(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)

    def handleDetailTanamanWindow(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
    
    def handleTodolistWindow(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)

    def handleJurnalForm(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)

    def handleTodolistForm(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
            
    def handleTanamanForm(self, page):
        if page == "main":
            self.stackedWidget.setCurrentIndex(0)
