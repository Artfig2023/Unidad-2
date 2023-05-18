class Viajero:
    __numvia = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self,num,docu,nomb,ape,millas):
        self.__numvia = int(num)
        self.__dni = docu
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas_acum = int(millas)

    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def canjearMillas(self,millascanje):
        if type(millascanje) is int:
            if millascanje <= self.__millas_acum:
                self.__millas_acum -= millascanje
            else:
                print('Error. Millas insuficientes para canjear')
        else:
            print('Error. Dato incorrecto')
        return self.__millas_acum

    def __str__(self):
        return 'Numero de viajero: ' + str(self.__numvia) + '/ DNI: ' + self.__dni + '/  Nombre: ' + self.__nombre + '/  Apellido: ' + self.__apellido + '/  Millas acumuladas: ' + str(self.__millas_acum)

    def getNumeroViajero(self):
        return self.__numvia

    def __add__(self, cmill):
        return Viajero(self.__numvia, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + cmill)

    def __radd__(self, xcantmill):
        return Viajero(self.__numvia, self.__dni, self.__nombre, self.__apellido, xcantmill + self.__millas_acum)

    def __sub__(self, cantmill):
        return Viajero(self.__numvia, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - cantmill)

    def __rsub__(self, xcantmill):
        return Viajero(self.__numvia, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - xcantmill)

    def __gt__(self, segunviaj):
        if self.__millas_acum > segunviaj.cantidadTotaldeMillas():
            return True
        else:
            return False

    def __eq__(self, xcantmill):
        if self.__millas_acum == xcantmill:
            return True
        else:
            return False