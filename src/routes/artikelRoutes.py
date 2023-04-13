from flask import Blueprint
from controllers.artikelController import ArtikelController

artikelRoutes = Blueprint("artikelRoutes", __name__)

artikelRoutes.route("/", methods=["GET"])(ArtikelController.getArtikel)