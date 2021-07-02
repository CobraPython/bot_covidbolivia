import os,sys
import pandas as pd
import numpy as np
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)      


# La corrección para llevar los indicadores a 100 000 habitantes.
_n=115.131 

#datos casos diarios
df_casos=pd.read_csv('covid19-bolivia-udape/confirmados_diarios.csv',sep=',',header=0,index_col=0).fillna(0)

# correccion para llevarlo a corrección cada 100 000 hab por cada departamento. 
# se usa una relación proporcional de población

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




nac = casos[0]+casos[1]+casos[2]+casos[3]+casos[4]+casos[5]+casos[6]+casos[7]+casos[8]
mean_nac = mean_casos[0]+mean_casos[1]+mean_casos[2]+mean_casos[3]+mean_casos[4]+mean_casos[5]+mean_casos[6]+mean_casos[7]+mean_casos[8]

bol = mpimg.imread('bol.jpg')
imagebox = OffsetImage(bol,zoom=1)
firma = AnnotationBbox(imagebox,(len(y)/2,30))



fig = plt.figure(figsize=(50,30))

#Color del fondo
fig.patch.set_facecolor(tableau20[0])
plt.axes().patch.set_facecolor(tableau20[0])

plt.subplots_adjust(top=0.80)
plt.title('\nNUEVOS CASOS/DÍA POR 100\'000 HAB A NIVEL NACIONAL'+'\n(último reporte en fuente: '+y[-1]+')\n',fontsize=70,fontproperties=prop,color=tableau20[1])
plt.plot(y,nac/_n,label='Nuevos Casos/día',linewidth=5,color=tableau20[2],linestyle='-',marker='.',markersize=15,markeredgecolor='yellow' ,markerfacecolor='y')
plt.plot(y,mean_nac/_n,label='Promedio 7 días',linewidth=8,color=tableau20[3],linestyle='-')
plt.legend(loc='upper left',fontsize=50)

plt.yticks(fontsize=50,fontproperties=prop,color=tableau20[1])
plt.xticks(y[::30],fontsize=35,rotation=45,fontproperties=prop,color=tableau20[1])

#plt.ylim(0,np.max(nacional2_)+5) 
#plt.xlim(0,y[-1])  

plt.ylabel('Casos/día',fontsize=60,fontproperties=prop,color=tableau20[1])
plt.gca().yaxis.grid(linestyle='--',linewidth=1,dashes=(5,15))
plt.gca().spines["top"].set_visible(False)    
plt.gca().spines["bottom"].set_visible(False)    
plt.gca().spines["right"].set_visible(False)    
plt.gca().spines["left"].set_visible(False)  
plt.gca().get_xaxis().tick_bottom()    
plt.gca().get_yaxis().tick_left()
plt.gca().add_artist(firma)
plt.subplots_adjust(bottom=0.2)
plt.text(0,-1/3*np.max(nac/_n),"Data source: https://www.udape.gob.bo/index.php?option=com_wrapper&view=wrapper&Itemid=104" 
       "\nAutor: Telegram Bot: @Bolivian_Bot"    
       "\nNota: Curva de nuevos casos/día ajustada a 100 000 hab",fontsize=35,fontproperties=prop,color=tableau20[1]); 
plt.savefig('imagenes/covNac.png')


