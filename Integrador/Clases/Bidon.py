from Carga import Carga
class Bidon(Carga):
    def __init__(self, contenido, capacidad, densidad) -> None:
        super().__init__(contenido)
        self._capacidad = capacidad
        self._densidad = densidad

    def __str__(self) -> str:
        return super().__str__() + self._capacidad + " " + self._densidad
    
    @property
    def peso(self):
        return self._capacidad * self._densidad