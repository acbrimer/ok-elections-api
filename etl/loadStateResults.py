import os
import pandas as pd
import sqlite3
from app.models.engine.app import db
from app.models import ElectionRace
from datetime import datetime

ROOT_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../')


def getResultsDF(SOURCE_DIR):
    stateResultsFiles = [f for f in os.listdir(SOURCE_DIR)]
    df = pd.concat([pd.read_csv(os.path.join(SOURCE_DIR, f),
                                engine='python', delimiter=",", encoding='utf-8', index_col=False) for f in stateResultsFiles])
    return df


def loadStateResults():
    df = getResultsDF(os.path.join(
        ROOT_DIR, 'data/source/state_election_results'))
    df.to_sql('df', con=db.engine, if_exists='replace')
    q = """ 
    SELECT 
        race_number, 
        elec_date,
        race_description,
        race_party,
        tot_race_prec,	
        race_prec_reporting,
        SUM(cand_tot_votes) as race_tot_votes,
        SUM(cand_absmail_votes) as race_absmail_votes,
        SUM(cand_early_votes) as race_early_votes,	
        SUM(cand_elecday_votes) as race_elecday_votes,
        MAX(cand_number) as race_num_candidates
    FROM df
        GROUP BY race_number, 
        elec_date, 
        race_description,
        race_party,
        tot_race_prec,
        race_prec_reporting
     """
    df_election_races = pd.read_sql(q, con=db.engine)
    df_election_races['elec_date'] = df_election_races.apply(
        lambda r: datetime.strptime(r['elec_date'], '%m/%d/%Y'), axis=1)
    df_election_races['elec_date_id'] = df_election_races.apply(
        lambda r: int(r['elec_date'].strftime('%Y%m%d')), axis=1)
    df_election_races.to_sql('election_races', con=db.engine,
                             if_exists='append', index=False)
    return ElectionRace.count_star()
