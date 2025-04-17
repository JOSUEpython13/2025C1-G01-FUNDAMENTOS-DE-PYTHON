
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
    