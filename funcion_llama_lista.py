margenes=[1.45,1.52,1.68]

area_selecionada=int(input("Selecciona un área:\n""\n"
               "1.Supermercado: \n"
               "2.Herbolario: \n"
               "3.Frutería: \n""\n"
               "Selecciona 0 para salir del programa""\n""\n"
               "Selección: "))

def obtener_datos():

    datos=[]

    coste=float(input("\nPor favor, introduce un coste: "))
    iva=float(input("Por favor, introduce un IVA: "))

    datos.append(coste)
    datos.append(iva)

    return datos

def operacion(datos, area):

    if area==1:

        resultado=datos[0]*margenes[0]+(datos[0]*datos[1]/100)
        
        return resultado

    elif area==2:

        resultado=datos[0]*margenes[1]+(datos[0]*datos[1]/100)
        
        return resultado
    
    elif area==3:

        resultado=datos[0]*margenes[2]+(datos[0]*datos[1]/100)
        
        return resultado

precio=obtener_datos()

print("El precio en punto de venta es: ",(round(operacion(precio,area_selecionada),2)))
print("El precio en punto de venta es: ",(round(operacion(precio,area_selecionada)*1.04,2)))
