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

@jurnalRoutes.route("/addjurnal", methods=["POST"])
def post_jurnal():
    return JurnalControllers.postJurnal()

@jurnalRoutes.route("/editjurnal/<int:idJurnal>", methods=["PUT"])
def edit_jurnal(idJurnal):
    return JurnalControllers.editJurnal(idJurnal)