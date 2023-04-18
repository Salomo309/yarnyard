from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication, QIcon, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib

class TanamanForm(QMainWindow):
    channel = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setUpTanamanForm()

    def setUpTanamanForm(self):
        self.setWindowTitle("yanyard - Tanaman Form")
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
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
        icon.addPixmap(QtGui.QPixmap(path + "icons/left_arrow.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText(" Kembali")
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        
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
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main.setStyleSheet('''
                                #main {
                                    background-color: #F7F4D9;
                                }
                                ''')
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
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_title_form = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_form.setMinimumSize(QtCore.QSize(238, 68))
        self.label_title_form.setStyleSheet('''
                                            #label_title_form {
                                                color: #F7F4D9;
                                                background-color: #3C6255;
                                                padding: 15px 0px;
                                                border-radius: 25px;
                                                font-size: 24px;
                                                font-weight: 600;
                                            }
                                            ''')
        self.label_title_form.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title_form.setObjectName("label_title_form")
        self.label_title_form.setText("Form Tanaman")
        
        self.horizontalLayout_4.addWidget(self.label_title_form, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMinimumSize(QtCore.QSize(500, 340))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_contents_1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_3.setMaximumSize(QtCore.QSize(160, 200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_img = QtWidgets.QPushButton(parent=self.frame_3)
        self.widget_img.setMinimumSize(QtCore.QSize(160, 200))
        
        image = "assets/images/tanaman/add_photo.png"
        self.widget_img.setStyleSheet(f'''
                                        #widget_img {{
                                            border-image: url({image}) 0 0 0 0 stretch stretch;
                                            border-radius:40px;
                                        }}
                                        ''')
        
        self.widget_img.setObjectName("widget_img")
        self.widget_img.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.verticalLayout_4.addWidget(self.widget_img)
        self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_2.setMaximumSize(QtCore.QSize(370, 55))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nama_tanaman = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.nama_tanaman.setMinimumSize(QtCore.QSize(310, 45))
        self.nama_tanaman.setMaximumSize(QtCore.QSize(16777215, 45))
        self.nama_tanaman.setStyleSheet('''
                                        #nama_tanaman {
                                            padding: 7px 12px;
                                            border-radius: 20px;
                                            background: #61876E;
                                            color: #F7F3D7;
                                            font-size: 14px;
                                            font-weight: 600;
                                        }
                                        ''')
        self.nama_tanaman.setMaximumBlockCount(1)
        self.nama_tanaman.setObjectName("nama_tanaman")
        self.nama_tanaman.setPlaceholderText("Masukkan nama tanamanmu . . .")
        
        self.verticalLayout_5.addWidget(self.nama_tanaman, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deskripsi_jurnal = QtWidgets.QPlainTextEdit(parent=self.frame)
        self.deskripsi_jurnal.setMinimumSize(QtCore.QSize(310, 40))
        self.deskripsi_jurnal.setStyleSheet('''
                                            #deskripsi_jurnal {
                                                padding: 12px;
                                                font-size: 14px;
                                                border-radius: 15px;
                                                background: #61876E;
                                                color: #F7F3D7;
                                                font-weight: 600;
                                            }
                                            ''')
        self.deskripsi_jurnal.setOverwriteMode(True)
        self.deskripsi_jurnal.setObjectName("deskripsi_jurnal")
        self.deskripsi_jurnal.setPlaceholderText("Ceritakan tentang tanamanmu. . .")
        
        self.verticalLayout_6.addWidget(self.deskripsi_jurnal)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_contents_1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_submit = QtWidgets.QPushButton(parent=self.frame_description)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setMinimumSize(QtCore.QSize(130, 40))
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
        
        self.horizontalLayout_5.addWidget(self.btn_submit, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_description)
        self.verticalLayout.addWidget(self.main)
        self.setCentralWidget(self.centralwidget)

        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        self.widget_img.clicked.connect(self.on_img_clicked)

    def on_btn_back_clicked(self):
        self.changePageToMain()

    def changePageToMain(self):
        self.channel.emit("main")
        
    def on_img_clicked(self):
        # Open File Dialog
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.xpm *.jpg *.jpeg)')
        if file_path:
            image = file_path
            self.widget_img.setStyleSheet(f'''
                                            #widget_img {{
                                                border-image: url({image}) 0 0 0 0 stretch stretch;
                                                border-radius:40px;
                                            }}
                                            ''')
        
