import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.parsers import count_empty_vals
import numpy as np
import matplotlib.ticker as ticker
import statistics as stats

datos = pd.read_csv('datos_ordenados1.csv')
totalCantidad=[]
totalTiempo=[]
totalParticipacion=[]
listaOrdenadaTiempo=[]
ciudadParaGrafica=[]

conjuntoCiudades = list(set(datos['CIUDAD']))
ciudadesClasificadas = list(datos.groupby(['CIUDAD']))
cantidadDeporte=datos['CANTIDAD']
iteracion = 11
cantidadPersonasArriaga=[]

cantidadDeporteOrdenada = sorted(datos.CANTIDAD)
cantidad = list(set(cantidadDeporteOrdenada))


tiemposArriaga = sorted(ciudadesClasificadas[0][1].TIEMPO)
#agrupar datos por ciudad
for j in range(0,len(conjuntoCiudades)):
    suma=sum(ciudadesClasificadas[j][1].CANTIDAD)
    suma2=sum(ciudadesClasificadas[j][1].TIEMPO)
    suma3=sum(ciudadesClasificadas[j][1].ID)
    totalCantidad.append(suma)
    totalTiempo.append(suma2)
    totalParticipacion.append(suma3)
#termina agrupar datos por 


a=0
variable=[]
listaPromedio=[]

for i in range(0,len(ciudadesClasificadas[0][1])):
    a=tiemposArriaga.count(tiemposArriaga[i])
    variable.append(a)
    
for b in range(0,len(conjuntoCiudades)):
    listaPromedio.append(totalTiempo[b]/len(ciudadesClasificadas[b][1].CANTIDAD))

#obtener dos letras de las palabras
for i in range (0,len(conjuntoCiudades)):
    ciudadParaGrafica.append(conjuntoCiudades[i][0]+conjuntoCiudades[i][1])
ciudadParaGrafica.sort()
# termina obtener dos letras de las palabras
fig = plt.figure(figsize=(15,10))

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(1, len(conjuntoCiudades)+1):
        y = ciudadesClasificadas[i-1][1].TIEMPO
        ax =plt.subplot(3,5,i)
        ax.hist(y,bins,edgecolor='black')
        ax.axvline(round(stats.median(y),4), color='red', label='mediana',linewidth=7)
        ax.axvline(stats.mode(y),color='yellow',label='moda',linewidth=5)
        ax.axvline(listaPromedio[i-1],color='green', label='Media',linewidth=5)
        ax.legend()
        ax.set_xlabel('TIEMPO')
        ax.set_ylabel('CANTIDAD ')
        ax.set_title('Grafica '+str(ciudadesClasificadas[i-1][0]))
        plt.yscale('linear')
        #print(ciudadesClasificadas[i-1][1].CANTIDAD)

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ax =plt.subplot(3,5,11)
ax.bar(ciudadParaGrafica, listaPromedio)
ax.set_xlabel('CIUDAD')
ax.set_ylabel('PROMEDIO')
ax.set_title('Grafica')
plt.yscale('linear')            

listaOrdenadaTiempo = sorted(datos.TIEMPO)

rango = listaOrdenadaTiempo[len(listaOrdenadaTiempo)-1]-listaOrdenadaTiempo[0]
varianza = stats.variance(listaPromedio)

ax3 =plt.subplot(3,5,12)
ax3.text(0.2, .6, 'Rango: {0}'.format(rango), fontsize=20)
ax3.text(0.2, .8, 'Varianza: {0}'.format(varianza), fontsize=20)
ax3.axis('off')

plt.subplots_adjust(left=0.04,
                    bottom=0.067,
                    right=0.98,
                    top=0.95,
                    wspace=0.302,
                    hspace=0.393)

plt.show()