from Hospital import Hospital
from Medica import *
from Paciente import *

if __name__ == '__main__':

    h = Hospital("Privado")

    juan = Paciente("Juan", "fiebre", False)
    benja = Paciente("Benja", "fiebre", True)

    h.addAtencion(Medica(1, 1, juan, 5000))
    h.addAtencion(Medica(2, 1, benja, 2000))

    
    print()
    
    for atencion in h.atenciones:
        print(atencion)

    print(h.importe_total_atencion_consulta())
    print(h.importe_promedio_atenciones(1,10000))
    print(h.codigo_primera_atencion_habitual())
