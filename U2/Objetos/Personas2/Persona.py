class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self._documento = documento
        self._nombre = nombre
        self._apellido = apellido
        self._edad = int(edad)
    def __str__(self):
        return f"{self.documento:8}|{self.nombre:20}|{self.apellido:20}|{self.edad:2}"
    @property
    def documento(self): return self._documento
    @property
    def nombre(self): return self._nombre
    @property
    def apellido(self): return self._apellido
    @property
    def edad(self): return self._edad

    @documento.setter
    def documento(self, nuevo): self._documento = nuevo
    @nombre.setter
    def nombre(self, nuevo): self._nombre = nuevo
    @apellido.setter
    def apellido(self, nuevo): self._apellido = nuevo
    @edad.setter
    def edad(self, nuevo): self._edad = nuevo


    def esMayor(self):
        return self._edad >= 18
    def nombreConVocal(self):
        return self._nombre[0] in "AEIOU"
    def apellidoConVocal(self):
        return self._apellido[0] in "AEIOU"