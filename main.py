# Main script for the application

class Producto():

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"{self.nombre} | ${self.precio}"
    
class ListaProductos():

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto and producto not in self.productos:
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado a la lista.")

        elif producto in self.productos:
            print(f"El producto '{producto.nombre}' ya está en la lista.")

        else:
            print("Producto no válido. No se agregó a la lista.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos registrados:")
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos registrados.")

    def sumar_precios(self):
        total = sum(producto.precio for producto in self.productos)
        print(f"Total de la compra: ${total}")

    def productos_mayores_a_precio(self, precio):
        productos_filtrados = [producto for producto in self.productos if producto.precio > precio]
        if productos_filtrados:
            print(f"Productos con precio mayor a ${precio}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos con precio mayor a ${precio}.")

ListaProductos1 = ListaProductos()
comando = ""
while True:
    print("""
    1. agregar productos a una lista
    2. Mostrar todos los productos registrados
    3. Calcular el total de la compra
    4. Mostrar productos que cumplan una condición (por ejemplo: mayores a cierto precio)
    5. salir 
      """)
    
    comando = input("Ingrese el número de la opción que desea ejecutar (o 'salir' para terminar): ")

    if comando == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        nuevo_producto = Producto(nombre_producto, precio_producto)
        ListaProductos1.agregar_producto(nuevo_producto)

        input("Presione Enter para continuar...")

    elif comando == "2":
        ListaProductos1.mostrar_productos()
        input("Presione Enter para continuar...")

    elif comando == "3":
        ListaProductos1.sumar_precios()
        input("Presione Enter para continuar...")

    elif comando == "4":
        precio = float(input("Ingrese el precio para filtrar los productos: "))
        ListaProductos1.productos_mayores_a_precio(precio)
        input("Presione Enter para continuar...")
        
    elif comando == "5" or comando.lower().strip() == "salir":
        print("Saliendo del programa...")
        break
    