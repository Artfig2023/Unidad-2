from claseCliente import cliente
from claseReparacion import reparacion
from manejadorCliente import manejadorCliente
from manejadorRep import manejadorRep

if __name__ == '__main__':
    mC = manejadorCliente()
    mR = manejadorRep()
    mC.cargaArchivo()
    mR.cargaArchivo()
    
    opcion = 1
    while opcion != 0:
        print("-----MENU-----")
        print("1_ Datos y reparaciones de un cliente ")
        print("2_ Ver reparaciones de una patente ")
        print("3_ Listar clientes a los que no se le ha realizado aun la reparacion")
        print("4_ Clientes que le hacen servicio a mas de un vehiculo")
        print("0_ Para finalizar")
        opcion = int(input())
        if(opcion == 1):
            dni = input("Ingrese dni del cliente: ")
            mC.opcion1(dni, mR)
        elif(opcion == 2):
            pat = input("Ingrese la patente: ")
            mR.opcion2(pat, mC)
        elif(opcion == 3):
            mR.opcion3(mC)
        elif(opcion==4):
            mC.opcion4()
        else:
            print("Opcion Mal Ingresada ")