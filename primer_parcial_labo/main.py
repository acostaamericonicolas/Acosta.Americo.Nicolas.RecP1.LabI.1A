from funciones_parcial1 import *
import json
import os

lista_elementos_con_marca_nueva = []
lista_insumos_act=[]
1
while True:
    os.system("cls")  # limpia el terminal de ejecuc
    opcion = mostrar_menu()  # importo el menu desde el archivo menu.py

    if opcion == "1":
        # abro el archivo insumos.csv, lo recorro y convierto en lista de # diccionarios
        archivo = input("ingrese archivo a cargar (insumos.csv): ")
        while archivo != "insumos.csv":
            archivo = input("Error!!! ingrese archivo a cargar (insumos.csv): ")
        with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                lista_elementos.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                        "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})
        
        lista_elementos = list(map(calcular_stock_disponible, lista_elementos)) 

    elif opcion == "2":
        motrar = mostrar_cantidad_por_marca(lista_elementos, "MARCA")

    elif opcion == "3":
        motrar = mostrar_marca_y_precios(lista_elementos, "MARCA")

    elif opcion == "4":
        motrar = mostrar_por_caracteristica(lista_elementos, "CARACTERISTICAS")

    elif opcion == "5":
        motrar = ordenar_listas_dict(lista_elementos, "MARCA", True)

    elif opcion == "6":  # hacer compras
        mostrar = hacer_compras(lista_elementos)

    # Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento".
    elif opcion == "7": # abro "productos.js" modo escritura
        mostrar = obtener_productos_json ()

    elif opcion == "8":  # abro el archivo productos.js, lo recorro y convierto en lista de diccionarios
        mostrar = leer_desde_json()

    elif opcion == "9":  # actualizar precios # abro el archivo insumos.csv, lo recorro y convierto en lista de # diccionarios y lo guardo en el mismo archivo.
        mostrar = actualizar_precios_()

    elif opcion == "10": 
        mostrar = agregar_nuevo_producto(lista_elementos)

    elif opcion == "11":
        mostrar = guardar_como_json_o_csv(lista_elementos)

    elif opcion == "12":  # salir
        salida = input("Confirma salida?: s/n: ")
        if salida == "s" or "S":
            break
    os.system("pause")  # pausa el sistema para ver los resultados
