from Atencion import Atencion

class Farmacia(Atencion):
    def __init__(self, codigo, tdc, importe, dto) -> None:
        super().__init__(codigo, tdc)
        self._importe = importe
        self._descuento = dto

    @property
    def importe(self):
        return self._importe
    @property
    def descuento(self):
        return self._descuento
    
    def importeACobrar(self):
        importeFinal = self.importe - self.descuento
        importeFinal *= 1.3 if self._tipo_de_cobro == 2 else 0.95
        return importeFinal
    
    def __str__(self) -> str:
        return super().__str__() + f'{self.importe} | {self.descuento} | {self.importeACobrar()}'