import random

def generar_lista_de_compra():
    productos = {
        'manzanas' : 1000,
        'bananos'  : 150,
        'cerezas' : 2000,
        'naranjas' : 1900,
        'pan': 2275,
        'leche': 900,
        'huevos': 3400,
        'queso': 4500
    }
    seleccion = random.sample(list(productos.items()), k = 5) # seleccionar 5 productos de la lista de compras
    return seleccion