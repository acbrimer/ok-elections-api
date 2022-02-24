#!/usr/bin/python3
from models.engine.app import app, db

# app.register_blueprint(app_views)

if __name__ == "__main__":
    from routes import *
    # db.engine.echo = True
    app.run(debug=True)
