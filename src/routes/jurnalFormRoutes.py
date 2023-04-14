from flask import Blueprint
from controllers.jurnalFormController import JurnalFormController

jurnalFormRoutes = Blueprint("jurnalFormRoutes", __name__)

jurnalFormRoutes.route("/", methods=["GET"])(JurnalFormController.getJurnal)
