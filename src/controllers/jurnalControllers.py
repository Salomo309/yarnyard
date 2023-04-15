from flask import jsonify, request

from models.jurnalModels import JurnalModels

class JurnalControllers:
    @staticmethod
    def getJurnal():
        try:
            fetchedData = JurnalModels.getAllJurnal()
                        
            if fetchedData is None:
                return "No Jurnal Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_jurnal": d.getIDJurnal(),
                                "id_tanaman": d.getIDTanaman(),
                                "tanggal_jurnal": d.getTanggalJurnal(),
                                "deskripsi_jurnal": d.getDeskripsiJurnal()})
                    
                return jsonify(res), 200
                
        except Exception as e:
            return str(e), 400