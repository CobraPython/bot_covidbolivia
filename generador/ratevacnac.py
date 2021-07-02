import os,sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

_n=115.131 # factor de correción para llevar a 10^4 hab

#datos vacunacion
df1=pd.read_csv('vacunas/datos/primera.csv',sep=',').sort_values(by='fecha').set_index('fecha').fillna(0)
df2=pd.read_csv('vacunas/datos/segunda.csv',sep=',').sort_values(by='fecha').set_index('fecha').fillna(0)

#ambas concentraciones de datos tienen distintos etiquetados.
#se replican los ordenes en distintos vectores.
#bdep_v=['Beni','Chuquisaca','Cochabamba','La Paz','Oruro','Pando','Potosi','Santa Cruz','Tarija']
c_dep = _n*(1/10)*np.array([4.19,5.78,17.52,27.03,4.92,1.10,8.23,26.42,4.81])  #el porcentaje

y=df1.index.values       #Se recuperaron los datos de la fuente

v_v1 = df1.rolling(7,min_periods=1).mean()
v_v2 = df2.rolling(7,min_periods=1).mean()
mv_v1 = v_v1.iloc[:,:].values.T   
mv_v2 = v_v2.iloc[:,:].values.T   

mm_v1=np.zeros((9,len(mv_v1[0])))
mm_v2=np.zeros((9,len(mv_v2[0])))

for j in range(9):
    mm_v1[j,0]=mv_v1[j,0]/c_dep[j]
    mm_v2[j,0]=mv_v2[j,0]/c_dep[j]
    for i in range(1,len(mv_v1[0])):
        mm_v1[j,i]=(mv_v1[j,i]-mv_v1[j,i-1])/c_dep[j]
        mm_v2[j,i]=(mv_v2[j,i]-mv_v2[j,i-1])/c_dep[j]


from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib import font_manager as fm, rcParams

fpath = os.path.join(r'MonoLisaSimpson-Regular.ttf')
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]


# These are the "Tableau 20" colors as RGB.    
tableau20 = [(48,48,48), (240,240,240), (59,170,6), (61,167,249),    
             (230,0,0)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)   

vac1 = mm_v1[0]+mm_v1[1]+mm_v1[2]+mm_v1[3]+mm_v1[4]+mm_v1[5]+mm_v1[6]+mm_v1[7]+mm_v1[8]
vac2 = mm_v2[0]+mm_v2[1]+mm_v2[2]+mm_v2[3]+mm_v2[4]+mm_v2[5]+mm_v2[6]+mm_v2[7]+mm_v2[8]

bol = mpimg.imread('bol.jpg')
imagebox = OffsetImage(bol,zoom=1)
firma = AnnotationBbox(imagebox,(len(y)/2,280))



fig = plt.figure(figsize=(50,30))

#Color del fondo
fig.patch.set_facecolor(tableau20[0])
plt.axes().patch.set_facecolor(tableau20[0])

plt.subplots_adjust(top=0.80)
plt.title('\nTasa de vacunación cada 10\'000 Hab a nivel Nacional:'+'\n(último reporte en fuente: '+y[-1]+')\n',fontsize=75,fontproperties=prop,color=tableau20[1])
plt.plot(y,np.abs(vac1),label='Promedio 7 días',linewidth=4,color=tableau20[3],linestyle='-')
plt.plot(y,vac2,label='Promedio 7 días',linewidth=4,color=tableau20[2],linestyle='-')

plt.yticks(fontsize=60,fontproperties=prop,color=tableau20[1])
plt.xticks(y[::7],fontsize=50,rotation=45,fontproperties=prop,color=tableau20[1])
plt.ylabel('\nVacunados/día\n',fontsize=60,fontproperties=prop,color=tableau20[1])
plt.gca().yaxis.grid(linestyle='--',linewidth=1,dashes=(5,15))
plt.gca().spines["top"].set_visible(False)    
plt.gca().spines["bottom"].set_visible(False)    
plt.gca().spines["right"].set_visible(False)    
plt.gca().spines["left"].set_visible(False)  
plt.gca().get_xaxis().tick_bottom()    
plt.gca().get_yaxis().tick_left()
plt.gca().add_artist(firma)
plt.subplots_adjust(bottom=0.2)
plt.text(len(mv_v1[0]), vac1[-1],'1er\nDosis',fontsize=30,color=tableau20[3])
plt.text(len(mv_v2[0]), vac2[-1],'2da\nDosis',fontsize=30,color=tableau20[2])
    

plt.text(0,-1.35*np.max(vac2),"Data source: https://www.udape.gob.bo/index.php?option=com_wrapper&view=wrapper&Itemid=104" 
       "\nAutor: Telegram Bot: @Bolivian_Bot"    
       "\nNota: Curva de vacunas/día ajustada a 10 000 hab",fontsize=35,fontproperties=prop,color=tableau20[1]); 
plt.savefig('imagenes/ratevacnac.png')

