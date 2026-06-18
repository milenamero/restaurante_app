class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    def __str__(self):
        return f"{self._nombre} - ${self._precio}"