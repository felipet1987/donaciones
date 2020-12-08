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
                   1: {"name": "Pañales", "qty": len(self.df_lista.query('panales_req == "Si"').index)},
                   2: {"name": "Comida", "qty": len(self.df_lista.query('comida_req == "Si"').index)},
                   3: {"name": "Leña", "qty": len(self.df_lista.query('lena_req == "Si"').index)},
                   4: {"name": "Leche", "qty": len(self.df_lista.query('leche_req == "Si"').index)},
                   5: {"name": "Agua", "qty": len(self.df_lista.query('agua_req == "Si"').index)},
                   6: {"name": "Ropa de cama", "qty": len(self.df_lista.query('ropaCama == "Si"').index)},
                   7: {"name": "Aseo personal", "qty": len(self.df_lista.query('aseoPersonal == "Si"').index)},
                   8: {"name": "Articulos de limpieza", "qty": len(self.df_lista.query('artLimpieza == "Si"').index)},
                   9: {"name": "Canasta familiar", "qty": len(self.df_lista.query('canastaFamiliar == "Si"').index)}
        }
