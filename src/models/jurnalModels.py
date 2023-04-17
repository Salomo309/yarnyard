from models.db import mysql

class JurnalModels:
    def __init__(self, id_jurnal, id_tanaman, tanggal_jurnal, deskripsi_jurnal):
        self.id_jurnal = id_jurnal
        self.id_tanaman = id_tanaman
        self.tanggal_jurnal = tanggal_jurnal
        self.deskripsi_jurnal = deskripsi_jurnal

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
                id_jurnal, id_tanaman, tanggal_jurnal, deskripsi_jurnal = data

                # initialize class
                self = cls.__new__(cls)
                self.id_jurnal = id_jurnal
                self.id_tanaman = id_tanaman
                self.tanggal_jurnal = tanggal_jurnal
                self.deskripsi_jurnal = deskripsi_jurnal

                listJurnal.append(self)

            cursor.close()
            return listJurnal
    
    @classmethod
    def getJurnal(cls, idTanaman):
        cursor = mysql.connection.cursor()
        query = '''
            SELECT * 
            FROM jurnal
            WHERE id_tanaman = %s
            ORDER BY tanggal_jurnal ASC
        '''
        cursor.execute(query, (idTanaman,))

        dataJurnal = cursor.fetchall()

        # If empty set
        if len(dataJurnal) == 0:
            cursor.close()
            return None
        else:
            listJurnal = []
            for data in dataJurnal:
                id_jurnal, id_tanaman, tanggal_jurnal, deskripsi_jurnal = data

                # initialize class
                self = cls.__new__(cls)
                self.id_jurnal = id_jurnal
                self.id_tanaman = id_tanaman
                self.tanggal_jurnal = tanggal_jurnal
                self.deskripsi_jurnal = deskripsi_jurnal

                listJurnal.append(self)

            cursor.close()
            return listJurnal

    @classmethod
    def deleteJurnal(cls, idJurnal):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                DELETE FROM jurnal
                WHERE id_jurnal = %s
            '''
            cursor.execute(query, (idJurnal,))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()

    def getIDJurnal(self):
        return self.id_jurnal

    def getIDTanaman(self):
        return self.id_tanaman

    def getTanggalJurnal(self):
        return self.tanggal_jurnal

    def getDeskripsiJurnal(self):
        return self.deskripsi_jurnal