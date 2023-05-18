from ClaseViajero import Viajero
import csv

class ManejadorViajeros:

    def __init__(self):
        self.__listaViajeros = []

    def test(self):
        print('Funcion test.')
        print('Carga de un viajero frecuente.')
        print('Numero de viajero: "18776" , DNI: "177013", Nombre: "Adrian", Apellido: "Paez", Millas acumuladas: "982"')
        testviajero = Viajero('18876','177013','Adrian','Paez','982')
        print('Viajero cargado.')
        print(testviajero)
        print('------- Fin Test -------')

    def agregaViajero(self,viajero):
        self.__listaViajeros.append(viajero)

    def cargaViajeros(self):
        archivo = open('Viajeros.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unViajero = Viajero(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                self.agregaViajero(unViajero)
        archivo.close()
        print('Se han cargado los viajeros frecuentes.')

    def buscaViajero(self,num):
        ban = -1
        i = 0
        while i < len(self.__listaViajeros) and ban == -1:
            if self.__listaViajeros[i].getNumeroViajero() == num:
                ban = i
            else:
                i += 1
        return ban

    def mostrarViajeros(self):
        print('Listado de viajeros frecuentes:')
        for i in range(len(self.__listaViajeros)):
            print(self.__listaViajeros[i])

    def MuestraMillas(self,ind):
        return self.__listaViajeros[ind].cantidadTotaldeMillas()

    def AcumulaMillas(self,ind,xcant):
        if type(xcant) is int:
            viajero = xcant + self.__listaViajeros[ind]
            print('Resultado de operacion:')
            print(viajero)
            self.__listaViajeros[ind] = viajero
        else:
            print('Error. Parametros incorrectos.')

    def CanjeaMillas(self,ind,xcant):
        if type(xcant) is int:
            if self.__listaViajeros[ind].cantidadTotaldeMillas() > xcant:
                viajero = xcant - self.__listaViajeros[ind]
                print('Resultado de operacion:')
                print(viajero)
                self.__listaViajeros[ind] = viajero
            else:
                print('Error. Millas insuficientes')
        else:
            print('Error. Parametros incorrectos.')

    def ComparaMillasViajero(self,xind,xcant):
        if type(xcant) is int:
            if self.__listaViajeros[xind] == xcant:
                print('Cantidad de millas iguales')
            else:
                print('Cantida de millas diferentes')
            if xcant == self.__listaViajeros[xind]:
                print('Cantidad de millas iguales')
            else:
                print('Cantidad de millas diferente')
        else:
            print('Error. Parametros incorrectos.')