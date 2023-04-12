import sys
from PyQt6.QtWidgets import QApplication
from threading import Thread

from app import app
from views import displayManager

from routes.artikelRoutes import artikelRoutes
from routes.mainRoutes import mainRoutes

def initServer():
    # Backend
    app.register_blueprint(mainRoutes, url_prefix="/")
    app.register_blueprint(artikelRoutes, url_prefix = "/artikel")
    
    app.run(port=3000, use_reloader=False)

if __name__ == '__main__':
    threadBackend = Thread(target=initServer)
    threadBackend.setDaemon(True)
    threadBackend.start()
    
    window = QApplication(sys.argv)
    view = displayManager.PageController()
    sys.exit(window.exec())