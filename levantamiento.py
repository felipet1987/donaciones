from grupo_familiar import GrupoFamiliar
from table import Table


class Levantamiento:
    def __init__(self):
        self.punto = Table('punto')
        self.familiar = GrupoFamiliar()


    def totales(self):
            return {
                "totalPuntos": self.punto.count(),
                "totalPersonas": self.familiar.totalPersonas(),
            }
