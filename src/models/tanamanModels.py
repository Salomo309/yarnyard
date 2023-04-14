from models.db import mysql

class TanamanModels:
    def __init__(self, id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar):
        self.id_tanaman = id_tanaman
        self.nama_tanaman = nama_tanaman
        self.tanggal_tanaman = tanggal_tanaman
        self.deskripsi_tanaman = deskripsi_tanaman
        self.gambar = gambar
    
    @classmethod
    def getAllTanaman(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tanaman")
        
        dataTanaman = cursor.fetchall()
        
        # If empty set
        if len(dataTanaman) == 0:
            cursor.close()
            return None
        else:
            listTanaman = []
            for data in dataTanaman:
                id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar = data
                
                # initialize class
                self = cls.__new__(cls)
                self.id_tanaman = id_tanaman
                self.nama_tanaman = nama_tanaman
                self.tanggal_tanaman = tanggal_tanaman
                self.deskripsi_tanaman = deskripsi_tanaman
                self.gambar = gambar
                
                listTanaman.append(self)
            
            cursor.close()
            return listTanaman
        
    def getIDTanaman(self):
        return self.id_tanaman
    
    def getNamaTanaman(self):
        return self.nama_tanaman
    
    def getTanggalTanaman(self):
        return self.tanggal_tanaman
    
    def getDeskripsiTanaman(self):
        return self.deskripsi_tanaman
    
    def getGambarTanaman(self):
        return self.gambar