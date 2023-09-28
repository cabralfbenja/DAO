class Paciente:
    def __init__(self, nombre, sintoma, habitual) -> None:
        self._nombre = nombre
        self._sintoma = sintoma
        self._habitual = habitual

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def sintoma(self):
        return self._sintoma
    
    @property
    def habitual(self):
        return self._habitual
    
    def __str__(self) -> str:
        return f'{self.nombre} | {self.sintoma:} | {self.habitual}'
    