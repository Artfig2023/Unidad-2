class Ventana:
    __titulo = ''
    __xsupizq = 0
    __ysupizq = 0
    __xinfder = 0
    __yinfder = 0

    def __init__(self,tit='',xsi=0,ysi=0,xid=500,yid=500):
        self.__titulo = tit
        if type(xsi) is int:
            self.__xsupizq = xsi
        else:
            print('Error de parametro xsi.')
        if type(ysi) is int:
            self.__ysupizq = ysi
        else:
            print('Error de parametro ysi.')
        if type(xid) is int:
            self.__xinfder = xid
        else:
            print('Error de parametro xid.')
        if type(yid) is int:
            self.__yinfder = yid
        else:
            print('Error de parametro yid.')
        self.normaliza()

    def normaliza(self):
        while self.__xsupizq < 0:
            self.__xsupizq += 50
        while self.__ysupizq < 0:
            self.__ysupizq += 50
        while self.__xinfder > 500:
            self.__xinfder -= 500
        while self.__yinfder > 500:
            self.__yinfder -= 500
        while self.__xsupizq > self.__xinfder:
            self.__xsupizq -= self.__xinfder
        while self.__ysupizq > self.__yinfder:
            self.__ysupizq -= self.__yinfder

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return '(' + str(self.__xsupizq) + ',' + str(self.__ysupizq) + ')'

    def ancho(self):
        return '(' + str(self.__xinfder) + ',' + str(self.__yinfder) + ')'

    def moverDerecha(self,unidad=1):
        if type(unidad) is int:
            self.__xsupizq -= unidad
            self.__xinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def moverIzquierda(self,unidad=1):
        if type(unidad) is int:
            self.__xsupizq -= unidad
            self.__xinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def bajar(self,unidad=1):
        if type(unidad) is int:
            self.__ysupizq -= unidad
            self.__yinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def subir(self,unidad=1):
        if type(unidad) is int:
            self.__ysupizq += unidad
            self.__yinfder -= unidad
        else:
            print('Error de paraemtro unidad.')
        self.normaliza()

    def mostrar(self):
        print('X superior izquierdo:{}'.format(self.__xsupizq))
        print('Y superior izquierdo:{}'.format(self.__ysupizq))
        print('X inferior derecho:{}'.format(self.__xinfder))
        print('Y inferior derecho:{}'.format(self.__yinfder))