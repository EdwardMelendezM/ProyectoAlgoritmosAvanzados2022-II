class classDia:
    def __init__(self,dia,horaI,horaF):
        self.dia=dia
        self.horaI=horaI
        self.horaF=horaF

class classCurso:
    def __init__(self,codAsignatura,nombre,docente,horario):
        self.codAsignatura=codAsignatura
        self.nombre=nombre
        self.docente=docente
        self.horario=horario
        
def determinarHorarios(curso):
    aula=[]
    dias={"lunes":0,"martes":1,"miercoles":2,"jueves":3,"viernes":4,"sabado":5}
    numero=0
    for curso in curso.horario:
        for num in range(curso.horaI,curso.horaF):
            aula.append((dias[curso.dia],num))
            numero+=1
    return numero,aula

def generarAuxAulas(listaCursos):
    diccionario={}
    for valor in listaCursos:
        diccionario[valor.codAsignatura]=-1
    return diccionario

def generarAuxDocentes(listaCursos):
    diccionario={}
    for valor in listaCursos:
        diccionario[valor.codAsignatura]=valor.docente
    return diccionario

def determinarSiEntraCurso(cromosoma,listaCursos):
    aulasDisponibles=[]
    auxAulasDisponibles=[]
    for aula in cromosoma:
        aulaExtra=[]
        auxAula=generarAuxAulas(listaCursos)
        for indice in range(len(aula)):
            auxCodAsignatura=listaCursos[indice].codAsignatura
            if(aula[indice]==0):
                auxAula[auxCodAsignatura]=0
            else:
                numero,tupla=determinarHorarios(listaCursos[indice])
                auxAula[auxCodAsignatura]=numero
                aulaExtra+=tupla
        aulasDisponibles.append(aulaExtra)
        auxAulasDisponibles.append(auxAula)
    return aulasDisponibles,auxAulasDisponibles
def cantidadRepetidos(lista):
    return dict(zip(lista,map(lambda x: lista.count(x),lista)))

# Encontrar los cursos repetidos en un mismo aula
def ECT(cromosoma):
    castigo=0
    aulasTuplas,auxlasDicc=determinarSiEntraCurso(cromosoma,listaCursos)
    for valor in aulasTuplas:
        diccionario=cantidadRepetidos(valor)
        for key in diccionario:
            if(diccionario[key]>1):
                castigo+=1
    return castigo

# Calcular los cursos que se repiten en otras aulas
def ECDAT(cromosoma):
    castigo=0
    primero=cromosoma[0]
    for x in range(len(cromosoma)):
        for y in range(len(cromosoma[x])):
            if(cromosoma[x][y]==1):
                for z in range(len(cromosoma)):
                    if(cromosoma[z][y]==1 and z!=x):
                        castigo+=1
    return castigo//2



L=[[1,0,0,0],[1,0,0,1],[1,0,1,0],[0,0,1,1]]
#print(ECDAT(L))

def EPT():
    pass


#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------    ANALISIS DEL PROBLEMA    --------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
l=[[[0,1,0],[1,1,0]]  ,  [[1,0,0],[0,0,0]]]
#     Cromosoma 1     ,     Cromosoma 2

#  Aula-1  ,   Aula-2
#[[0,1,0,1],[1,1,0,1]] Cromosoma
listaCursos=[classCurso("MAT","matematica","Jose",[classDia("lunes",7,9),classDia("miercoles",7,9),classDia("viernes",7,8)]),
            classCurso("FIS","fisica","Manuel",[classDia("martes",7,9),classDia("miercoles",7,9)]),
            classCurso("BIO","biologia","Ana",[classDia("lunes",9,11),classDia("miercoles",9,11),classDia("viernes",8,9)]),
            classCurso("ALG","algebra","Jose",[classDia("martes",9,11),classDia("jueves",9,11),classDia("viernes",9,10)])
            ]

#[[0,1,0,1],[1,1,0,1]] Cromosoma



cromosoma=[[0,1,0,0],[1,1,0,1],[1,1,0,1]]
#print(ECT(cromosoma))

print(generarAuxDocentes(listaCursos))


aula1=[(0,0),(0,1),(2,0),(2,1),(4,0),(1,0),(1,1),(2,0),(2,1),(0,2),(0,3),(2,2),(2,3)]
aula2=[(0,0),(0,1),(2,0),(2,1),(4,0)]
aula3=[(1,0),(1,1),(2,0),(2,1)]

auxAula1={"MAT":5,"FIS":4,"BIO":4}
auxAula2={"MAT":5,"FIS":0,"BIO":0}
auxAula2={"MAT":0,"FIS":4,"BIO":0}



if():
    pass