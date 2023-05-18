class PlanAhorro:
    __codigoplan = ''
    __modelo = ''
    __version = ''
    __valor= 0.0
    cantcuotas = 60
    cantcuotaslic = 15

    def __init__(self,codplan,mod,vers,valor):
        self.__codigoplan = codplan
        self.__modelo = mod
        self.__version = vers
        if type(valor) is float:
            self.__valor = valor

    def getValor(self):
        return self.__valor
    def __str__(self):
        return 'Codigo: ' + self.__codigoplan + '/ Modelo: ' + self.__modelo + '/ Version: ' + self.__version + '/ Valor: ' + str(self.__valor)
    def setValor(self,nuevoval):
        if type(nuevoval) is float:
            self.__valor = nuevoval
            print('Valor actualizado.')
        else:
            print('Error. El valor no es del tipo de dato correspondiente.')

    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantcuotas
    @classmethod
    def getCantCuotasLicit(cls):
        return cls.cantcuotaslic