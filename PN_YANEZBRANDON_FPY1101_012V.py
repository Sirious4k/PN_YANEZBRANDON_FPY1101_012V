import random
import csv

# Lista de trabajadores
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández',
                'Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

# Funciones

# Menú

def menu():
    while True:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = int(input("Seleccione una opción (1-5)"))
        
        if opcion < 1 or opcion > 5:
            print("Opción inválida. Intente de nuevo.")
            
        elif opcion == 5:
            print("Gracias por usar el programa. Adiós!")
            break
            
        elif opcion == 1:
            print("Asignando sueldos aleatorios...")
            generar_sueldos()
            
        elif opcion == 2:
            print("Clasificando sueldos...")
            clasificar_sueldos()
            
        elif opcion == 3:
            print("Ver estadísticas...")
            ver_estadisticas()
        
        elif opcion == 4:
            print("Generando reporte de sueldos...")
            generar_reporte()
    