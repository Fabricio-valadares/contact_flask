from .home.routes import app_home

def routes_register(app):
    app.register_blueprint(app_home)