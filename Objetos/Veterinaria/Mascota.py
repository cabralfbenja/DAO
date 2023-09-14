class Mascota:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    
    def __str__(self) -> str:
        return f'Mascota: {self.nombre:^20}|{self.edad:^3}'
    

    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad

    

    @nombre.setter
    def nombre(self, nuevo):
        self._nombre = nuevo
    @edad.setter
    def edad(self, nuevo):
        self._edad = nuevo
