from models.db import mysql


class TodolistModels:
    def __init__(self, id_tdl, id_tanaman, waktu, deskripsi_tdl):
        self.id_tdl = id_tdl
        self.id_tanaman = id_tanaman
        self.waktu = waktu
        self.deskripsi_tdl = deskripsi_tdl

    @classmethod
    def getAllTodolist(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM todolist")

        dataTDL = cursor.fetchall()

        # If empty set
        if len(dataTDL) == 0:
            cursor.close()
            return None
        else:
            listTDL = []
            for data in dataTDL:
                id_tdl, id_tanaman, waktu, deskripsi_tdl = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tdl = id_tdl
                self.id_tanaman = id_tanaman
                self.waktu = waktu
                self.deskripsi_tdl = deskripsi_tdl

                listTDL.append(self)

            cursor.close()
            return listTDL

    @classmethod
    def getTodolist(cls, idTanaman):
        cursor = mysql.connection.cursor()
        query = '''
            SELECT * 
            FROM todolist 
            WHERE id_tanaman = %s
            ORDER BY waktu ASC
        '''
        cursor.execute(query, (idTanaman,))
        dataTDL = cursor.fetchall()

        # If empty set
        if len(dataTDL) == 0:
            cursor.close()
            return None
        else:
            listTDL = []
            for data in dataTDL:
                id_tdl, id_tanaman, waktu, deskripsi_tdl = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tdl = id_tdl
                self.id_tanaman = id_tanaman
                self.waktu = waktu
                self.deskripsi_tdl = deskripsi_tdl

                listTDL.append(self)

            cursor.close()
            return listTDL

    @classmethod
    def deleteTodolist(cls, idTDL):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                DELETE FROM todolist
                WHERE id_tdl = %s
            '''
            cursor.execute(query, (idTDL,))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()

    def getIDTDL(self):
        return self.id_tdl

    def getIDTanaman(self):
        return self.id_tanaman

    def getWaktuTDL(self):
        return self.waktu

    def getDeskripsiTDL(self):
        return self.deskripsi_tdl
