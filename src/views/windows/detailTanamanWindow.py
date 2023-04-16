from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication, QIcon, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json

class DetailTanamanWindow(QMainWindow):
    channel = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setUpDetailTanamanWindow()

    def setUpDetailTanamanWindow(self):
        self.setWindowTitle("yanyard - Detail Tanaman")
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

        # self.setArtikel()
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
        
        # Layouts
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Header
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setStyleSheet('''
                                    #header {
                                        background-color: #3C6255;
                                    }
                                    ''')
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
        
        # Scroll area
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setStyleSheet('''
                                        #scrollArea {
                                            background-color: #F7F4D9;
                                        }
                                        
                                        QScrollBar:vertical {
                                            border: none;
                                            width: 20px;
                                            margin: 5px;
                                            border-radius: 0px;
                                         }
                                        
                                        /*  HANDLE BAR VERTICAL */
                                        QScrollBar::handle:vertical {    
                                            background-color: #3C6255;
                                            min-height: 20px;
                                            border-radius: 5px;
                                        }
                                        
                                        QScrollBar::handle:vertical:hover{    
                                            background-color: #23493C;
                                        }
                                        
                                        /* BTN TOP - SCROLLBAR */
                                        QScrollBar::sub-line:vertical {
                                            height: 0px;
                                        }
                                        
                                        /* BTN BOTTOM - SCROLLBAR */
                                        QScrollBar::add-line:vertical {
                                            height: 0px;
                                        }
                                        
                                        /* RESET ARROW */
                                        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                            background: none;
                                        }
                                        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                            background: none;
                                        }
                                        ''')
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -243, 940, 801))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Main
        self.main = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet('''
                                #main {
                                    background-color: #F7F4D9;
                                }
                                ''')
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(38, 0, 18, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_tanaman = QtWidgets.QFrame(parent=self.main)
        self.frame_tanaman.setMinimumSize(QtCore.QSize(0, 380))
        self.frame_tanaman.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tanaman.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tanaman.setObjectName("frame_tanaman")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tanaman)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_img = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_img.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_img.setObjectName("frame_img")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_img)
        self.verticalLayout_6.setContentsMargins(0, 18, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        # Image Tanaman
        self.widget_img = QtWidgets.QWidget(parent=self.frame_img)
        self.widget_img.setMinimumSize(QtCore.QSize(160, 200))
        self.widget_img.setMaximumSize(QtCore.QSize(130, 200))
        self.widget_img.setStyleSheet('''
                                        #widget_img {
                                            border-radius:30px;
                                            background-color: #3C6255;
                                        }
                                        ''')
        self.widget_img.setObjectName("widget_img")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_img)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6.addWidget(self.widget_img)
        self.verticalLayout_4.addWidget(self.frame_img, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_name = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_name.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_name.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_name.setObjectName("frame_name")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_name)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        # Name Tanaman
        self.label_name = QtWidgets.QLabel(parent=self.frame_name)
        self.label_name.setStyleSheet('''
                                        #label_name {
                                            color: #3C6255;
                                            font-size: 28px;
                                            font-weight: 800;
                                        }
                                        ''')
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_5.addWidget(self.label_name, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_name)
        self.frame_text = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_text.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_text.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_text.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_text.setObjectName("frame_text")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_text)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        # Description Tanaman
        self.text_desc_tanaman = QtWidgets.QPlainTextEdit(parent=self.frame_text)
        self.text_desc_tanaman.setStyleSheet('''
                                            #text_desc_tanaman {
                                                color: #0F0F0F;
                                                font-size: 14px;
                                            }
                                            ''')
        self.text_desc_tanaman.setReadOnly(True)
        self.text_desc_tanaman.setObjectName("text_desc_tanaman")
        self.horizontalLayout_6.addWidget(self.text_desc_tanaman)
        self.verticalLayout_4.addWidget(self.frame_text)
        self.verticalLayout_3.addWidget(self.frame_tanaman)
        
        # TO DO LIST
        self.frame_tdl = QtWidgets.QFrame(parent=self.main)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        # Head TDL
        self.frame_head_tdl = QtWidgets.QFrame(parent=self.frame_tdl)
        self.frame_head_tdl.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_head_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl.setObjectName("frame_head_tdl")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_head_tdl)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_head_tdl_1 = QtWidgets.QFrame(parent=self.frame_head_tdl)
        self.frame_head_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl_1.setObjectName("frame_head_tdl_1")
        self.icon_tdl = QtWidgets.QLabel(parent=self.frame_head_tdl_1)
        self.icon_tdl.setGeometry(QtCore.QRect(0, 15, 30, 30))
        self.icon_tdl.setPixmap(QtGui.QPixmap(path + "icons/format_list_bulleted.svg"))
        self.icon_tdl.setScaledContents(True)
        self.icon_tdl.setObjectName("icon_tdl")
        self.label_tdl = QtWidgets.QLabel(parent=self.frame_head_tdl_1)
        self.label_tdl.setGeometry(QtCore.QRect(40, 15, 120, 30))
        self.label_tdl.setStyleSheet('''
                                    #label_tdl {
                                        color: #3C6255;
                                        font-size: 24px;
                                        font-weight: 600;
                                    }
                                    ''')
        self.label_tdl.setObjectName("label_tdl")
        self.label_tdl.setText("To Do List")
        
        self.horizontalLayout_4.addWidget(self.frame_head_tdl_1)
        self.frame_head_tdl_2 = QtWidgets.QFrame(parent=self.frame_head_tdl)
        self.frame_head_tdl_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl_2.setObjectName("frame_head_tdl_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_head_tdl_2)
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_add_tdl = QtWidgets.QPushButton(parent=self.frame_head_tdl_2)
        self.btn_add_tdl.setMinimumSize(QtCore.QSize(170, 0))
        self.btn_add_tdl.setStyleSheet('''
                                        #btn_add_tdl{
                                            color: #F7F4D9;
                                            background-color: #61876E;
                                            padding: 15px;
                                            border-radius: 20px;
                                            font-size: 14px;
                                            font-weight: 800;
                                        }
                                        ''')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path + "icons/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_add_tdl.setIcon(icon1)
        self.btn_add_tdl.setIconSize(QtCore.QSize(20, 20))
        self.btn_add_tdl.setObjectName("btn_add_tdl")
        self.btn_add_tdl.setText("ADD TO DO LIST")
        
        self.verticalLayout_8.addWidget(self.btn_add_tdl, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_4.addWidget(self.frame_head_tdl_2)
        self.verticalLayout_7.addWidget(self.frame_head_tdl)
        
        # List TDL
        self.frame_list_tdl = QtWidgets.QFrame(parent=self.frame_tdl)
        self.frame_list_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_tdl.setObjectName("frame_list_tdl")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_list_tdl)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        
        # Dynamic TDL
        for i in range(3):
            # Frame
            self.frame_tdl_temp = QtWidgets.QFrame(parent=self.frame_list_tdl)
            self.frame_tdl_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_tdl_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_tdl_temp.setObjectName(f"frame_tdl_temp_{i}")
            
            # Layout for frame
            self.horizontal_layout_temp = QtWidgets.QHBoxLayout(self.frame_tdl_temp)
            self.horizontal_layout_temp.setContentsMargins(0, 9, 0, 9)
            self.horizontal_layout_temp.setObjectName(f"horizontal_layout_temp_{i}")
            
            # Time frame
            self.frame_time_tdl = QtWidgets.QFrame(parent=self.frame_tdl_temp)
            self.frame_time_tdl.setMaximumSize(QtCore.QSize(120, 16777215))
            self.frame_time_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_time_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_time_tdl.setObjectName(f"frame_time_tdl_{i}")
            
            # Vert layout
            self.vertical_layout_time = QtWidgets.QVBoxLayout(self.frame_time_tdl)
            self.vertical_layout_time.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_time.setSpacing(0)
            self.vertical_layout_time.setObjectName(f"vertical_layout_time_{i}")
            
            # Label time
            self.label_time = QtWidgets.QLabel(parent=self.frame_time_tdl)
            self.label_time.setMinimumSize(QtCore.QSize(0, 35))
            self.label_time.setStyleSheet(f'''
                                            #label_time_{i} {{
                                                color: #F7F4D9;
                                                background-color: #61876E;
                                                padding: 8px 40px;
                                                border-radius: 16px;
                                                font-size: 14px;
                                                font-weight: 600;
                                            }}
                                            ''')
            self.label_time.setText("07.00")
            self.label_time.setObjectName(f"label_time_{i}")
        
            self.vertical_layout_time.addWidget(self.label_time, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
    
            # Add time frame to horizontal layout
            self.horizontal_layout_temp.addWidget(self.frame_time_tdl)
            
            # Desc frame
            self.frame_desc = QtWidgets.QFrame(parent=self.frame_tdl_temp)
            self.frame_desc.setMaximumSize(QtCore.QSize(16777215, 35))
            self.frame_desc.setStyleSheet(f'''
                                     #frame_desc_{i} {{
                                        color: #F7F4D9;
                                        background-color: #61876E;
                                        padding: 0px 20px;
                                        border-radius: 16px;
                                    }}
                                    ''')
            self.frame_desc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_desc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_desc.setObjectName(f"frame_desc_{i}")
            
            # Horizontal layout
            self.horizontal_layout_desc = QtWidgets.QHBoxLayout(self.frame_desc)
            self.horizontal_layout_desc.setContentsMargins(0, 9, 0, 9)
            self.horizontal_layout_desc.setObjectName(f"horizontal_layout_desc_{i}")
            
            # Label
            self.label_desc_tdl = QtWidgets.QLabel(parent=self.frame_desc)
            self.label_desc_tdl.setStyleSheet(f'''
                                                #label_desc_tdl_{i} {{
                                                    color: #F7F4D9;
                                                    font-size: 14px;
                                                    font-weight: 600;
                                                }}
                                                ''')
            self.label_desc_tdl.setText("Siram tanaman sebelum berangkat kuliah")
            self.label_desc_tdl.setObjectName(f"label_desc_tdl_{i}")
            self.horizontal_layout_desc.addWidget(self.label_desc_tdl, 0, QtCore.Qt.AlignmentFlag.AlignLeft) #
            
            self.btn_more_1 = QtWidgets.QPushButton(parent=self.frame_desc)
            self.btn_more_1.setStyleSheet("")
            self.btn_more_1.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/test/more_vert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_more_1.setIcon(icon2)
            self.btn_more_1.setIconSize(QtCore.QSize(20, 20))
            self.btn_more_1.setObjectName(f"btn_more_1_{i}")
            
            self.horizontal_layout_desc.addWidget(self.btn_more_1, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.horizontal_layout_temp.addWidget(self.frame_desc)
            self.verticalLayout_10.addWidget(self.frame_tdl_temp)
                    
        # Spacer
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addWidget(self.frame_list_tdl)
        self.verticalLayout_3.addWidget(self.frame_tdl)
        
        # Jurnal
        self.frame_jurnal = QtWidgets.QFrame(parent=self.main)
        self.frame_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_jurnal.setObjectName("frame_jurnal")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_jurnal)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 36)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_head_jurnal = QtWidgets.QFrame(parent=self.frame_jurnal)
        self.frame_head_jurnal.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_head_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal.setObjectName("frame_head_jurnal")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_head_jurnal)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_head_jurnal_1 = QtWidgets.QFrame(parent=self.frame_head_jurnal)
        self.frame_head_jurnal_1.setStyleSheet("")
        self.frame_head_jurnal_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal_1.setObjectName("frame_head_jurnal_1")
        self.icon_jurnal = QtWidgets.QLabel(parent=self.frame_head_jurnal_1)
        self.icon_jurnal.setGeometry(QtCore.QRect(0, 15, 30, 30))
        self.icon_jurnal.setPixmap(QtGui.QPixmap(":/test/article.svg"))
        self.icon_jurnal.setScaledContents(True)
        self.icon_jurnal.setObjectName("icon_jurnal")
        self.label_jurnal = QtWidgets.QLabel(parent=self.frame_head_jurnal_1)
        self.label_jurnal.setGeometry(QtCore.QRect(40, 15, 200, 30))
        self.label_jurnal.setStyleSheet('''
                                        #label_jurnal {
                                            color: #3C6255;
                                            font-size: 24px;
                                            font-weight: 600;
                                        }
                                        ''')
        self.label_jurnal.setObjectName("label_jurnal")
        self.horizontalLayout_9.addWidget(self.frame_head_jurnal_1)
        self.frame_head_jurnal_2 = QtWidgets.QFrame(parent=self.frame_head_jurnal)
        self.frame_head_jurnal_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal_2.setObjectName("frame_head_jurnal_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_head_jurnal_2)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_add_jurnal = QtWidgets.QPushButton(parent=self.frame_head_jurnal_2)
        self.btn_add_jurnal.setMinimumSize(QtCore.QSize(170, 0))
        self.btn_add_jurnal.setStyleSheet('''
                                        #btn_add_jurnal {
                                            color: #F7F4D9;
                                            background-color: #61876E;
                                            padding: 15px;
                                            border-radius: 20px;
                                            font-size: 14px;
                                            font-weight: 800;
                                        }
                                        ''')
        self.btn_add_jurnal.setIcon(icon1)
        self.btn_add_jurnal.setIconSize(QtCore.QSize(20, 20))
        self.btn_add_jurnal.setObjectName("btn_add_jurnal")
        self.horizontalLayout_10.addWidget(self.btn_add_jurnal, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_9.addWidget(self.frame_head_jurnal_2)
        self.verticalLayout_12.addWidget(self.frame_head_jurnal)
        self.frame_list_jurnal = QtWidgets.QFrame(parent=self.frame_jurnal)
        self.frame_list_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_jurnal.setObjectName("frame_list_jurnal")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_list_jurnal)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_jurnal_1 = QtWidgets.QFrame(parent=self.frame_list_jurnal)
        self.frame_jurnal_1.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frame_jurnal_1.setStyleSheet('''
                                            #frame_jurnal_1 {
                                                color: #F7F4D9;
                                                background-color: #3C6255;
                                                border-radius: 30px;
                                            }
                                            ''')
        self.frame_jurnal_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_jurnal_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_jurnal_1.setObjectName("frame_jurnal_1")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_jurnal_1)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_jurnal_top = QtWidgets.QFrame(parent=self.frame_jurnal_1)
        self.frame_jurnal_top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_jurnal_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_jurnal_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_jurnal_top.setObjectName("frame_jurnal_top")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_jurnal_top)
        self.horizontalLayout_11.setContentsMargins(27, 18, 9, 9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_left = QtWidgets.QFrame(parent=self.frame_jurnal_top)
        self.frame_left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left.setObjectName("frame_left")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_left)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_time_jurnal_1 = QtWidgets.QLabel(parent=self.frame_left)
        self.label_time_jurnal_1.setStyleSheet('''
                                                #label_time_jurnal_1 {
                                                    color: #F7F4D9;
                                                    font-size: 20px;
                                                    font-weight: 600;
                                                }
                                                ''')
        self.label_time_jurnal_1.setObjectName("label_time_jurnal_1")
        self.horizontalLayout_12.addWidget(self.label_time_jurnal_1)
        self.horizontalLayout_11.addWidget(self.frame_left)
        self.frame_right = QtWidgets.QFrame(parent=self.frame_jurnal_top)
        self.frame_right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_right.setObjectName("frame_right")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_right)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.btn_more_2 = QtWidgets.QPushButton(parent=self.frame_right)
        self.btn_more_2.setStyleSheet("")
        self.btn_more_2.setText("")
        self.btn_more_2.setIcon(icon2)
        self.btn_more_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_more_2.setObjectName("btn_more_2")
        self.verticalLayout_16.addWidget(self.btn_more_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_11.addWidget(self.frame_right)
        self.verticalLayout_15.addWidget(self.frame_jurnal_top)
        self.frame_jurnal_bot = QtWidgets.QFrame(parent=self.frame_jurnal_1)
        self.frame_jurnal_bot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_jurnal_bot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_jurnal_bot.setObjectName("frame_jurnal_bot")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_jurnal_bot)
        self.horizontalLayout_13.setContentsMargins(27, 0, 27, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.text_desc_jurnal_1 = QtWidgets.QPlainTextEdit(parent=self.frame_jurnal_bot)
        self.text_desc_jurnal_1.setStyleSheet('''
                                                #text_desc_jurnal_1 {
                                                    color: #F7F4D9;
                                                    font-size: 14px;
                                                }
                                                ''')
        self.text_desc_jurnal_1.setObjectName("text_desc_jurnal_1")
        self.horizontalLayout_13.addWidget(self.text_desc_jurnal_1)
        self.verticalLayout_15.addWidget(self.frame_jurnal_bot)
        self.verticalLayout_13.addWidget(self.frame_jurnal_1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addWidget(self.frame_list_jurnal)
        self.verticalLayout_3.addWidget(self.frame_jurnal)
        self.verticalLayout_2.addWidget(self.main)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", " Kembali"))
        self.label_name.setText(_translate("MainWindow", "Strobeyi"))
        self.text_desc_tanaman.setPlainText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at nibh volutpat, eleifend augue vel, hendrerit augue. Fusce egestas ipsum dolor, id convallis nulla cursus eleifend. Aliquam erat volutpat. Suspendisse facilisis quis ex non vestibulum. In ultricies porta dapibus. Praesent in arcu vel risus auctor elementum id at ex."))
        # self.label_tdl.setText(_translate("MainWindow", "To Do List"))
        # self.btn_add_tdl.setText(_translate("MainWindow", "ADD TO DO LIST"))
        # self.label_time_tdl_1.setText(_translate("MainWindow", "07.00"))
        # self.label_desc_tdl_1.setText(_translate("MainWindow", "Siram tanaman sebelum berangkat kuliah"))
        self.label_jurnal.setText(_translate("MainWindow", "Jurnal Tanaman"))
        self.btn_add_jurnal.setText(_translate("MainWindow", "ADD JURNAL"))
        self.label_time_jurnal_1.setText(_translate("MainWindow", "19 April 2023"))
        self.text_desc_jurnal_1.setPlainText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at nibh volutpat, eleifend augue vel, hendrerit augue. Fusce egestas ipsum dolor, id convallis nulla cursus eleifend. Aliquam erat volutpat. Suspendisse facilisis quis ex non vestibulum. In ultricies porta dapibus. Praesent in arcu vel risus auctor elementum id at ex. Vestibulum gravida, odio ac dapibus convallis, erat lacus molestie turpis, in tristique urna mauris vitae ligula."))
