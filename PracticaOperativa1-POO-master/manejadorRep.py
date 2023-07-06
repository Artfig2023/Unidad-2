import csv
from claseReparacion import reparacion
class manejadorRep:
    def __init__(self):
        self.__listaRep = []
    def agrega(self, rep):
        self.__listaRep.append(rep)
    def getListaa(self):
        return self.__listaRep
    def cargaArchivo(self):
        archivo = open('reparaciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nuevaRep = reparacion(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.agrega(nuevaRep)
    
    def cont_opcion1(self, patente):
        total=0
        for i in range(len(self.getListaa())): ##CICLO FOR UTILIZADO DEBIDO A QUE SI ENCUENTRA LO BUSCADO DEBE SEGUIR ITERANDO
            if patente == self.getListaa()[i].getPatente():
                subtotal= int(self.getListaa()[i].getPrecioRep()) + int(self.getListaa()[i].getPrecioMano())
                total += subtotal
                print("Reparacion       Precio repuesto         Mano de obra            Subtotal")
                print(f"{self.getListaa()[i].getReparacion()}     {self.getListaa()[i].getPrecioRep()}                      {self.getListaa()[i].getPrecioMano()}         {subtotal}")
        print(f"Total = {total}")
    def opcion2(self, patente, manejadorC):
        centinela = True
        for i in range(len(self.getListaa())):  ##CICLO FOR UTILIZADO DEBIDO A QUE SI ENCUENTRA LO BUSCADO DEBE SEGUIR ITERANDO
            if patente == self.getListaa()[i].getPatente() and self.getListaa()[i].getEstado() == 'T':
                manejadorC.cambiaEstado(patente)
                tot =  int(self.getListaa()[i].getPrecioRep()) + int(self.getListaa()[i].getPrecioMano())
                print(f"{tot}")
                centinela = False 
        if centinela:
            print(f"El auto con pantente: {patente} aun no esta listo")
    def opcion3(self, manejadorC):
        for i in range(len(self.getListaa())): ####CICLO FOR UTILIZADO DEBIDO A QUE SI ENCUENTRA LO BUSCADO DEBE SEGUIR ITERANDO
            if self.getListaa()[i].getEstado() == 'P':
                manejadorC.cont_opcion3(self.getListaa()[i].getPatente())
                print(f"Reparacion: {self.getListaa()[i].getReparacion()}")
        
                
                