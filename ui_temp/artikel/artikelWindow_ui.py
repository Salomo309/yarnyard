# Form implementation generated from reading ui file 'd:\STEI\Jurusan\Semester-4\RPL\Tubes\if2250-2023-k01-g09-yanyard\ui_temp\artikel\artikelWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 602)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#header {\n"
"    background-color: #3C6255;\n"
"}\n"
"\n"
"#main {\n"
"    background-color: #F7F4D9;\n"
"}\n"
"\n"
"#footer {\n"
"    background-color: #F7F4D9;\n"
"}\n"
"\n"
"#btn_back {\n"
"    color: #F7F4D9;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#btn_back:hover {\n"
"    color: #DEDBC0;\n"
"}\n"
"\n"
"#btn_prev, #btn_next {\n"
"    background-color: #61876E;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"#btn_prev:hover {\n"
"    background-color: #486E55;\n"
"}\n"
"\n"
"#btn_next:hover {\n"
"    background-color: #486E55;\n"
"}\n"
"\n"
"#label_title_artikel {\n"
"    color: #F7F4D9;\n"
"    background-color: #3C6255;\n"
"    padding: 15px 70px;\n"
"    border-radius: 25px;\n"
"    font-size: 28px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#box_description_artikel {\n"
"    color: #F9F9F9;\n"
"    background-color: #3C6255;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#text_description_artikel {\n"
"    color: #F9F9F9;\n"
"    padding: 10px 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#text_title_artikel {\n"
"    font-size: 18px;\n"
"    color: #F9F9F9;\n"
"    font-weight: 600;\n"
"    margin: 0 8px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
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
        self.logo.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\artikel\\logo_circle.png"))
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
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_title_artikel = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_artikel.setObjectName("label_title_artikel")
        self.horizontalLayout_4.addWidget(self.label_title_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_contents_1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_prev = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_prev.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_prev.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_prev.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_prev.setObjectName("frame_prev")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_prev)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_prev = QtWidgets.QWidget(parent=self.frame_prev)
        self.btn_prev.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_prev.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_prev.setObjectName("btn_prev")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.btn_prev)
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_prev_inside = QtWidgets.QPushButton(parent=self.btn_prev)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev_inside.sizePolicy().hasHeightForWidth())
        self.btn_prev_inside.setSizePolicy(sizePolicy)
        self.btn_prev_inside.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/left__arrow.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_prev_inside.setIcon(icon1)
        self.btn_prev_inside.setIconSize(QtCore.QSize(24, 24))
        self.btn_prev_inside.setObjectName("btn_prev_inside")
        self.verticalLayout_3.addWidget(self.btn_prev_inside, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_6.addWidget(self.btn_prev)
        self.horizontalLayout_5.addWidget(self.frame_prev, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.frame_img = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_img.setMaximumSize(QtCore.QSize(400, 170))
        self.frame_img.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_img.setObjectName("frame_img")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.frame_img)
        self.hboxlayout.setObjectName("hboxlayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_img)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.hboxlayout.addWidget(self.stackedWidget)
        self.horizontalLayout_5.addWidget(self.frame_img)
        self.frame_next = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_next.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_next.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_next.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_next.setObjectName("frame_next")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_next)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_next = QtWidgets.QWidget(parent=self.frame_next)
        self.btn_next.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_next.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.btn_next)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_next_inside = QtWidgets.QPushButton(parent=self.btn_next)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_inside.sizePolicy().hasHeightForWidth())
        self.btn_next_inside.setSizePolicy(sizePolicy)
        self.btn_next_inside.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/right_arrow.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_next_inside.setIcon(icon2)
        self.btn_next_inside.setIconSize(QtCore.QSize(24, 24))
        self.btn_next_inside.setObjectName("btn_next_inside")
        self.horizontalLayout_10.addWidget(self.btn_next_inside, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_7.addWidget(self.btn_next)
        self.horizontalLayout_5.addWidget(self.frame_next, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_contents_1)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.box_description_artikel = QtWidgets.QWidget(parent=self.frame_description)
        self.box_description_artikel.setMaximumSize(QtCore.QSize(600, 220))
        self.box_description_artikel.setObjectName("box_description_artikel")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.box_description_artikel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_title_artikel = QtWidgets.QPlainTextEdit(parent=self.box_description_artikel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_title_artikel.sizePolicy().hasHeightForWidth())
        self.text_title_artikel.setSizePolicy(sizePolicy)
        self.text_title_artikel.setMaximumSize(QtCore.QSize(16777215, 35))
        self.text_title_artikel.setReadOnly(True)
        self.text_title_artikel.setCenterOnScroll(False)
        self.text_title_artikel.setObjectName("text_title_artikel")
        self.verticalLayout_4.addWidget(self.text_title_artikel)
        self.text_description_artikel = QtWidgets.QPlainTextEdit(parent=self.box_description_artikel)
        self.text_description_artikel.setReadOnly(True)
        self.text_description_artikel.setObjectName("text_description_artikel")
        self.verticalLayout_4.addWidget(self.text_description_artikel)
        self.horizontalLayout_8.addWidget(self.box_description_artikel)
        self.verticalLayout_2.addWidget(self.frame_description)
        self.verticalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", " Kembali"))
        self.label_title_artikel.setText(_translate("MainWindow", "Artikel"))
        self.text_title_artikel.setPlainText(_translate("MainWindow", "Cara Menanam Tanaman"))
        self.text_description_artikel.setPlainText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at nibh volutpat, eleifend augue vel, hendrerit augue. Fusce egestas ipsum dolor, id convallis nulla cursus eleifend. Aliquam erat volutpat. Suspendisse facilisis quis ex non vestibulum. In ultricies porta dapibus. Praesent in arcu vel risus auctor elementum id at ex. Vestibulum gravida, odio ac dapibus convallis, erat lacus molestie turpis, in tristique urna mauris vitae ligula."))
