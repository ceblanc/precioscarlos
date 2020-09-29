print("Calculadora Espacio Orgánico\n")
area=int(input("""Selecciona una opción:
- Frutería 1
- Supermercado 2
- Herbolario 3\n
Opción: """))

if area == 1:

    coste=float(input("Por favor, introduce un coste: "))
    margen=1.68
    iva=int(input("Por favor, introduce el IVA: "))

    def calculadora(coste,margen,iva):
        resultado=coste*margen+(coste*iva/100)
        return resultado

    precio_venta=calculadora

    print(precio_venta(coste,margen,iva))

elif area == 2:

    coste=float(input("Por favor, introduce un coste: "))
    margen=1.45
    iva=int(input("Por favor, introduce el IVA: "))

    def calculadora(coste,margen,iva):
        resultado=coste*margen+(coste*iva/100)
        return resultado

    precio_venta=calculadora

    print(precio_venta(coste,margen,iva))

elif area == 3:

    coste=float(input("Por favor, introduce un coste: "))
    margen=1.52
    iva=int(input("Por favor, introduce el IVA: "))

    def calculadora(coste,margen,iva):
        resultado=coste*margen+(coste*iva/100)
        return resultado

    precio_venta=calculadora

    print(precio_venta(coste,margen,iva))

else:
    print("No existe ese área\n")
    

