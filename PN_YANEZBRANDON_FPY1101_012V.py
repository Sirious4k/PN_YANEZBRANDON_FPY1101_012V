import random
import csv

# Lista de trabajadores
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández',
                'Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

# Lista para almacenar los saldos
lista_saldos = []

# Funciones

def sueldos_random():
    return random.randint(300000, 2500000)

# Generar sueldos aleatorios para cada trabajador
def generar_sueldos():
    global lista_saldos
    lista_saldos = [(nombre, sueldos_random()) for nombre in trabajadores]
    print("Sueldos aleatorios asignados correctamente.")

# Clasificar sueldos por categorías
def clasificar_sueldos():
    global lista_saldos
    menores_800k = []
    entre_800k_2m = []
    mayores_2m = []
    
    for nombre, saldo in lista_saldos:
        if saldo < 800000:
            menores_800k.append((nombre, saldo))
        elif saldo >= 800000 and saldo <= 2000000:
            entre_800k_2m.append((nombre, saldo))
        else:
            mayores_2m.append((nombre, saldo))
    
    # Ordenar por categorías
    menores_800k.sort()
    entre_800k_2m.sort()
    mayores_2m.sort()
    
    # Mostrar resultados
    print(f"Trabajadores con sueldos menores a $800.000 TOTAL {len(menores_800k)}:")
    for nombre, saldo in menores_800k:
        print(f"{nombre}: ${saldo}")
    print(f"\nTrabajadores con sueldos entre $800.000 y $2.000.000 TOTAL {len(entre_800k_2m)}:")
    for nombre, saldo in entre_800k_2m:
        print(f"{nombre}: ${saldo}")
    print(f"\nTrabajadores con sueldos mayores a $2.000.000 TOTAL {len(mayores_2m)}:")
    for nombre, saldo in mayores_2m:
        print(f"{nombre}: ${saldo}")

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
    
menu()