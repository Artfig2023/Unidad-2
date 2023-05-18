from ClaseManejadorAlumno import Manejador_Alumno
from ClaseManejadoMateria import Manejador_Materia
from ClaseMenu import Menu

if __name__ == "__main__":
    arreglo = Manejador_Alumno.inicializar()
    manejadorAlumno = Manejador_Alumno(arreglo)
    # print("\n")
    lista = Manejador_Materia.inicializar()
    manejadorMateria = Manejador_Materia(lista)

    Menu(manejadorMateria, manejadorAlumno)