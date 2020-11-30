from table import Table
import requests
import pandas as pd

class Requerimiento:
    def __init__(self):
        response = requests.post("http://rsap.cl/rsap/services/api/detallePunto.php")
        lista = response.json()['lista']
        self.df_lista = pd.DataFrame(lista)
        self.table = Table('requerimientos')

    def levantados(self):
        return {
            "panales": len(self.df_lista.query('panales_req == "Si"').index),
            "comida": len(self.df_lista.query('comida_req == "Si"').index),
            "lena": len(self.df_lista.query('lena_req == "Si"').index),
            "leche": len(self.df_lista.query('leche_req == "Si"').index),
            "agua": len(self.df_lista.query('agua_req == "Si"').index),
            "ropa de Cama": len(self.df_lista.query('ropaCama == "Si"').index),
            "aseo Personal": len(self.df_lista.query('aseoPersonal == "Si"').index),
            "articulos de Aseo ": len(self.df_lista.query('artLimpieza == "Si"').index),
            "canasta familiar ": len(self.df_lista.query('canastaFamiliar == "Si"').index),
        }
