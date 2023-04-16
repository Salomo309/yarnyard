# Form implementation generated from reading ui file 'd:\STEI\Jurusan\Semester-4\RPL\Tubes\if2250-2023-k01-g09-yanyard\ui_temp\form\jurnalForm2.ui'
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
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet("#header {\n"
"    background-color: #3C6255;\n"
"}")
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
        self.logo.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\form\\../artikel/logo_circle.png"))
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
        self.body = QtWidgets.QWidget(parent=self.centralwidget)
        self.body.setStyleSheet("#body {\n"
"    background-color: #F7F4D9;\n"
"}")
        self.body.setObjectName("body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content = QtWidgets.QFrame(parent=self.body)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.submit = QtWidgets.QFrame(parent=self.content)
        self.submit.setGeometry(QtCore.QRect(0, 410, 960, 90))
        self.submit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.submit.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.submit.setObjectName("submit")
        self.btn_submit = QtWidgets.QPushButton(parent=self.submit)
        self.btn_submit.setGeometry(QtCore.QRect(415, 25, 130, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setStyleSheet("#btn_submit {\n"
"    border-radius: 20px;\n"
"    background: #3C6255;\n"
"    color: #F7F3D7;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#btn_submit:hover {\n"
"    background-color: #23493C;\n"
"}")
        self.btn_submit.setDefault(False)
        self.btn_submit.setFlat(False)
        self.btn_submit.setObjectName("btn_submit")
        self.frame_2 = QtWidgets.QFrame(parent=self.content)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 960, 410))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.deskripsi_jurnal = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.deskripsi_jurnal.setGeometry(QtCore.QRect(150, 110, 660, 300))
        self.deskripsi_jurnal.setStyleSheet("#deskripsi_jurnal {\n"
"    padding: 17px 17px;\n"
"    font-size: 14px;\n"
"    border-radius: 15px;\n"
"    background: #61876E;\n"
"    color: #F7F3D7;\n"
"    height: 40px;\n"
"    font-weight: 600;\n"
"    width: 243px;\n"
"}")
        self.deskripsi_jurnal.setOverwriteMode(True)
        self.deskripsi_jurnal.setObjectName("deskripsi_jurnal")
        self.label_title = QtWidgets.QLabel(parent=self.frame_2)
        self.label_title.setGeometry(QtCore.QRect(361, 25, 238, 60))
        self.label_title.setStyleSheet("#label_title {\n"
"    color: #F7F4D9;\n"
"    background-color: #3C6255;\n"
"    border-radius: 20px;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.content)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", " Kembali"))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.deskripsi_jurnal.setPlainText(_translate("MainWindow", "Tulis deskripsi jurnal . . ."))
        self.label_title.setText(_translate("MainWindow", "Form Jurnal"))
