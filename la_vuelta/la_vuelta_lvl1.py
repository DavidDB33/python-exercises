"""
¡¡¡ ACABAS DE ABRIR UNA TIENDA !!!

Tu primer cliente trae varios productos:
¿Cuánto es su precio?
"""





###### TODO: PROGRAMAR AQUÍ ######
def calcula_total(cesta: dict, precios: dict) -> float:
    # Sabrías hacerlo en una línea?
    raise NotImplementedError("PRIMERO DEBES SUPERAR EL PRIMER NIVEL")
##################################








def muestra_total(total: float) -> None:
    print(" - ¡Hola!")
    print(" + Hola")
    print(f" - Serán {total} €. No se adminte tarjeta")

def main():
    cesta = dict( # Cantidades
        manzana = 2,
        pera = 3,
        sandia = 1
    )
    precios = dict( # En €
        manzana = 0.20,
        pera = 0.30,
        sandia = 1.5,
    )
    total = calcula_total(cesta, precios)
    return total

if __name__ == '__main__':
    main()
