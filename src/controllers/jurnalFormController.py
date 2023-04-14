from flask import jsonify, request

from models.jurnalFormModels import JurnalForm

class JurnalFormController:
    @staticmethod
    def getJurnal():
        try:
            fetchedData = JurnalForm.getAllJurnal()

            if fetchedData is None:
                return "No Jurnal Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_jurnal": d.getIdJurnal(),
                                "id_tanaman": d.getIdTanaman(),
                                "tanggal_jurnal": d.getTanggal(),
                                "deskripsi": d.getDeskripsi()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400
