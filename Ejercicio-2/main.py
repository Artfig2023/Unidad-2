from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()

    bandera = False
    while not bandera:
        print('Menu principal')
        print('1- Mostrar todos los viajeros.\n2- Ingresar a menu de viajero.\n0- Salir.')
        op = input('Seleccione opcion: ')
        menu.opcion(op)
        bandera = op == '0'