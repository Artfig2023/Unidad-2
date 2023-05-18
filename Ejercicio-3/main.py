from ClaseMenu import Menu

if __name__ == '__main__':
    menuprinc = Menu()

    bandera = False
    while not bandera:
        print('Menu principal')
        print('------------------')
        print('1- Mostrar dia y hora de menor y mayor valor.\n2- Mostrar temperatura promedio mensual por hora.\n3- Listar datos de dia.\n0- Salir.')
        opc = input('Opcion: ')
        menuprinc.opcion(opc)
        bandera = opc == '0'