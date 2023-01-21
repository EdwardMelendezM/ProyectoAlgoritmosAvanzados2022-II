from claseGenetico import *
from claseGeneticoHibridoGreedy import *
import matplotlib.pyplot as plt

#Paul
# GENERAR LOS DATOS DE LOS DOCENTES Y HORARIOS EN UNA LISTA

#Andy
# EL TIEMPO DE EJECUCION DE LOS DOS ALGORITMOS


#Cursos iniciales
cursoNuevo = ClaseCurso("MAT",
                        "matematica",
                        "Jacob",
                        [ClaseDia("lunes",7,9,"teo"),ClaseDia("miercoles",7,9,"lab"),ClaseDia("viernes",7,8,"teo")])
cursoNuevo2 = ClaseCurso("FIS",
                        "fisica",
                        "Maria",
                        [ClaseDia("martes",7,9,"teo"),ClaseDia("jueves",7,9,"lab"),ClaseDia("viernes",7,8,"teo")])
cursoNuevo3 = ClaseCurso("ALG",
                        "fisica",
                        "Juan",
                        [ClaseDia("lunes",9,11,"teo"),ClaseDia("miercoles",9,11,"lab"),ClaseDia("viernes",8,9,"teo")])
cursoNuevo4 = ClaseCurso("BIO",
                        "fisica",
                        "Pilar",
                        [ClaseDia("lunes",12,15,"teo"),ClaseDia("jueves",11,1,"lab"),ClaseDia("viernes",9,10,"teo")])
cursoNuevo5 = ClaseCurso("ANAT",
                        "anatomia",
                        "Ana",
                        [ClaseDia("lunes",16,18,"teo"),ClaseDia("miercoles",16,18,"lab"),ClaseDia("viernes",16,15,"teo")])



#Inicializamos la clase genetico
totalCursos=[cursoNuevo,cursoNuevo2,cursoNuevo3,cursoNuevo4,cursoNuevo5]
var = claseGeneticoHibridoGreedy(_cursos=len(totalCursos),_aulas=3,_n=250,_listaCursos=totalCursos,_cantLaboratorios=2)

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