import sqlalchemy as db
import pandas as pd

def get():
    engine = db.create_engine('mysql+mysqlconnector://rsapcl_remote:aePyPNMLQwBjv9@rsap.cl:3306/rsapcl_rsap')
    connection = engine.connect()
    df =  pd.read_sql_table('registro',connection)
    return df