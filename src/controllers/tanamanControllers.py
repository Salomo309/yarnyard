from flask import jsonify, request

from models.tanamanModels import TanamanModels

class TanamanControllers:
    @staticmethod
    def getTanaman():
        try:
            fetchedData = TanamanModels.getAllTanaman()
                        
            if fetchedData is None:
                return "No Tanaman Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tanaman": d.getIDTanaman(),
                                "nama_tanaman": d.getNamaTanaman(),
                                "tanggal_tanaman": d.getTanggalTanaman(),
                                "deskripsi_tanaman": d.getDeskripsiTanaman(),
                                "gambar": d.getGambarTanaman()})
                    
                return jsonify(res), 200
                
        except Exception as e:
            return str(e), 400