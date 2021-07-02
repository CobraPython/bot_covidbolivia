""" En este script se obtienen algunos datos 
rápidos  """


import os, sys
import pandas as pd 
import numpy as np 


_n=115.131

df_1=pd.read_csv('covid19-bolivia-udape/confirmados_diarios.csv',sep=',',header=0,index_col=0).fillna(0)
df_2=pd.read_csv('covid19-bolivia-udape/decesos_diarios.csv',sep=',',header=0,index_col=0).fillna(0)
df_3=pd.read_csv('covid19-bolivia-udape/recuperados_diarios.csv',sep=',',header=0,index_col=0).fillna(0)
dep_cov = ['Chuquisaca','La Paz','Cochabamba','Oruro','Potosí','Tarija','Santa Cruz','Beni','Pando']
y_cov = df_1.index.values

df_4=pd.read_csv('vacunas/datos/primera.csv',sep=',',header=0,index_col=0).fillna(0)
df_5=pd.read_csv('vacunas/datos/segunda.csv',sep=',',header=0,index_col=0).fillna(0)
dep_vac = ['Beni','Chuquisaca','Cochabamba','La Paz','Oruro','Pando','Potosi','Santa Cruz','Tarija']
c_dep = _n*(1/10)*np.array([4.19,5.78,17.52,27.03,4.92,1.10,8.23,26.42,4.81])  #el porcentaje
y_vac = df_4.index.values



casos = df_1.iloc[:,:9].values.T
muertes= df_2.iloc[:,:9].values.T
recuperados= df_3.iloc[:,:9].values.T

vac1= df_4.iloc[:,:9].values.T
vac2= df_5.iloc[:,:9].values.T

v1=np.zeros((9,len(vac1[0])))
v2=np.zeros((9,len(vac2[0])))

for j in range(9):
    v1[j,0]=(vac1[j,0])
    v2[j,0]=(vac2[j,0])
    for i in range(1,len(v1[0])):
        v1[j,i]=(vac1[j,i]-vac1[j,i-1])
        v2[j,i]=(vac2[j,i]-vac2[j,i-1])

print(v1[0])

#dep_cov = ['Chuquisaca','La Paz','Cochabamba','Oruro','Potosí','Tarija','Santa Cruz','Beni','Pando']
#dep_vac = ['Beni','Chuquisaca','Cochabamba','La Paz','Oruro','Pando','Potosi','Santa Cruz','Tarija']

#Los datos estan limpios y ordenados, siendo la posición [0] el inicio de acopio de datos
#lo que se debe ordenar la secuencia de departamentos, es distinta en cada dataset

#Vamos a guardar de una sola forma dep_cov

    
estados = np.array([[dep_cov[0],casos[0,-1],muertes[0,-1],recuperados[0,-1],v1[1,-1],v2[1,-1]],
         [dep_cov[1],casos[1,-1],muertes[1,-1],recuperados[1,-1],v1[3,-1],v2[3,-1]],
         [dep_cov[2],casos[2,-1],muertes[2,-1],recuperados[2,-1],v1[2,-1],v2[2,-1]],
         [dep_cov[3],casos[3,-1],muertes[3,-1],recuperados[3,-1],v1[4,-1],v2[4,-1]],
         [dep_cov[4],casos[4,-1],muertes[4,-1],recuperados[4,-1],v1[6,-1],v2[6,-1]],
         [dep_cov[5],casos[5,-1],muertes[5,-1],recuperados[5,-1],v1[8,-1],v2[8,-1]],
         [dep_cov[6],casos[6,-1],muertes[6,-1],recuperados[6,-1],v1[7,-1],v2[7,-1]],
         [dep_cov[7],casos[7,-1],muertes[7,-1],recuperados[7,-1],v1[0,-1],v2[0,-1]],
         [dep_cov[8],casos[8,-1],muertes[8,-1],recuperados[8,-1],v1[5,-1],v2[5,-1]],
         ['Nacional',np.sum(casos[:,-1]),np.sum(muertes[:,-1]),np.sum(recuperados[:,-1]),np.round(np.sum(v1[:,-1]),2),np.round(np.sum(v2[:,-1]),2)]])

fechas = [y_cov[-1],y_vac[-1]]

np.save('estados.npy',estados)        #Guarda las últimas fechas donde se llenaron las fuentes. 
np.save('fechas.npy',fechas)        #Guarda las últimas fechas donde se llenaron las fuentes. 

