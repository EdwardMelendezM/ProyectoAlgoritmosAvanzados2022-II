import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from claseGenetico import *
from claseGeneticoHibridoGreedy import *
from sklearn import preprocessing


def ordenar_lista_curso(lista):
  lista_dias1=['LUNES','MARTES','MIÉRCOLES','JUEVES','VIERNES','SÁBADO','SABADO ']
  lista_order=[]
  for dia in lista_dias1:
    for k in range(len(lista)):
      #print(dia)
      if lista[k][0]==dia:
        lista_order.append(lista[k])
  return lista_order

def orden_codigo(dataset):
  #print(dataset)
  unicos=dataset['CODIGO'].unique()
  #print(unicos)
  lista_horario=[]
  for u in unicos: #recorremos los valores unicos encontrados
    lista_unica=[]
    for _ in range(len(dataset)):#recorremos todo el data set
      if u==dataset.iloc[_,1]:#verificamos 
        lista_unica.append([dataset.iloc[_,9],dataset.iloc[_,10],dataset.iloc[_,11],dataset.iloc[_,5]])
    #verificamos la lista unica y ordenamos
    #print(lista_unica)
    lista_unica=ordenar_lista_curso(lista_unica)
    #print(lista_unica)
    lista_horario.append(lista_unica)
  return(lista_horario)


def buscar_codigo_docent(dataset):
  #print(dataset)
  unicos=dataset['CODIGO'].unique()
  #print(unicos)
  lista_do=[]
  for u in unicos: #recorremos los valores unicos encontrados de codigos
    for _ in range(len(dataset)):#recorremos todo el data set
      if u==dataset.iloc[_,1]:#verificamos 
        lista_do.append([u,dataset.iloc[_,3],dataset.iloc[_,15]])
  return(lista_do)


def unir_listas(prof,horario):
  lista_unida=[]
  tam=0
  k=0
  for i in horario:
    print(tam)
    lista_unida=prof[tam]+horario[k]
    tam=tam+len(i)
    k=k+1
    print(lista_unida)

#qr nombre docente y codigo
#w horarios cada uno tiene un elemento
def unir_listas(prof,horario):
  lista_unida=[]
  tam=0
  k=0
  for i in horario:
    lista_unir=prof[tam]+[horario[k]]
    tam=tam+len(i)
    k=k+1
    lista_unida.append(lista_unir)
  return(lista_unida)


def convertir_objetos(lista_unida):
  totalCursos=[]
  for i in lista_unida1:
    horario=[]
    #print(i)
    for k in range(len(i[3])):
      horario.append(ClaseDia(i[3][k][0],i[3][k][1],i[3][k][2],i[3][k][3]))
    totalCursos.append(ClaseCurso(i[0],i[1],i[2],horario))
  return(totalCursos)


#------------------------ INPUT PRINCIPAL --------------------------------
dataset = pd.read_csv("cargaAcademica.csv",sep=';')
len(dataset)
dataset_copy = dataset.loc[dataset['CARRERA'] == 'INGENIERIA INFORMATICA']
dataset_copy=dataset_copy.loc[dataset_copy['DOCENTES']!='CURSO DESACTIVADO']

w=orden_codigo(dataset_copy)
sum=0
qr=buscar_codigo_docent(dataset_copy)
unir_listas(qr,w)
lista_unida1=unir_listas(qr,w)
cursos=convertir_objetos(lista_unida1)
print(cursos)