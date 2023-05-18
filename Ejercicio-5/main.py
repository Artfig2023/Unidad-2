from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()

    bandera = False
    while not bandera:
        print('\nMenu Principal')
        print('\n1- Actualizar el valores.\n2- Mostrar vehiculos con valor inferior.')
        print('3- Mostrar monto a pagar para licitacion.\n4- Modificar cantidad de cuotas pagas.')
        print('0- Salir')
        opc = input('Opcion: ')
        menu.opcion(opc)
        bandera = opc == '0'