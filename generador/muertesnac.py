import os,sys
import pandas as pd
import numpy as np
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)      


# La corrección para llevar los indicadores a 100 000 habitantes.
_n=115.131 

#datos casos diarios
df_muertes=pd.read_csv('covid19-bolivia-udape/decesos_diarios.csv',sep=',',header=0,index_col=0).fillna(0)

muertes = df_muertes.iloc[:,:].values.T
y=df_muertes.index.values    #con el indice dado por las fechas del reporte

mdf_muertes = df_muertes.rolling(7,min_periods=1).mean()
mean_muertes = mdf_muertes.iloc[:,:].values.T 

nac_muertes = muertes[0]+muertes[1]+muertes[2]+muertes[3]+muertes[4]+muertes[5]+muertes[6]+muertes[7]+muertes[8]
mean_nac_muertes = mean_muertes[0]+mean_muertes[1]+mean_muertes[2]+mean_muertes[3]+mean_muertes[4]+mean_muertes[5]+mean_muertes[6]+mean_muertes[7]+mean_muertes[8]


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
             #2[1]   blanco de titulos
             #3[2]    rojo neon puntos
            
             #4[3]    verdes
             #5[4]    ROJO
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)   


bol = mpimg.imread('bol.jpg')
imagebox = OffsetImage(bol,zoom=1)
firma = AnnotationBbox(imagebox,(len(y)/2,1))



fig = plt.figure(figsize=(50,25))

#Color del fondo
fig.patch.set_facecolor(tableau20[0])
plt.axes().patch.set_facecolor(tableau20[0])

plt.subplots_adjust(top=0.80)
plt.title('\nFallecimientos/día por 100\'000 Hab a nivel Nacional'+'\n(último reporte en fuente: '+y[-1]+')\n',fontsize=70,fontproperties=prop,color=tableau20[1])
plt.plot(y,nac_muertes/_n,label='Nuevos Casos/día',linewidth=3,color=tableau20[3],linestyle='-',marker='.',markersize=5,markeredgecolor='yellow' ,markerfacecolor='y')
plt.plot(y,mean_nac_muertes/_n,label='Promedio 7 días',linewidth=8,color=tableau20[4],linestyle='-')
plt.legend(loc='upper left',fontsize=50)
plt.yticks(fontsize=50,fontproperties=prop,color=tableau20[1])
plt.xticks(y[::30],fontsize=35,rotation=45,fontproperties=prop,color=tableau20[1])
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
plt.text(0,-1*np.max(nac_muertes/_n)/2.8,"Data source: https://github.com/mauforonda/covid19-bolivia"    
       "\nAutor: Telegram Bot: @Bolivian_Bot"    
       "\nNota: Curva de fallecimientos/día ajustada a 100 000 hab",fontsize=35,fontproperties=prop,color=tableau20[1]); 
plt.savefig('imagenes/muertesNac.png')
