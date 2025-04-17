import csv, os, pandas as pd

def ingresar_ventas(lista_ventas):
    while True:
        #Ingresar las ventas
        try:
            producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad: "))
            fecha = input("Ingrese la fecha de la venta (AAAA-MM-DD): ")
            precio = float(input("Ingrese le precio del producto: "))
            cliente = input("Ingrese el nombre del cliente: ").upper()
        except ValueError:
            print("Entradas no validas, intentenlo nuevamente")
            continue
        
        venta = {
            'producto' : producto,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }
        
        lista_ventas.append(venta)
        
        continuart = input("Desea ingresar otra venta S/N :").lower()
        if continuart == "s":
            print("\n ------ Ingresando otra venta -----")
        elif continuart == "n":
            break
        else:
            print("\nOpcion no valida")

def guardar_ventas(ventas):
    if not ventas:
        print("No hay ventas que guardar en el CSV")
    else:
        if os.path.exists("ventas.csv"):
            #Si el archivo existe se agrega Append
            with open("ventas.csv",'a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo, fieldnames=["producto","cantidad","precio","fecha","cliente"])
                guardar.writerows(ventas)     
        else: #Si el archivo no existe se crea
            with open("ventas.csv",'w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo, fieldnames=["producto","cantidad","precio","fecha","cliente"])
                guardar.writeheader()
                guardar.writerows(ventas)
        #Limpio ventas en memoria
        ventas = []
        print("Datos Guardados con exito")

def analizar_ventas():
    df = pd.read_csv("ventas.csv")
    print("\n---------------------------- RESUMEN DE VENTAS ----------------------------")
    
    df['subtotal'] = df['cantidad'] * df["precio"]
    total_ingreso = df["subtotal"].sum()
    
    print(f"Total de ventas {total_ingreso:.2f}")
    
    #Producto mas vendido
    producto_top = df.groupby('producto')['cantidad'].sum().idxmax()
    print(f"El prodcuto mas vendido es {producto_top}")
    
    #Cliente TOP
    cliente_top = df.groupby('cliente')['cantidad'].sum().idxmax()
    print(f"EL cliente TOP es {cliente_top}")
    
    #Ventas por fecha
    ventas_fecha = df.groupby('fecha')['subtotal'].sum().sort_values(ascending=False)
    print(ventas_fecha)
    