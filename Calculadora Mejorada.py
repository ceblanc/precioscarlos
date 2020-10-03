#Falta por mejorar:
#-Poder elegir área cada vez
#-Salir del programa introduciendo "0"


#Sustituir "Escribe 0 para salir del programa" por "Escribe 0 en cualquier momento para salir del programa"
print("Calculadora Espacio Orgánico\n")
area=int(input("""Selecciona una opción:
- Frutería 1
- Supermercado 2
- Herbolario 3\n\n
Escribe 0 para salir del programa
Opción: """))

def calculadora(coste,margen,iva):
    
        resultado=coste*margen+(coste*iva/100)
        
        return resultado
    
while True:

    if area == 1:

        coste=float(input("Por favor, introduce un coste: "))
    
        margen=1.68
    
        iva=int(input("Por favor, introduce el IVA: "))

        precio_venta=calculadora

        print("El precio de venta en Supermercado es:",precio_venta(coste,margen,iva),"€")
        print("El precio de venta en Tienda Online es:",round((precio_venta(coste,margen,iva))*1.04,2),"€\n")

    elif area == 2:

        coste=float(input("Por favor, introduce un coste: "))
    
        margen=1.45
    
        iva=int(input("Por favor, introduce el IVA: "))

        precio_venta=calculadora

        print("El precio de venta en Supermercado es:",precio_venta(coste,margen,iva),"€")
        print("El precio de venta en Tienda Online es:",round((precio_venta(coste,margen,iva))*1.04,2),"€\n")

    elif area == 3:

        coste=float(input("Por favor, introduce un coste: "))
    
        margen=1.52
    
        iva=int(input("Por favor, introduce el IVA: "))

        precio_venta=calculadora

        print("El precio de venta en Supermercado es:",precio_venta(coste,margen,iva),"€")
        print("El precio de venta en Tienda Online es:",round((precio_venta(coste,margen,iva))*1.04,2),"€\n")

    elif area == 0:
    
        break
