class cliente:
    def __init__(self, dnii, apellidoo, nombree, tel, patentee, vehic, estadoo):
        self.__dni=dnii 
        self.__apellido = apellidoo
        self.__nombre = nombree
        self.__telefono = tel
        self.__patente = patentee
        self.__vehiculo = vehic 
        self.__estado = estadoo
    def getDNI(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTel(self):
        return self.__telefono
    def getNomCompleto(self):
        return self.__apellido + " " + self.__nombre
    def getPatente(self):
        return self.__patente
    def getVehiculo(self):
        return self.__vehiculo
    def cambiaE(self):
        self.__estado = 'T'
        print("Estado cambiado con exito")
    def __eq__(self, otro): ##SOBRECARGA DE OPERADOR (==)
        propio = str(self.__dni) + str(self.__nombre) + str(self.__apellido) + str(self.__telefono)
        otro = str(otro.getDNI()) + str(otro.getNombre()) + str(otro.getApellido()) + str(otro.getTel())
        if propio == otro:
            v = True
        else:
            v= False
        return v