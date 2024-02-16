##Demetrio Torres Yanahi

# Importar el módulo pyplot 
import matplotlib.pyplot as plt
import numpy as np

#Definir el conjuntos de valores de x 
xi = [0,1,2,3,4,5,6,7,8,9,10]

#Definir el conjunto de valores de y
yi = [0,1,4,9,16,25,36,49,64,81,100]

#Se generan los puntos de la gráfica con xi,yi
plt.plot(xi,yi)



# Agregar etiquetas 
plt.xlabel('Eje x')
plt.ylabel('Eje y')

#Agregar el título de la gráfica
plt.title('Gráfica de x^2')
#Guardamos la gráfica en formato png pero esto no es necesario
plt.savefig('x².png')
 

#Mostramos el gráfico
plt.grid(True)
plt.show()


