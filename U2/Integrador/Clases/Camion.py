from Carga import *

class Camion:
    def __init__(self, patente, carga_max) -> None:
        self._patente = patente
        self._estado = "Disponible"
        self._carga_maxima = carga_max
        self._cargas = []

    def __str__(self) -> str:
        return f'{self.patente: 7} | {self.estado:15} | {self.carga_maxima: 5} | {self.peso_cargas(): 5}'
    
    @property
    def patente(self):
        return self._patente
    @property
    def estado(self):
        return self._estado
    @property
    def carga_maxima(self):
        return self._carga_maxima
    @property
    def cargas(self):
        return self._cargas
    @estado.setter
    def estado(self, nuevo): self._estado = nuevo

    def subirCarga(self, nueva_carga):
        if(self.chequear_peso(nueva_carga.peso + self.peso_cargas())):
            self._cargas.append(nueva_carga)
        else:
            print("No se puede cargar... hay sobrepeso")
    def bajarCarga(self, carga):
        if(self.estado == "Disponible" and carga in self._cargas):
            self._cargas.remove(carga)
        else:
            print("Opcion no válida...")

    def peso_cargas(self):
        total = 0
        for carga in self.cargas:
            total += carga.peso
        return total

    def a_reparacion(self):
        self.estado("En reparación")
    
    def sale_reparado(self):
        self.estado("Disponible")
    
    def partir(self):
        if(self.listoParaPartir):
            self.en_viaje()
        else:
            print("No puede partir...")
    def en_viaje(self):
        self.estado("De viaje")

    def de_regreso(self):
        self.estado("De regreso")
    
    def chequear_peso(self, peso):
        return peso < self.carga_maxima

    def cantidad_de_cargas(self):
        return len(self.cargas)
    
    def listarCargas(self):
        cadena = ""
        for carga in self.cargas:
            cadena += str(carga) + "\n"
        return cadena
    
    def listoParaPartir(self):
        return self.estado == "Disponible" and (self.peso_cargas() > self.carga_maxima * 0.75)