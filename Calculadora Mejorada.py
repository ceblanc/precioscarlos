#Falta por mejorar:
#-Poder elegir área cada vez
#-Salir del programa introduciendo "0"

margen=[1.68,1.45,1.52]

def calculadora(coste,margen,iva):
    
        resultado=coste*margen+(coste*iva/100)
        
        return resultado
    
while True:

    #Sustituir "Escribe 0 para salir del programa" por "Escribe 0 en cualquier momento para salir del programa"
    print("Calculadora Espacio Orgánico\n")
    area=int(input("""Selecciona una opción:
    - Frutería 1
    - Supermercado 2
    - Herbolario 3\n\n
    Escribe 0 para salir del programa
    Opción: """))

    if area == 0:
        break
    elif area <0 or area > 3:
        print ("ERROR: la selección elegida no es correcta, por favor, elige una de las disponbiles")
    else:
        #Solicitamos los datos
        coste=float(input("Por favor, introduce un coste: "))

        iva=int(input("Por favor, introduce el IVA: "))

        #Realizamos las operaciones
        precio_venta=calculadora(coste,margen,iva)

        #Visualizamos el resultado
        print("El precio de venta en Supermercado es:",precio_venta(coste,margen[area+1],iva),"€")
        print("El precio de venta en Tienda Online es:",round((precio_venta(coste,margen[area+1],iva))*1.04,2),"€\n")
