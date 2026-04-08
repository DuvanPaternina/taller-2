# Main script for the application

class Producto():

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.lista_productos = []

    def agregar_producto(self, producto):
        pass

    def __str__(self):
        return f"{self.nombre} | ${self.precio}"
    

comando = ""
while True:
    print("""
    1. Permitir agregar productos a una lista
    2. Mostrar todos los productos registrados
    3. Calcular el total de la compra
    4. Mostrar productos que cumplan una condición (por ejemplo: mayores a cierto precio)
    5. salir 
      """)
    
    comando = input("Ingrese el número de la opción que desea ejecutar (o 'salir' para terminar): ")

    if comando == "1":
        pass
    elif comando == "2":
        pass
    elif comando == "3":
        pass
    elif comando == "4":
        pass
    elif comando == "5" or comando.lower().strip() == "salir":
        print("Saliendo del programa...")
        break