# Introducción a la Programación CONTROL No.2
# NRC: 11564
# Curso: TDFI102
# Sección:685
# Eduardo Rubio
# 13.695.741-4

# importo librerias
import os
import csv

# suma_precios = 0

# genero un mensaje de bienvenida al programa
mensaje_1 = """
    ::::::::::::::::::::::::::::::::::::::::::
      Bienvenidos a Empresa Real Flash SPA\n
      enviamos encomiendas a todo el Mundo
    ::::::::::::::::::::::::::::::::::::::::::
    """
# imprimo el mensaje
print(mensaje_1)

# creo mi primera funcion para la opcion 1 ingresar la informacion


def envios(flash_spa):
    # Abrimos el archivo en modo 'append' para agregar sin borrar
    with open(flash_spa, 'a', newline='') as archivo:
        while True:
            # Pedimos los datos de la encomienda
            name_rem = input("Ingrese Nombre del Remitente : ")
            name_dest = input("Ingrese Nombre del Destinatario : ")
            f_envio = input("Ingrese fecha de envio (D-M-A) : ")
            region_origen = input("Ingrese Region de Origen : ")
            region_destino = input("Ingrese Region de destino : ")
            # este if se encarga de validar que que las ciudades no sean iguales
            if region_origen == region_destino:
                print(
                    "\n Error : Las ciudades de Origen-Destino no pueden ser iguales\n")
                break
            tipo = input(
                "Seleccione tipo:\n1.- Sobre\n2.- Caja\n")
            # este if se encarga de definir de tipo de envio
            if tipo == "1":
                print("\nEl sobre tiene un costo de $5000.- CLP")
                precio = "5000"
                tipo2 = "Sobre"
            else:
                print("\nLa Caja tiene un costo de $15000.- CLP")
                precio = "15000"
                tipo2 = "Caja"
            # aca escribo en el archivo csv los datos ingresados
            archivo.write(
                f'{name_rem},{name_dest},{f_envio},{region_origen},{region_destino},{tipo},{tipo2},{precio}\n')
            # valido los ingresos
            print("\nSus datos han sido ingresados correctamente\n")
            # imprimo mensaje de bienvenida
            print(mensaje_1)
            break

# creo mi segunda funcion para la opcion 2 reporte de encomiendas


def report():
    print("\n Resumen de Encomiendas\n")
    # busco mi archivo creado previamente en modo read
    with open('flash_spa.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
    print(mensaje_1)


# creo mi tercera funcion para la opcion 3 ingresos
def ingresos_t(nombre_archivo, indice_columna):
    suma = 0
    # abro archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        # por si dejo n encabezado en el excel
        # next(lector)
        for fila in lector:
            try:
                # comienzo la suma por celdas
                suma += float(fila[indice_columna])
            except (ValueError, IndexError):
                # Ignoro errores deceldas vacías o texto
                continue
    # tengo la suma en una variable
    return suma


# imprimimo el menu inicial
while True:
    opcion = input(
        "1.- Registrar Encomienda\n2.- Reporte de Encomiendas\n3.- Montos Generales\n4.- Salir \n\nSeleccione Opcion : ")
    if opcion == "1":
        envios('flash_spa.csv')
    elif opcion == "2":
        report()
    elif opcion == "3":
        total = ingresos_t('flash_spa.csv', 7)
        print(f"La suma Total de ingresos es: {total}\n")
        print(mensaje_1)
    elif opcion == "4":
        break
