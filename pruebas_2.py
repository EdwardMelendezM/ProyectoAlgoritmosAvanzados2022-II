import numpy as np
class ClaseDia:
    def __init__(self,_dia,_horaInicio,_horaFinal):
        self.dia=_dia
        self.horaInicio=_horaInicio
        self.horaFinal=_horaFinal
    def getDia(self):
        return self.dia
    def getHoraInicio(self):
        return self.horaInicio
    def getHoraFinal(self):
        return self.horaFinal
class ClaseCurso:
    def __init__(self,_idCurso,_nombre,_docente,_dia):
        self.idCurso=_idCurso
        self.nombre=_nombre
        self.docente=_docente
        self.dias = _dia
        self.aula=None


def ingresarDias(curso:ClaseCurso,matriz:list):
    castigo=0
    def determinarIndices(dia,horaInicio,horaFinal):
        diccionarioDias={"lunes":0,"martes":1,"miercoles":2,"jueves":3,"viernes":4,"sabado":5}
        return diccionarioDias[dia],horaInicio-7,horaFinal-8
    for valor in curso.dias:
        dia,horaI,horaF=determinarIndices(valor.dia,valor.horaInicio,valor.horaFinal)
        if(horaI!=horaF ):
            for num in range(horaI,horaF+1):
                matriz.append((dia,num))  
        else:
            matriz.append((dia,horaF))
    return matriz
cursoNuevo = ClaseCurso("INFO014",
                        "matematica",
                        "juanPipa",
                        [ClaseDia("lunes",7,9),ClaseDia("miercoles",7,9),ClaseDia("viernes",7,8)])
cursoNuevo2 = ClaseCurso("INFOM14",
                        "fisica",
                        "MariaPilar",
                        [ClaseDia("lunes",7,9),ClaseDia("jueves",7,9),ClaseDia("viernes",7,8)])
matrix=[]
ingresarDias(cursoNuevo,matrix)
ingresarDias(cursoNuevo2,matrix)
for valor in matrix:
    print(f"{valor}")
#  Dia,horaI,horaF
castigo=0
def count_repeated_elements(list,castigo):
    count = {}
    for i in list:
        count[i] = count.get(i, 0) + 1
    for key in count:
        if(count[key]==1):
            continue
        castigo+=1
    return castigo

print(count_repeated_elements(matrix,castigo))