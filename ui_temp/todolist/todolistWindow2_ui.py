# Form implementation generated from reading ui file 'd:\STEI\Jurusan\Semester-4\RPL\Tubes\if2250-2023-k01-g09-yanyard\ui_temp\todolist\todolistWindow2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setStyleSheet("#header {\n"
"    background-color: #3C6255;\n"
"}")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_temp = QtWidgets.QFrame(parent=self.header)
        self.frame_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp.setObjectName("frame_temp")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_temp)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_back = QtWidgets.QPushButton(parent=self.frame_temp)
        self.btn_back.setStyleSheet("#btn_back {\n"
"    color: #F7F4D9;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#btn_back:hover {\n"
"    color: #DEDBC0;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/left__arrow2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_temp)
        self.frame_logo = QtWidgets.QFrame(parent=self.header)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(parent=self.frame_logo)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(42, 42))
        self.logo.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\todolist\\../artikel/logo_circle.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.frame_temp_2 = QtWidgets.QFrame(parent=self.header)
        self.frame_temp_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp_2.setObjectName("frame_temp_2")
        self.horizontalLayout.addWidget(self.frame_temp_2)
        self.verticalLayout.addWidget(self.header)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setStyleSheet("#scrollArea {\n"
"    background-color: #F7F4D9;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    width: 20px;\n"
"    margin: 5px;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: #3C6255;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: #23493C;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet("#main {\n"
"    background-color: #F7F4D9;\n"
"}")
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 36)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_title_tdl = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_tdl.setMaximumSize(QtCore.QSize(238, 16777215))
        self.label_title_tdl.setStyleSheet("#label_title_tdl {\n"
"    color: #F7F4D9;\n"
"    background-color: #3C6255;\n"
"    padding: 15px 50px;\n"
"    border-radius: 25px;\n"
"    font-size: 28px;\n"
"    font-weight: 600;\n"
"}")
        self.label_title_tdl.setObjectName("label_title_tdl")
        self.horizontalLayout_5.addWidget(self.label_title_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_title)
        self.frame_tdl = QtWidgets.QFrame(parent=self.main)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_tdls = QtWidgets.QFrame(parent=self.frame_tdl)
        self.frame_tdls.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdls.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdls.setObjectName("frame_tdls")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_tdls)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_tanggal = QtWidgets.QFrame(parent=self.frame_tdls)
        self.frame_tanggal.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_tanggal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tanggal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tanggal.setObjectName("frame_tanggal")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_tanggal)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_tdl = QtWidgets.QLabel(parent=self.frame_tanggal)
        self.icon_tdl.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_tdl.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\todolist\\../../assets/icons/event_note_green.svg"))
        self.icon_tdl.setScaledContents(True)
        self.icon_tdl.setObjectName("icon_tdl")
        self.horizontalLayout_4.addWidget(self.icon_tdl)
        self.label_tdl = QtWidgets.QLabel(parent=self.frame_tanggal)
        self.label_tdl.setStyleSheet("#label_tdl {\n"
"    color: #3C6255;\n"
"    font-size: 24px;\n"
"    font-weight: 600;\n"
"}")
        self.label_tdl.setObjectName("label_tdl")
        self.horizontalLayout_4.addWidget(self.label_tdl)
        self.verticalLayout_6.addWidget(self.frame_tanggal)
        self.frame_list_tdl = QtWidgets.QFrame(parent=self.frame_tdls)
        self.frame_list_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_tdl.setObjectName("frame_list_tdl")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_list_tdl)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_tdl_1 = QtWidgets.QFrame(parent=self.frame_list_tdl)
        self.frame_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl_1.setObjectName("frame_tdl_1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_tdl_1)
        self.horizontalLayout_7.setContentsMargins(0, 9, 10, 9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_time_tdl_1 = QtWidgets.QFrame(parent=self.frame_tdl_1)
        self.frame_time_tdl_1.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_time_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_time_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_time_tdl_1.setObjectName("frame_time_tdl_1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_time_tdl_1)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_time_tdl_1 = QtWidgets.QLabel(parent=self.frame_time_tdl_1)
        self.label_time_tdl_1.setMinimumSize(QtCore.QSize(100, 0))
        self.label_time_tdl_1.setStyleSheet("#label_time_tdl_1 {\n"
"    color: #F7F4D9;\n"
"    background-color: #61876E;\n"
"\n"
"    border-radius: 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}")
        self.label_time_tdl_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time_tdl_1.setObjectName("label_time_tdl_1")
        self.verticalLayout_11.addWidget(self.label_time_tdl_1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.frame_time_tdl_1)
        self.frame_desc_tdl = QtWidgets.QFrame(parent=self.frame_tdl_1)
        self.frame_desc_tdl.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_desc_tdl.setStyleSheet("#frame_desc_tdl {\n"
"    color: #F7F4D9;\n"
"    background-color: #61876E;\n"
"    padding: 0px 20px;\n"
"    border-radius: 16px;\n"
"}")
        self.frame_desc_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_desc_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_desc_tdl.setObjectName("frame_desc_tdl")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_desc_tdl)
        self.horizontalLayout_8.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_desc_tdl_1 = QtWidgets.QLabel(parent=self.frame_desc_tdl)
        self.label_desc_tdl_1.setStyleSheet("#label_desc_tdl_1 {\n"
"    color: #F7F4D9;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}")
        self.label_desc_tdl_1.setObjectName("label_desc_tdl_1")
        self.horizontalLayout_8.addWidget(self.label_desc_tdl_1, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.btn_more_1 = QtWidgets.QPushButton(parent=self.frame_desc_tdl)
        self.btn_more_1.setStyleSheet("")
        self.btn_more_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/test/more_vert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_more_1.setIcon(icon1)
        self.btn_more_1.setIconSize(QtCore.QSize(20, 20))
        self.btn_more_1.setObjectName("btn_more_1")
        self.horizontalLayout_8.addWidget(self.btn_more_1, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_7.addWidget(self.frame_desc_tdl)
        self.verticalLayout_10.addWidget(self.frame_tdl_1)
        self.verticalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_6.addWidget(self.frame_list_tdl)
        self.verticalLayout_4.addWidget(self.frame_tdls)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.frame_tdl)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.main)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", " Kembali"))
        self.label_title_tdl.setText(_translate("MainWindow", "To Do List"))
        self.label_tdl.setText(_translate("MainWindow", "19 April 2023"))
        self.label_time_tdl_1.setText(_translate("MainWindow", "07.00"))
        self.label_desc_tdl_1.setText(_translate("MainWindow", "Siram tanaman sebelum berangkat kuliah"))
