from flask import Blueprint
from controllers.jurnalControllers import JurnalControllers

jurnalRoutes = Blueprint("jurnalRoutes", __name__)

# jurnalRoutes.route("/", methods=["GET"])(JurnalControllers.getJurnal)
@jurnalRoutes.route("/", methods=["GET"])
def get_jurnals():
    return JurnalControllers.getJurnal()

@jurnalRoutes.route("/<int:idTanaman>", methods=["GET"])
def get_jurnal(idTanaman):
    return JurnalControllers.getJurnalByIdTanaman(idTanaman)

@jurnalRoutes.route("/deletejurnal/<int:idJurnal>", methods=["DELETE"])
def delete_todolist(idJurnal):
    return JurnalControllers.deleteJurnalByIdJurnal(idJurnal)
