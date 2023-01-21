from claseGenetico import *
import matplotlib.pyplot as plt

# GENERAR LOS DATOS DE LOS DOCENTES Y HORARIOS EN UNA LISTA
# EL TIEMPO DE EJECUCION DE LOS DOS ALGORITMOS


#Cursos iniciales
cursoNuevo = ClaseCurso("MAT",
                        "matematica",
                        "Jacob",
                        [ClaseDia("lunes",7,9),ClaseDia("miercoles",7,9),ClaseDia("viernes",7,8)])
cursoNuevo2 = ClaseCurso("FIS",
                        "fisica",
                        "Maria",
                        [ClaseDia("martes",7,9),ClaseDia("jueves",7,9),ClaseDia("viernes",7,8)])
cursoNuevo3 = ClaseCurso("ALG",
                        "fisica",
                        "Juan",
                        [ClaseDia("lunes",9,11),ClaseDia("miercoles",9,11),ClaseDia("viernes",8,9)])
cursoNuevo4 = ClaseCurso("BIO",
                        "fisica",
                        "Pilar",
                        [ClaseDia("lunes",12,15),ClaseDia("jueves",11,1),ClaseDia("viernes",9,10)])
cursoNuevo5 = ClaseCurso("ANAT",
                        "anatomia",
                        "Ana",
                        [ClaseDia("lunes",16,18),ClaseDia("miercoles",16,18),ClaseDia("viernes",16,15)])



#Inicializamos la clase genetico
totalCursos=[cursoNuevo,cursoNuevo2,cursoNuevo3,cursoNuevo4,cursoNuevo5]
var = claseGenetico(_cursos=5,_aulas=2,_n=250,_listaCursos=totalCursos)

#Damos el valor para iterar las generaciones
generaciones = 100

#Generamos la primera poblacion
var.generarPoblacion()
aux=1

#--------------------------------------------------------------
#Empezamos con las iteraciones
while aux<generaciones:
    #Entrenamos nuestra poblacion con cada iteracion
    var.entrenar()
    if(var.puntuacion[-1]==1.0):
        break
    aux+=1
#--------------------------------------------------------------

# Ver datos
y=var.obtenerPuntuacion()
x=[i for i in range(1,len(y)+1)]
print("---- Generado correctamente")


plt.plot(x,y)
plt.show()