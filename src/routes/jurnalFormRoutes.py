from flask import Blueprint
from controllers.jurnalControllers import JurnalControllers

jurnalFormRoutes = Blueprint("jurnalFormRoutes", __name__)

jurnalFormRoutes.route("/", methods=["GET"])(JurnalControllers.getAllJurnal)
