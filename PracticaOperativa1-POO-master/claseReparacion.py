class reparacion:
    def __init__(self, patentee, repa, precioRep, precioM, estadoo):
        self.__patente=patentee
        self.__reparacion = repa
        self.__precioRep = precioRep
        self.__precioMano = precioM
        self.__estado = estadoo
    def getPatente(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getPrecioRep(self):
        return self.__precioRep
    def getPrecioMano(self):
        return self.__precioMano
    def getEstado(self):
        return self.__estado