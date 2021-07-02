
"""
En este script se recrean los datos obtenidos
de UDAPE, actualizado por los datos del gobierno.

De inicio se usaran las tablas dadas en el repositorio
pero se buscara en el futuro construir todo.

"""

import os,sys
import pandas as pd
import numpy as np
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)      


# La corrección para llevar los indicadores a 100 000 habitantes.
_n=115.131 

#datos casos diarios
df_casos=pd.read_csv('covid19-bolivia-udape/confirmados_diarios.csv',sep=',',header=0,index_col=0).fillna(0)
dep=['Chuquisaca','La Paz','Cochabamba','Oruro','Potosí','Tarija','Santa Cruz','Beni','Pando']

# correccion para llevarlo a corrección cada 100 000 hab por cada departamento. 
# se usa una relación proporcional de población
n_dep = _n*(1/100)*np.array([5.78,27.03,17.52,4.92,8.23,4.81,26.42,4.19,1.10])  #el porcentaje

casos = df_casos.iloc[:,:].values.T
y=df_casos.index.values    #con el indice dado por las fechas del reporte

mdf_casos = df_casos.rolling(7,min_periods=1).mean()
mean_casos = mdf_casos.iloc[:,:].values.T 

import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib import font_manager as fm, rcParams

fpath = os.path.join(r'MonoLisaSimpson-Regular.ttf')
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(48,48,48), (240,240,240), (59,170,6), (61,167,249),    
             (230,0,0)]    

             #1[0] fondo plomo
             #2    blanco de titulos
             #3    rojo neon puntos
             #4    verdes
             #5    celestes
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)   



for i in range(len(dep)):
    fig = plt.figure(figsize=(50,30))
    #Color del fondo
    fig.patch.set_facecolor(tableau20[0])
    plt.axes().patch.set_facecolor(tableau20[0])
    plt.subplots_adjust(top=0.80)
    plt.title('\nNuevos casos/día cada 100\'000 HAB en el Dep.:\n'+dep[i]+'\n(último reporte en fuente: '+y[-1]+')\n',fontsize=75,fontproperties=prop,color=tableau20[1])
    for j in range(9):
        if dep[j]!=dep[i]:
            plt.plot(y,mean_casos[j]/n_dep[j],label=dep[j],linewidth=2,linestyle='-')
        else:
            pass
    plt.plot(y,mean_casos[i]/n_dep[i],label='Promedio 7 días '+dep[i],linewidth=6,color=tableau20[2],linestyle='-')
 
    plt.setp(plt.legend(loc='upper left',fontsize=40).get_lines(), linewidth=6)
    plt.yticks(fontsize=50,fontproperties=prop,color=tableau20[1])
    plt.xticks(y[::30],fontsize=40,rotation=45,fontproperties=prop,color=tableau20[1])
   # plt.ylim(0,2*np.max(var_mc[i]))  
    plt.ylabel('\nCasos/día\n',fontsize=60,fontproperties=prop,color=tableau20[1])
    plt.gca().yaxis.grid(linestyle='--',linewidth=1,dashes=(5,15))
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False)  
    plt.gca().get_xaxis().tick_bottom()    
    plt.gca().get_yaxis().tick_left()
    plt.subplots_adjust(bottom=0.2)
    plt.text(0,-18,"Data source: https://www.udape.gob.bo/index.php?option=com_wrapper&view=wrapper&Itemid=104"    
       "\nAutor: Telegram Bot: @Bolivian_Bot"    
       "\nNota: Curva de nuevos casos/día ajustada a 100 000 hab",fontsize=30,fontproperties=prop,color=tableau20[1]);
    plt.savefig('imagenes/casos_cov_'+dep[i]+'.png');
 