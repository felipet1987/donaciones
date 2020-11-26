from database import Database

class Table:

    def __init__(self,name):
        db = Database()
        self.df = db.to_df(name)

    def count(self):
        return len(self.df.index)



