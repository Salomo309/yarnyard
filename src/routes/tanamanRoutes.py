from flask import Blueprint
from controllers.tanamanControllers import TanamanControllers

tanamanRoutes = Blueprint("tanamanRoutes", __name__)

# tanamanRoutes.route("/", methods=["GET"])(TanamanControllers.getTanaman)
@tanamanRoutes.route("/", methods=["GET"])
def get_tanamans():
    return TanamanControllers.getTanaman()

@tanamanRoutes.route("/<int:idTanaman>", methods=["GET"])
def get_tanaman(idTanaman):
    return TanamanControllers.getTanamanById(idTanaman)