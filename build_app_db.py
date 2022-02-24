import os
from app.models.engine.app import db
from app.models.ElectionDate import *
import pandas as pd
from etl.loadStateResults import loadStateResults


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.engine.echo = True
    db.drop_all()
    db.create_all()

    fp = os.path.join(
        os.getcwd(), 'data/staging/election_dates.csv')
    loadStateResults()
    df_dates = pd.read_csv(fp)
    df_dates.to_sql('election_dates', con=db.engine,
                    if_exists='append', index=False)
    print("Done!")
