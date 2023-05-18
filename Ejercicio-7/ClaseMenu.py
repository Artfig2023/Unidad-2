from ClaseManejador import ManejadorViajeros

class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
        self.__mv = ManejadorViajeros()
        self.__mv.test()
        self.__mv.cargaViajeros()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion invalida.'))
        func()

    def opcion1(self):
        print('Comparar millas')
        numviaj = int(input('Ingrese numero de viajero:'))
        ind = self.__mv.buscaViajero(numviaj)
        if ind == -1:
            print('Error. Viajero no encontrado.')
        else:
            cant = int(input('Ingrese cantidad de millas para comparar:'))
            self.__mv.ComparaMillasViajero(ind, cant)

    def opcion2(self):
        print('Acumular millas.')
        numviaj = int(input('Ingrese numero de viajero:'))
        ind = self.__mv.buscaViajero(numviaj)
        if ind == -1:
            print('Error. Viajero no encontrado.')
        else:
            cant = int(input('Ingrese cantidad de millas a acumular:'))
            self.__mv.AcumulaMillas(ind,cant)

    def opcion3(self):
        print('Canjear millas.')
        numviaj = int(input('Ingrese numero de viajero:'))
        ind = self.__mv.buscaViajero(numviaj)
        if ind == -1:
            print('Error. Viajero no encontrado.')
        else:
            cant = int(input('Ingrese cantidad de millas a canjear:'))
            self.__mv.CanjeaMillas(ind, cant)

    def salir(self):
        print('Salio del programa.')