import random as rd
from operator import itemgetter
from random import randint, random
from claseCurso import *
from claseDia import *

class claseGenetico():
    def __init__(self,_cursos,_aulas,_n,_listaCursos:list):
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

    #Generamos un individuo
    def generarIndividuo(self):
        individuo=[[rd.randint(0,1) for k in range(self.cursos)] for j in range(self.aulas)]
        return individuo
    
    #Generamos la poblacion de individuos
    def generarPoblacion(self):
        self.poblacion=[self.generarIndividuo() for i in range(self.n)]
    #[ [[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]],
    #  [[0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1, 0, 0]] ]

    #Esta funcion nos sirve para seleecionar a aquellos que son
    #mas aptos.
    def NuevaRuleta(self,pais): #SELECCION DE RULETA
        def sortear(fitness_total, indice_a_ignorar=-1):
            ruleta, acumulado, valor_sorteado = [], 0, random()

            if indice_a_ignorar!=-1:
                fitness_total -= valores[0][indice_a_ignorar]

            for indice, i in enumerate(valores[0]):
                if indice_a_ignorar==indice: 
                    continue
                acumulado += i
                ruleta.append(acumulado/fitness_total)
                if ruleta[-1] >= valor_sorteado:
                    return indice
    
        valores = list(zip(*pais)) 
        
        fitness_total = sum(valores[0])

        #Recuperamos el indice de la molecula mas apto
        indice_padre = sortear(fitness_total) 

        #Recuperamos el indice de la segunda molecula mas apto
        indice_madre = sortear(fitness_total, indice_padre)

        #Recuperamos el valor con el indice
        padre = valores[1][indice_padre]
        madre = valores[1][indice_madre]
        
        return padre, madre
    
    #[ AULAS , AULAS , AULAS , AULAS , AULAS ]
    #[ [0,1,0,1,0,1] ] , [0,1,0,1,0,1] , [0,1,0,1,0,1] ]
    #[[1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]]
    def determinarHorarios(self,curso):
        aula=[]
        dias={"lunes":0,"martes":1,"miercoles":2,"jueves":3,"viernes":4,"sabado":5}
        numero=0
        for curso in curso.horario:
            for num in range(curso.horaI,curso.horaF):
                aula.append((dias[curso.dia],num))
                numero+=1
        return numero,aula

    def generarAuxAulas(self):
        diccionario={}
        for valor in self.listaCursos:
            diccionario[valor.codAsignatura]=-1
        return diccionario

    def generarAuxDocentes(self):
        diccionario={}
        for valor in self.listaCursos:
            diccionario[valor.docente]=-1
        return diccionario

    def determinarSiEntraCurso(self,cromosoma):
        aulasDisponibles=[]
        auxAulasDisponibles=[]
        for aula in cromosoma:
            aulaExtra=[]
            auxAula=self.generarAuxAulas()
            for indice in range(len(aula)):
                auxCodAsignatura=self.listaCursos[indice].codAsignatura
                if(aula[indice]==0):
                    auxAula[auxCodAsignatura]=0
                else:
                    numero,tupla=self.determinarHorarios(self.listaCursos[indice])
                    auxAula[auxCodAsignatura]=numero
                    aulaExtra+=tupla
            aulasDisponibles.append(aulaExtra)
            auxAulasDisponibles.append(auxAula)
        return aulasDisponibles,auxAulasDisponibles
    def cantidadRepetidos(self,lista):
        return dict(zip(lista,map(lambda x: lista.count(x),lista)))

    # Encontrar los cursos repetidos en un mismo aula
    def ECT(self,cromosoma):
        castigo=0
        aulasTuplas,auxlasDicc=self.determinarSiEntraCurso(cromosoma)
        for valor in aulasTuplas:
            diccionario=self.cantidadRepetidos(valor)
            for key in diccionario:
                if(diccionario[key]>1):
                    castigo+=1
        return castigo

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
    def evaluacion(self):
        self.evaluar=[(self.funcionObjetivo(valor),valor) for valor in self.poblacion if(0.1<self.funcionObjetivo(valor)<=1)]
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
            padre,madre=self.NuevaRuleta(self.evaluar)

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
