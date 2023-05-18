from ClaseConjunto import Conjunto

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__conj1 = None
        self.__conj2 = None

    def inicializa(self):
        print("Cargar conjunto nro 1")
        elems = input("Ingrese elementos separados por coma: ")
        elems = elems.split(',')
        for i in range(len(elems)):
            int(elems[i])
        self.__conj1 = Conjunto(elems)
        print('Se ha cargado el primer conjunto.')
        print("Cargar conjunto nro 2")
        elems = input("Ingrese elementos separados por coma: ")
        elems = elems.split(',')
        for i in range(len(elems)):
            int(elems[i])
        self.__conj2 = Conjunto(elems)
        print('Se ha cargado el segundo conjunto.')

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        nuevoconj = self.__conj1 + self.__conj2
        print('Resultado de la union.')
        nuevoconj.muestra()

    def opcion2(self):
        nuevoconj = self.__conj1 - self.__conj2
        print('Resultado de la diferencia.')
        nuevoconj.muestra()

    def opcion3(self):
        self.__conj1.muestra()
        self.__conj2.muestra()
        if self.__conj1 == self.__conj2:
            print('Los conjuntos son iguales.')
        else:
            print('Los conjuntos no son iguales.')

    def salir(self):
        print('Salio del programa.')