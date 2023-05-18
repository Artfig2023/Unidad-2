from ClaseEmail import Email
from ClaseManejador import ManejadorEmails

def test():
    print('Funcion test.')
    print('Ingreso de un mail por partes.')
    print('id de cuenta: "marcoszarate15", dominio: "hotmail", tipo de dominio: "com", contrasenha: "marzarte77"')
    mailtest = Email('marcoszarate15','hotmail','com','marzarte77')
    print('Mail creado: {}'.format(mailtest.retornaEmail()))
    print('------------------------------------')
    print('Ingreso de un mail completo.')
    print('Mail ingresado: "lucreciamartinez88@gmail.com"')
    mailtest2 = Email('','','','')
    mailtest2.crearCuenta('lucreciamartinez88@gmail.com')
    print('Mail creado: {}'.format(mailtest2.retornaEmail()))
    print('------------------------------------')
    print('------- Fin Test -------')

if __name__ == '__main__':
    test()
    ### Inciso 1
    nombre = input('Ingrese su nombre:')
    print('Ingrese su email por partes.')
    idc = input('Ingrese id de cuenta:')
    dom = input('Ingrese dominio:')
    tipodom = input('Ingrese tipo de dominio:')
    contra = input('Ingrese contrasenha:')
    unEmail = Email(idc, dom, tipodom, contra) ### Crea la instancia con los datos
    print('Estimado/a {} te enviaremos tus mensajes a la direccion {}'.format(nombre, unEmail.retornaEmail()))
    ### Inciso 2
    unEmail.modificaContrasenha()
    ### Inciso 3
    em = input('Ingrese su email:')
    otroEmail = Email('', '', '', '') ### Nota: se puede enviar palabras en blanco (entre comillas simples)
    otroEmail.crearCuenta(em)
    print('Email: {}'.format(otroEmail.retornaEmail()))
    ### Inciso 4
    me = ManejadorEmails()
    me.CargaEmails()
    idc = input('Ingrese id de cuenta a buscar:')
    me.IndicaRepetido(idc)