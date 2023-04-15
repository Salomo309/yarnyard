from flask import Blueprint
from controllers.jurnalControllers import JurnalControllers

jurnalRoutes = Blueprint("jurnalRoutes", __name__)

jurnalRoutes.route("/", methods=["GET"])(JurnalControllers.getJurnal)