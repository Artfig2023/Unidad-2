from ClasePlanAhorro import PlanAhorro
import csv

class ManejadorPlanes:

    def __init__(self):
        self.__listaPlanes = []

    def agregaPlan(self, plan):
        self.__listaPlanes.append(plan)

    def testPlanes(self):
        archivo = open('Planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unPlan = PlanAhorro(fila[0],fila[1],fila[2],float(fila[3]))
                self.agregaPlan(unPlan)
        archivo.close()
        print('Se han cargado los planes de ahorro')

    def listarVehiculoMasBaratoValor(self):
        print('Listar vehiculos con valor inferior al dado.')
        valor = int(input('Ingrese valor:'))
        for i in range(len(self.__listaPlanes)):
            if self.__listaPlanes[i].getValor() < valor:
                print(self.__listaPlanes[i])

    def actualizarValorVehiculo(self):
        for i in range(len(self.__listaPlanes)):
            print(self.__listaPlanes[i])
            nuevovalor = float(input('Ingrese nuevo valor de vehiculo: '))
            self.__listaPlanes[i].setValor(nuevovalor)
            print('------------------------------------')

    def montoPagarLicitar(self):
        print('Monto a pagar para licitar cada vehiculo.')
        for i in range(len(self.__listaPlanes)):
            print('Vehiculo nro. {}'.format(i+1))
            print(self.__listaPlanes[i])
            importecuota = self.__listaPlanes[i].getValor() / PlanAhorro.getCantidadCuotas()
            print('Monto a pagar para licitar el vehiculo: %.2f' % (PlanAhorro.getCantCuotasLicit() * importecuota))