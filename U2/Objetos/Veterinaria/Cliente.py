class Cliente:
    def __init__(self, id, nombre, ant, mascota):
        self._id = id
        self._nombre = nombre
        self._antiguedad = ant
        self._mascota = mascota
    
    def __str__(self) -> str:
        return f'{self.id:8}|{self.nombre:^20}|{self.antiguedad:^3}\n{self.mascota}'
    
    
    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def antiguedad(self):
        return self._antiguedad
    @property
    def mascota(self):
        return self._mascota
    
    flag = 1
    @id.setter
    def id(self, nuevo):
        self._id = nuevo
    @nombre.setter
    def nombre(self, nuevo):
        self._nombre = nuevo
    @antiguedad.setter
    def antiguedad(self, nuevo):
        self._antiguedad = nuevo
    @mascota.setter
    def mascota(self, nuevo):
        self._mascota = nuevo
    
    def getEdadMascota(self):
        return self.mascota.edad
