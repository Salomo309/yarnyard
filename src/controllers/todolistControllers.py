from flask import jsonify, request

from models.todolistModels import TodolistModels

class TodolistControllers:
    @staticmethod
    def getTodolist():
        try:
            fetchedData = TodolistModels.getAllTodolist()
                        
            if fetchedData is None:
                return "No Todolist Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tdl": d.getIDTDL(),
                                "id_tanaman": d.getIDTanaman(),
                                "waktu": d.getWaktuTDL(),
                                "deskripsi_tdl": d.getDeskripsiTDL()})
                    
                return jsonify(res), 200
                
        except Exception as e:
            return str(e), 400