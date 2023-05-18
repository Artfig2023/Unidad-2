class Conjunto:
    __elementos = None
    def __init__(self,elem):
        if type(elem) is list:
            self.__elementos = elem
        else:
            print('Error de parametros.')

    def getTamanho(self):
        return len(self.__elementos)

    def getElementos(self):
        return self.__elementos

    def muestra(self):
        print(self.__elementos)

    def __add__(self, xconj2):
        nuevoconj = self.__elementos.copy()
        i = 0
        while i < len(nuevoconj):
            cont = nuevoconj.count(nuevoconj[i])
            while cont > 1:
                nuevoconj.remove(nuevoconj[i])
                cont -= 1
            i += 1
        for j in range(xconj2.getTamanho()):
            i = 0
            ban = False
            while i < len(nuevoconj) and ban == False:
                if xconj2.getElementos()[j] == nuevoconj[i]:
                    ban = True
                else:
                    i += 1
            if ban == False:
                nuevoconj.append(xconj2.getElementos()[j])
        return Conjunto(nuevoconj)

    def __sub__(self, xconj2):
        nuevoconj = []
        for i in range(len(self.__elementos)):
            j = 0
            ban = False
            while j < xconj2.getTamanho() and not ban:
                if self.__elementos[i] == xconj2.getElementos()[j]:
                    ban = True
                else:
                    j += 1
            if ban == False:
                nuevoconj.append(self.__elementos[i])
        return Conjunto(nuevoconj)



    def __eq__(self, xconj2):
        tconj1 = len(self.__elementos)
        tconj2 = xconj2.getTamanho()
        self.__elementos.sort()
        xconj2.getElementos().sort()
        i = j = 0
        ban = True
        if tconj1 == tconj2:
            while i < tconj1 and ban:
                if self.__elementos[i] == xconj2.getElementos()[j]:
                    i += 1
                    j += 1
                else:
                    ban = False
        else:
            ban = False

        return ban