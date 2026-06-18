from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar():
    resto = Restaurante()
    resto.agregar_producto(Producto("Pizza", 12.50))
    resto.registrar_cliente(Cliente("Juan", "001"))
    resto.mostrar_info()

if __name__ == "__main__":
    ejecutar()