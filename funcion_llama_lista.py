def crea_lista():

    datos=[]

    coste=float(input("Coste: "))
    margen=float(input("Margen: "))
    iva=float(input("Iva: "))

    datos.append(coste)
    datos.append(margen)
    datos.append(iva)

    return datos

def operacion(datos):

    resultado=datos[0]*datos[1]+(datos[0]*datos[2]/100)
        
    return resultado

precio=crea_lista()
print(operacion(precio))
