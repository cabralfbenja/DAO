from Atencion import Atencion
from Paciente import Paciente

class Hospital:
    def __init__(self, rs) -> None:
        self._razon_social = rs
        self._atenciones = []
    
    @property
    def razon_social(self):
        return self.razon_social
    @property
    def atenciones(self):
        return self._atenciones
    
    def addAtencion(self, atencion):
        self._atenciones.append(atencion)
    
    def importe_total_atencion_consulta(self):
        atencionesMedicas = list(filter(lambda x: x.es_medica(), self.atenciones))
        suma = 0
        for atencion in atencionesMedicas:
            suma += atencion.importeACobrar()
        return suma


    def importe_promedio_atenciones(self, min, max):
        atencionesMedicas = list(filter(lambda x: x.es_medica(), self.atenciones))
        suma = 0
        cont = 0
        for atencion in atencionesMedicas:
            if atencion.importeACobrar() < max and atencion.importeACobrar() > min:
                suma += atencion.importeACobrar()
                cont += 1
        return round(suma/cont, 2) if cont > 0 else 0


    def codigo_primera_atencion_habitual(self):
        atencionesMedicasHabituales = list(filter(
                lambda x: (x.es_medica() and x.paciente.habitual), 
                self.atenciones))
        return atencionesMedicasHabituales[0].codigo if len(atencionesMedicasHabituales) else 0
        