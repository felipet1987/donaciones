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
        adultos_masculinos = self.table.df['adultosMasculinos'].sum().item()
        adultos_femeninos = self.table.df['adultosFemeninos'].sum().item()
        ninos_masculinos = self.table.df['ninosMasculinos'].sum().item()
        ninos_femeninos = self.table.df['ninosFemeninos'].sum().item()
        adultos_mayores = self.table.df['adultosMayores'].sum().item()
        sum = adultos_masculinos + \
              adultos_femeninos + \
              ninos_masculinos + \
              ninos_femeninos + \
              adultos_mayores
        return sum

