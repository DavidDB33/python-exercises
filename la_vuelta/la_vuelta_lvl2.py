"""
¡¡Ya sabes el precio!!
¡Pero ahora deberías darle el cambio!

¿Puedes hacer un algoritmo para saber el conjunto mínimo de billetes a devolver?
"""
from la_vuelta_lvl1 import muestra_total, calcula_total
import json





###### TODO: PROGRAMAR AQUÍ ######
def calcula_cambio(total: float, monedas: list[int]) -> dict[float, int]:
    return { 0.01 : int(total * 100) } # No es la solución :P
##################################


















def muestra_cambio(cambio: dict[float, int]) -> None:
    print(" **Calculando cambio...**")
    print(" - Aquí está el cambio:")
    for moneda, numero in cambio.items():
        print(f' {numero} monedas de {moneda} €')

def main():
    cesta = { # Cantidades [Kg]
        'guisantes' : 0.5,
        'coles de bruselas' : 0.3,
        'kiwi pulpa verde' : 0.15,
        'patata roja' : 2.0,
        'limon primafiori' : 0.1,
        'moras' : 0.3,
        'platanos extra' : 0.6
    }
    monedas = [
        0.01, 0.02, 0.05,
        0.10, 0.20, 0.50,
        1.00, 2.00, 5.00,
        10.00, 20.00, 50.00,
        100.00, 200.00, 500.00
    ]
    with open('datos/precios.json') as f:
        precios = json.load(f)

    total = calcula_total(cesta, precios)
    muestra_total(total)
    print("Tome, un billete de 50€")
    cambio_valor = 50 - total
    cambio = calcula_cambio(cambio_valor, monedas)
    muestra_cambio(cambio)
    if sum(cambio.values()) > 10:
        print(" + No puedo con tantas monedas!")
    else:
        print(" + Muchas gracias!")

if __name__ == '__main__':
    main()
