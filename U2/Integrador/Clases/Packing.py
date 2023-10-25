from Carga import Carga

class Packing(Carga):
    def __init__(self, contenido, peso_por_caja, cantidad, peso_estructura) -> None:
        super().__init__(contenido)
        self._peso_por_caja = peso_por_caja
        self._cantidad = cantidad
        self._peso_estructura = peso_estructura

    @property
    def peso(self):
        return (self._peso_por_caja * self._cantidad) + self._peso_estructura
    
    def __str__(self) -> str:
        return super().__str__() + str(self._peso_por_caja) + " " + str(self._cantidad) + str(self._peso_estructura)