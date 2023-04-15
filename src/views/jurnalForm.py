# Form implementation generated from reading ui file 'jurnalForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import datetime
from controllers.jurnalControllers import JurnalControllers
import sqlite3


class Ui_JurnalForm(object):
    def setupUi(self, JurnalForm):
        JurnalForm.setObjectName("JurnalForm")
        JurnalForm.resize(960, 600)
        self.header = QtWidgets.QWidget(parent=JurnalForm)
        self.header.setEnabled(True)
        self.header.setGeometry(QtCore.QRect(0, 0, 960, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet(
            "*{\n"
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
        "")

        # Header
        self.header.setObjectName("header")
        self.frame_logo = QtWidgets.QFrame(parent=self.header)
        self.frame_logo.setGeometry(QtCore.QRect(459, 9, 42, 42))
        self.frame_logo.setObjectName("frame_logo")
        self.label = QtWidgets.QLabel(parent=self.frame_logo)
        self.label.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../assets/logo_circle.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.btn_submit_2 = QtWidgets.QPushButton(parent=self.header)
        self.btn_submit_2.setGeometry(QtCore.QRect(10, 15, 111, 31))
        self.btn_submit_2.setStyleSheet(
            "QPushButton {\n"
        "    padding: 5px 10px;\n"
        "    border-radius: 15px;\n"
        "    background: #3C6255;\n"
        "    color: #F7F3D7;\n"
        "    height: 40px;\n"
        "    width: 243px;\n"
        "    font-size: 16px;\n"
        "    font-weight: 600;\n"
        "    cursor: pointer;\n"
        "    text-align: left;\n"
        "}\n"
        "\n"
                "QPushButton:hover {\n"
                "    background-color: #23493C;\n"
                "}")
        self.btn_submit_2.setDefault(False)
        self.btn_submit_2.setFlat(False)
        self.btn_submit_2.setObjectName("btn_submit_2")
        self.footer = QtWidgets.QWidget(parent=JurnalForm)
        self.footer.setEnabled(False)
        self.footer.setGeometry(QtCore.QRect(0, 540, 960, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.footer.setAutoFillBackground(False)
        self.footer.setStyleSheet("#footer {\n"
                                "    background-color: #F7F4D9;\n"
                                "}")

        # Footer
        self.footer.setObjectName("footer")
        self.frame = QtWidgets.QFrame(parent=self.footer)
        self.frame.setGeometry(QtCore.QRect(0, 540, 960, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.body = QtWidgets.QWidget(parent=JurnalForm)
        self.body.setGeometry(QtCore.QRect(0, 60, 960, 480))
        self.body.setStyleSheet("#body {\n"
                                "    background-color: #F7F4D9;\n"
                                "}")

        # Body
        self.body.setObjectName("body")
        self.content = QtWidgets.QFrame(parent=self.body)
        self.content.setGeometry(QtCore.QRect(-1, 9, 961, 471))
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.submit = QtWidgets.QFrame(parent=self.content)
        self.submit.setGeometry(QtCore.QRect(0, 410, 960, 61))
        self.submit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.submit.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.submit.setObjectName("submit")
        self.btn_submit = QtWidgets.QPushButton(parent=self.submit)
        self.btn_submit.setGeometry(QtCore.QRect(390, 10, 181, 31))
        self.btn_submit.setStyleSheet(
            "QPushButton {\n"
        "    padding: 5px 10px;\n"
        "    border-radius: 15px;\n"
        "    background: #3C6255;\n"
        "    color: #F7F3D7;\n"
        "    height: 40px;\n"
        "    width: 243px;\n"
        "    font-size: 16px;\n"
        "    font-weight: 600;\n"
        "    cursor: pointer;\n"
        "}\n"
        "\n"
                "QPushButton:hover {\n"
                "    background-color: #23493C;\n"
                "}")
        self.btn_submit.setDefault(False)
        self.btn_submit.setFlat(False)
        self.btn_submit.setObjectName("btn_submit")
        self.frame_2 = QtWidgets.QFrame(parent=self.content)
        self.frame_2.setGeometry(QtCore.QRect(-1, 9, 961, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 60, 661, 311))
        self.plainTextEdit.setStyleSheet(
            "QPlainTextEdit {\n"
        "    padding: 7px 10px;\n"
        "    border-radius: 15px;\n"
        "    background: #61876E;\n"
        "    color: #F7F3D7;\n"
        "    height: 40px;\n"
        "    width: 243px;\n"
        "    font-size: 15px;\n"
        "    font-weight: 600;\n"
        "    cursor: pointer;\n"
        "}\n"
        "\n"
                "QPlainTextEdit:hover {\n"
                "    background-color: #23493C;\n"
                "}")
        self.plainTextEdit.setObjectName("plainTextEdit")

        connection = sqlite3.connect('database.db')
        self.btn_submit.clicked.connect(self.setJurnal(connection))

        self.retranslateUi(JurnalForm)
        QtCore.QMetaObject.connectSlotsByName(JurnalForm)

    def retranslateUi(self, JurnalForm):
        _translate = QtCore.QCoreApplication.translate
        JurnalForm.setWindowTitle(_translate("JurnalForm", "Dialog"))
        self.btn_submit_2.setText(_translate("JurnalForm", "< Kembali"))
        self.btn_submit.setText(_translate("JurnalForm", "Submit"))
        self.plainTextEdit.setPlainText(_translate("JurnalForm", "Tulis deskripsi jurnal"))

    def setJurnal(self, connection):
        cursor = connection.cursor()
        # dapatkan isi jurnal yang telah ditulis
        journal = self.plainTextEdit.toPlainText()

        jc = JurnalControllers()
        id_jurnal = jc.getJurnal()[0]['id_jurnal']
        id_tanaman = jc.getJurnal()[0]['id_tanaman']

        # buat tuple data untuk dimasukkan ke dalam tabel jurnal
        data = (id_jurnal, id_tanaman, datetime.date.today(), journal)

        # masukkan data ke dalam tabel jurnal pada database
        cursor.execute("INSERT INTO jurnal (id_jurnal, id_tanaman, tanggal, isi_jurnal) VALUES (?, ?, ?, ?)", data)
        connection.commit()

        # tutup koneksi database
        cursor.close()
        connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JurnalForm = QtWidgets.QDialog()
    ui = Ui_JurnalForm()
    ui.setupUi(JurnalForm)
    JurnalForm.show()
    sys.exit(app.exec())
