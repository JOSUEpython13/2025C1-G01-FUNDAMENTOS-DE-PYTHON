'''
Autor: Josue Solano Redondo
Fecha: 04/16/2025
Version 1.0
Sistema de Gestión de Ventas que nos permita ingresar, almacenar y analizar datos de ventas.
'''
import os
from modulo1 import ingresar_ventas, guardar_ventas, analizar_ventas

def limpiar_pantalla():
    #Limpia pantalla de la terminal en ejecucion
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione ENTER para continuar.....")

#Menu Principal
def menu():
    #variable del sistema
    ventas = []
    while True:
        print("\n******* Menu Principal *******")
        print("1. Ingresar Ventas")
        print("2. Guardar Datos")
        print("3. Analizar datos")
        print("4. Salir del sistema")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            limpiar_pantalla()
            print("\n ***** Ingresar Ventas *****")
            ingresar_ventas(ventas)
            pausar()
            
        elif opcion == "2":
            limpiar_pantalla()
            print("\n ***** Guardar Datos *****")
            guardar_ventas(ventas)
            pausar()
            
        elif opcion == "3":
            limpiar_pantalla()
            print("\n ***** Analizar Datos *****")
            analizar_ventas()
            pausar()
            
        elif opcion == "4":
            print("\n Gracias por usar el sistema, vuelva pronto!!")
            pausar()
            limpiar_pantalla()
            break # - Cierre del sistema
        
        else:
            limpiar_pantalla()
            print("Opcion no valida. Intente nuevamente")
            pausar()
            
#Ejecucion del sistema
if __name__ == "__main__":
    print("Bienvenido al sistema de Gestion de Ventas")
    menu()

