import csv
from claseCliente import cliente
class manejadorCliente:
    def __init__(self):
        self.__listaCliente = []
    def getListaa(self):
        return self.__listaCliente
    def agrega(self, cliente):
        self.__listaCliente.append(cliente)
    def cargaArchivo(self):
        archivo = open('clientes.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nuevoCliente = cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            self.agrega(nuevoCliente)
    def opcion1(self, DNI, manejadorR):
        centinela = True
        i = 0
        while i < len(self.getListaa()) and centinela:
            if self.getListaa()[i].getDNI() == DNI:
                print(f"DNI: {DNI}                       Apellido y Nombre: {self.getListaa()[i].getNomCompleto()}")
                print(f"Patente: {self.getListaa()[i].getPatente()}             Vehiculo: {self.getListaa()[i].getVehiculo()}")
                manejadorR.cont_opcion1(self.getListaa()[i].getPatente())
                centinela = False
            i+=1
        if centinela:
            print("No se encontro cliente con ese numero de dni")
    def cambiaEstado(self, pat):
        i=0
        centinela = True
        while i < len(self.getListaa()) and centinela:
            if self.getListaa()[i].getPatente() == pat:
                self.getListaa()[i].cambiaE()
                print(f"{self.getListaa()[i].getNomCompleto()}")
                print(f"{self.getListaa()[i].getTel()}")
                print(f"{self.getListaa()[i].getVehiculo()}")
                centinela = False
            i+=1
            
    def cont_opcion3(self, patente):
        centinela = True
        i=0
        while i < len(self.getListaa()) and centinela:
            if self.getListaa()[i].getPatente() == patente:
                print(f"Apellido y nombre: {self.getListaa()[i].getNomCompleto()} Tel: {self.getListaa()[i].getTel()}")
                print(f"Patente: {patente}              Vehiculo: {self.getListaa()[i].getVehiculo()}")
                centinela = False
            i+=1
                
    def opcion4(self):
         for i in range(len(self.getListaa())):  ##CICLO FOR ANIDADO UTILIZADO DEBIDO A QUE DEBE COMPARAR TODAS LAS POSIBILIDADES, AUNQUE ENCUENTRE LO BUSCADO DEBE SEGUIR ITERANDO
             for k in range(len(self.getListaa())):
                 if self.getListaa()[i] == self.getListaa()[k] and i != k:
                    print(f"{self.getListaa()[i].getDNI()}")
                    print(f"{self.getListaa()[i].getNomCompleto()}")
                    print(f"{self.getListaa()[i].getTel()}")
                    print(f"{self.getListaa()[i].getPatente()}")
                    print(f"{self.getListaa()[i].getVehiculo()}")
                    
                    
                