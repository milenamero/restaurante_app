from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self._productos = []
        self._clientes = []
    def agregar_producto(self, producto):
        self._productos.append(producto)
    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)
    def mostrar_info(self):
        print("\n--- Menú ---")
        for p in self._productos: print(p)
        print("\n--- Clientes ---")
        for c in self._clientes: print(c)