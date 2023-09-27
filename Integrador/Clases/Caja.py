from Carga import Carga
class Caja(Carga):
    def __init__(self, contenido, peso) -> None:
        super().__init__(contenido)
        self._peso = peso

    @property 
    def peso(self):
        return self._peso
    
    def __str__(self) -> str:
        return super().__str__() + str(self.peso)