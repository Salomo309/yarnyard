from models.db import mysql

class JurnalForm() :
    def __init__(self, id_jurnal, id_tanaman, tanggal_jurnal, deskripsi):
        self.id_jurnal = id_jurnal
        self.id_tanaman = id_tanaman
        self.tanggal_jurnal = tanggal_jurnal
        self.deskripsi = deskripsi

    @classmethod
    def getAllJurnal(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM jurnal")

        dataJurnal = cursor.fetchall()

        # If empty set
        if len(dataJurnal) == 0:
            cursor.close()
            return None
        else:
            listJurnal = []
            for data in dataJurnal:
                id_jurnal, id_tanaman, tanggal_jurnal, deskripsi = data

                # initialize class
                self = cls.__new__(cls)
                self.id_jurnal = id_jurnal
                self.id_tanaman = id_tanaman
                self.tanggal_jurnal = tanggal_jurnal
                self.deskripsi = deskripsi

                listJurnal.append(self)

            cursor.close()
            return listJurnal

    def getIdJurnal(self):
        return self.id_jurnal

    def getIdTanaman(self):
        return self.id_tanaman

    def getTanggal(self):
        return self.tanggal_jurnal

    def getDeskripsi(self):
        return self.deskripsi

    def setIdJurnal(self, idj):
        self.id_jurnal = idj

    def setIdTanaman(self, idt):
        self.id_tanaman = idt

    def setTanggal(self, tanggal):
        self.tanggal_jurnal = tanggal

    def setDeskripsi(self, deskripsi):
        self.deskripsi = deskripsi
