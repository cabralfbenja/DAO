class Atencion:
    def __init__(self, codigo, tdc) -> None:
        self._codigo = codigo
        self._tipo_de_cobro = tdc
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def tipo_de_cobro(self):
        return self._tipo_de_cobro
    
    def __str__(self) -> str:
        return f'{self.codigo} | {self.tipo_de_cobro} '
    
    def es_medica(self):
        return False
    
    def importeACobrar():
        pass