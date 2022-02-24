# App

The root for the Flask-sqlalchemy API with deployment setup to Google Cloud Run.

# Deploy

**Important:** make sure `app.db` is removed from .gitignore before running deployment. Need to figure out a better solution for this to get around this.

To deploy to Google Cloud Run, run `deploy.bash` (script will always resolve to the correct `/app` deployment dir).
