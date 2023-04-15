from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication, QIcon, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib

class JurnalForm(QMainWindow):
    channel = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setUpJurnalForm()
    
    def setUpJurnalForm(self):
        self.setWindowTitle("yanyard - Jurnal Form")
        self.resize(960, 600)
        # self.setFixedSize(960, 600)
        
        # Get the size and position of the user's screen
        primary_screen = QGuiApplication.primaryScreen()
        screen = primary_screen.availableGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Center the window on the screen
        self.move(int((screen_width - self.width()) / 2),
                    int((screen_height - self.height()) / 2))
        
        # Assets path
        path = str(pathlib.Path(__file__).parent.absolute()) + '/../../../assets/'
        
        # Logo
        self.setWindowIcon(QIcon(path + 'logo/logo.ico'))
        
        # Fonts
        fonts_folder_path = path + 'fonts/'
        for filename in os.listdir(fonts_folder_path):
            if filename.endswith('.ttf') or filename.endswith('.otf'):
                font_path = os.path.join(fonts_folder_path, filename)
                QFontDatabase.addApplicationFont(font_path)
        
        self.initializeWidgets(path)
        
    def initializeWidgets(self, path):
        self.setStyleSheet('''
                           *{
                                border: none;
                                background-color: transparent;
                                background: transparent;
                                padding: 0;
                                margin: 0;
                                font-family: Poppins;
                            }
                           ''')
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet('''
                                  #header {
                                      background-color: #3C6255;
                                  }
                                  ''')
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
        self.btn_back.setStyleSheet('''
                                    #btn_back {
                                        color: #F7F4D9;
                                        font-size: 20px;
                                        font-weight: 600;
                                    }
                                    
                                    #btn_back:hover {
                                        color: #DEDBC0;
                                    }
                                    ''')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path + "icons/left_arrow.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText(" Kembali")
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_3.addWidget(
            self.btn_back, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
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
        self.logo.setPixmap(QtGui.QPixmap(path + "logo/logo_circle.png"))
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
        self.body.setStyleSheet('''
                                #body {
                                    background-color: #F7F4D9;
                                }
                                ''')
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setStyleSheet('''
                                      #btn_submit {
                                          border-radius: 20px;
                                          background: #3C6255;
                                          color: #F7F3D7;
                                          font-size: 16px;
                                          font-weight: 600;
                                      }
                                      
                                      #btn_submit:hover {
                                          background-color: #23493C;
                                      }
                                      ''')
        self.btn_submit.setDefault(False)
        self.btn_submit.setFlat(False)
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.setText("Submit")
        self.btn_submit.setCursor(Qt.CursorShape.PointingHandCursor)

        self.frame_2 = QtWidgets.QFrame(parent=self.content)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 960, 410))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.deskripsi_jurnal = QtWidgets.QTextEdit(parent=self.frame_2)
        self.deskripsi_jurnal.setGeometry(QtCore.QRect(150, 110, 660, 300))
        self.deskripsi_jurnal.setStyleSheet('''
                                            #deskripsi_jurnal {
                                                padding: 17px 17px;
                                                font-size: 14px;
                                                border-radius: 15px;
                                                background: #61876E;
                                                color: #F7F3D7;
                                                height: 40px;
                                                font-weight: 600;
                                                width: 243px;
                                            }
                                            ''')
        self.deskripsi_jurnal.setOverwriteMode(True)
        self.deskripsi_jurnal.setObjectName("deskripsi_jurnal")
        self.deskripsi_jurnal.setPlaceholderText(
            "Tulis deskripsi jurnal . . .")
        self.deskripsi_jurnal.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.label_title = QtWidgets.QLabel(parent=self.frame_2)
        self.label_title.setGeometry(QtCore.QRect(361, 25, 238, 60))
        self.label_title.setStyleSheet('''
                                       #label_title {
                                           color: #F7F4D9;
                                           background-color: #3C6255;
                                           border-radius: 20px;
                                           font-size: 20px;
                                           font-weight: 600;
                                       }
                                       ''')
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_title.setText("Form Jurnal")

        self.verticalLayout_2.addWidget(self.content)
        self.verticalLayout.addWidget(self.body)
        self.setCentralWidget(self.centralwidget)

        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        
    def on_btn_back_clicked(self):
        self.changePageToMain()

    def changePageToMain(self):
        self.channel.emit("main")