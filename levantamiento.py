from grupo_familiar import GrupoFamiliar
from table import Table


class Levantamiento:
    def __init__(self):
        self.punto = Table('punto')
        self.familiar = GrupoFamiliar()


    def totales(self):
            return {
                "puntosLevantados": self.punto.count(),
                "personasLevantadas": self.familiar.totalPersonas(),
            }
