from table import Table


class GrupoFamiliar:
    def __init__(self):
        self.table = Table('grupo_familiar')

    def df(self):
        return self.table.df

    def totales(self):
        return {
            "adultosMasculinos": self.table.df['adultosMasculinos'].sum().item(),
            "adultosFemeninos": self.table.df['adultosFemeninos'].sum().item(),
            "adultosMayores": self.table.df['adultosMayores'].sum().item(),
            "ninosMasculinos": self.table.df['ninosMasculinos'].sum().item(),
            "ninosFemeninos": self.table.df['ninosFemeninos'].sum().item(),
        }

    def totalPersonas(self):
        sum = 0
        return sum

