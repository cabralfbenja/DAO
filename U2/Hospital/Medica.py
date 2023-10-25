from Atencion import Atencion
from Paciente import *

class Medica(Atencion):
    def __init__(self, codigo, tdc, paciente, importe) -> None:
        super().__init__(codigo, tdc)
        self._paciente = paciente
        self._importe = importe
    
    @property
    def paciente(self):
        return self._paciente
    @property
    def importe(self):
        return self._importe
    
    def importeACobrar(self):
        importeFinal = self._importe
        if self.paciente.habitual:
            importeFinal *= 0.75
        importeFinal *= 1.2 if self.tipo_de_cobro == 2 else 0.9
        return importeFinal
    
    def es_medica(self):
        return True
    
    def __str__(self) -> str:
        return super().__str__() + f'| {self.importeACobrar()}'