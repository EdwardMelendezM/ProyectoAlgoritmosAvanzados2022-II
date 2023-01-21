import random as rd
from operator import itemgetter
from random import randint, random
from claseCurso import *
from claseDia import *

class claseGeneticoHibridoGreedy():
    def __init__(self,_cursos,_aulas,_n,_listaCursos:list,_cantLaboratorios):
        self.probaMutacion=0.80
        self.probaCruce=0.5
        self.poblacion=None
        self.individuo=None
        self.evaluar=None
        self.fo=None
        self.puntuacion=[]
        self.cursos=_cursos
        self.aulas=_aulas
        self.n=_n
        self.listaCursos=_listaCursos
        self.laboratorios=None
        self.cantidadLaboratorios=_cantLaboratorios

    #Generamos un individuo
    def generarIndividuo(self):
        individuo=[[rd.randint(0,1) for k in range(self.cursos)] for j in range(self.aulas)]
        return individuo
    
    #Generamos la poblacion de individuos
    def generarPoblacion(self):
        self.poblacion=[self.generarIndividuo() for i in range(self.n)]
    #[ [[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]],
    #  [[0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1, 0, 0]] ]
    
    #[ AULAS , AULAS , AULAS , AULAS , AULAS ]
    #[ [0,1,0,1,0,1] ] , [0,1,0,1,0,1] , [0,1,0,1,0,1] ]
    #[[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]]
    def determinarHorariosLaboratorios(self,curso):
        aula=[]
        dias={"lunes":0,"martes":1,"miercoles":2,"jueves":3,"viernes":4,"sabado":5}
        lab=[]
        for curso in curso.horario:
            for num in range(curso.horaI,curso.horaF):
                if(curso.tipo=="lab"):
                    lab.append((dias[curso.dia],num))
                else:
                    aula.append((dias[curso.dia],num))
        return lab,aula

    def generarAuxDocentes(self):
        diccionario={}
        for valor in self.listaCursos:
            diccionario[valor.docente]=-1
        return diccionario

    def determinarSiEntraCurso(self,cromosoma):
        aulasDisponibles=[]
        labosDisponibles=[]
        for aula in cromosoma:
            aulaExtra=[]
            labExtra=[]
            for indice in range(len(aula)):
                if(aula[indice]==0):
                    continue
                else:
                    laboratorioBinario,aulasBinario=self.determinarHorariosLaboratorios(self.listaCursos[indice])
                    labExtra+=laboratorioBinario
                    aulaExtra+=aulasBinario
            aulasDisponibles.append(aulaExtra)
            labosDisponibles.append(labExtra)
        return aulasDisponibles,labosDisponibles
    def cantidadRepetidos(self,lista):
        return dict(zip(lista,map(lambda x: lista.count(x),lista)))

    # Encontrar los cursos que se cruzan horas en un mismo aula y laboratorio
    def ECT(self,cromosoma):
        def contarCastigos(aulasDisponibles):
            if(len(aulasDisponibles) in [0,1]):
                return 0
            castigo=0
            for valor in aulasDisponibles:
                diccionario=self.cantidadRepetidos(valor)
            for key in diccionario:
                if(diccionario[key]>1):
                    castigo+=1
            return castigo
        castigoTotal=0
        aulasDisponibles,labosDisponibles=self.determinarSiEntraCurso(cromosoma)
        castigoTotal+=contarCastigos(aulasDisponibles)
        #[[(0, 16), (0, 17)], [(1, 7), (1, 8), (4, 7), (0, 9), (0, 10), (4, 8), (0, 16), (0, 17)], [(0, 16), (0, 17)]]
        totalLabos=[]
        for valor in labosDisponibles:
            totalLabos+=valor
        reparticionDeLabos=[totalLabos[i:i + self.cantidadLaboratorios] for i in range(0, len(totalLabos), self.cantidadLaboratorios)]
        for valor in reparticionDeLabos:
            castigoTotal+=contarCastigos(valor)
        return castigoTotal

    # Calcular los cursos que se repiten en otras aulas
    def ECDAT(self,cromosoma):
        castigo=0
        primero=cromosoma[0]
        for x in range(len(cromosoma)):
            for y in range(len(cromosoma[x])):
                if(cromosoma[x][y]==1):
                    for z in range(len(cromosoma)):
                        if(cromosoma[z][y]==1 and z!=x):
                            castigo+=1
        return castigo//2


    #[[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]]
    #Paul

    def funcionObjetivo(self,cromosoma):
        #[[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]]
        #return 1/(1+randint(1,5)+randint(1,5))
        return 1/(1+self.ECT(cromosoma)+2*self.ECDAT(cromosoma))


    # USAR EL ALGORITMO GREEDY PARA SELEECIONAR LA SOLUCION OPTIMA
    def AlgoritmoGreddy(self,pais): #SELECCION DE RULETA
        valores = list(zip(*pais))
        #[(0.09090909090909091, 0.2), ([[1, 1, 1, 0, 1], [1, 0, 1, 1, 0], [0, 0, 1, 0, 1]], [[1, 1, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1]])]
        mejorValor2=-999
        mejorPos2=0
        mejorValor = -999
        mejorPos=0
        for indice in range(len(valores[0])):
            if(mejorValor<valores[0][indice]):
                if(valores[0][indice])==1.0:
                    mejorValor=valores[0][indice]
                    mejorPos=indice
                    break
                mejorValor=valores[0][indice]
                mejorPos=indice
        for indice in range(len(valores[0])):
            if(mejorValor2<valores[0][indice] and indice!=mejorPos):
                if(valores[0][indice])==1.0:
                    mejorValor2=valores[0][indice]
                    mejorPos2=indice
                    break
                mejorValor2=valores[0][indice]
                mejorPos2=indice


        #Recuperamos el indice de la molecula mas apto
        indice_padre = mejorPos

        #Recuperamos el indice de la segunda molecula mas apto
        indice_madre = mejorPos2

        #Recuperamos el valor con el indice
        padre = valores[1][indice_padre]
        madre = valores[1][indice_madre]
        
        return padre, madre
    def evaluacion(self):
        self.evaluar=[(self.funcionObjetivo(valor),valor) for valor in self.poblacion if(self.funcionObjetivo(valor)<=1)]
                    #   (  FuncionObjetivo(valor),valor)
                    #   (            121         , [[1, 0, 1], [0, 1, 1]])
                    #   (            88          , [[1, 0, 1], [0, 1, 1]])
        
        #Ordenar
        sorted(self.evaluar , key=itemgetter(0))

        puntuacion=0
        # ----------- ALMACENANDO LA PUNTUACION DE CADA GENERACION -----------
        for valor in self.evaluar:
            puntuacion+=valor[0]
        self.puntuacion.append(puntuacion/len(self.evaluar))

        # --------------------- CRUCE -----------------------
        hijos=[]
        # Itearamos cada hijo
        while(len(hijos)<self.n):
            #Almacenamos las moleculas mas aptas en padre y madre
            padre,madre=self.AlgoritmoGreddy(self.evaluar)

            #Generamos un numero entre 0 y 1 con "radom()" y si es menor a la
            #probabilidad de cruce -> Cruzamos padre y madre
            if(self.probaCruce>random()):
                for i in range(len(padre)):
                    for j in range(self.cursos//2):
                        madre[i][j]=padre[i][j]
            hijos.append(madre)

        #------------------ MUTACION ---------------------
        for individuo in hijos:
            #Hacemos lo mismo de cruce, generamos un random y lo comparamos con
            #la probabilidad de MUTACION
            if(self.probaMutacion>random()):
                indice_aleatorio=randint(0, len(individuo)-1)
                indice_aleatorioBinario=randint(0, len(individuo[indice_aleatorio])-1)
                #aQUI CAMBIAMOS LOS BIT Si es 0 a 1   y   de 1 a 0
                if individuo[indice_aleatorio][indice_aleatorioBinario] == 1:
                    individuo[indice_aleatorio][indice_aleatorioBinario] = 0
                else:
                    individuo[indice_aleatorio][indice_aleatorioBinario] = 1
        self.poblacion=hijos
        None==madre==padre==hijos
    def info(self):
        print("")
        print("------------ INFO ------------")
        print(f'Tam de cursos: {self.cursos}')
        print(f'Tam de aulas : {self.aulas}')
        print(f'Tam de pobl  : {self.n}')
        print(f'Puntuacion   : {self.puntuacion}')
        print("-----------------------------")
        
    def entrenar(self):
            self.evaluacion()
    def obtenerPoblacion(self):
        return self.poblacion
    def obtenerPuntuacion(self):
        return self.puntuacion
