from sqlalchemy import create_engine, inspect
import pandas as pd

db_url = 'mysql+mysqlconnector://clrsap_reporte:8kGWG!@tUmBoM&@rsap.cl:3306/clrsap_rsapcl_rsap'


class Database:

    def __init__(self):
        self.engine = create_engine(db_url)
        self.conn = self.engine.connect()

    def get_tables(self):
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        return tables


    def to_df(self, name):
        df = pd.read_sql_table(name, self.conn)
        return df

