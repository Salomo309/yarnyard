from flask import Blueprint
from controllers.tanamanControllers import TanamanControllers

tanamanRoutes = Blueprint("tanamanRoutes", __name__)

tanamanRoutes.route("/", methods=["GET"])(TanamanControllers.getTanaman)