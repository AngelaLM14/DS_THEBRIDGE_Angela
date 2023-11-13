import numpy as np


TAM_TABLERO = (10,10)

def crea_tablero(dimensiones=TAM_TABLERO, tile = " "):
    return np.full(dimensiones,tile)

dimensiones_usuario = input(f"De cuánto quieres el tablero (alto,ancho) ({TAM_TABLERO})")

dim_val = [int (valor) for valor in dimensiones_usuario.split(",")]


print(crea_tablero(dim_val))

