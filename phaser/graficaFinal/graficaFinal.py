import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

# Leer datos desde el archivo
with open('graficaMia.txt', 'r') as file:
    lines = file.readlines()

# Procesar los datos
data_bala1 = []
data_bala2 = []
targets_bala1 = []  # Lista para almacenar los targets de Bala 1
estatus_left_bala2 = [] 

for line in lines:
    # Verificar si la línea tiene datos antes de procesarla
    if line.strip():
        values = list(map(float, line.strip().split(',')))
        data_bala1.append(values[:3])  # Primeros tres valores para Bala 1
        data_bala2.append(values[3:])  # Últimos cuatro valores para Bala 2
        targets_bala1.append(values[2])  # Guardar el valor del target de Bala 1 (1 o 0)
        estatus_left_bala2.append(values[5])  

# Convertir las listas de datos a arrays de NumPy
data_bala1 = np.array(data_bala1)
data_bala2 = np.array(data_bala2)

# Crear un DataFrame con los targets de Bala 1
df_bala1 = pd.DataFrame({'Targets Bala 1': targets_bala1})

# Crear un DataFrame con el estatusLeft de Bala 2
df_bala2 = pd.DataFrame({'Estatus Left Bala 2': estatus_left_bala2})

# Mostrar las tablas
print("Tabla de Targets Bala 1:")
print(df_bala1)
print("\nTabla de Estatus Left Bala 2:")
print(df_bala2)

# Graficar para Bala 1
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

# Dividir los datos en dos grupos según el target (1 o 0)
mask_1 = np.array(targets_bala1) == 1
mask_0 = np.array(targets_bala1) == 0

# Mostrar los puntos en la gráfica con colores diferentes según el target
ax1.scatter(data_bala1[mask_1, 0], data_bala1[mask_1, 1], data_bala1[mask_1, 2], label='En el Aire - 1', marker='o', color='blue')
ax1.scatter(data_bala1[mask_0, 0], data_bala1[mask_0, 1], data_bala1[mask_0, 2], label='En el Suelo - 0', marker='o', color='red')

ax1.set_xlabel('Desplazamiento Bala 1')
ax1.set_ylabel('Velocidad Bala 1')
ax1.set_zlabel('Estatus Aire')

ax1.legend()
ax1.set_title('Gráfica para Bala 1')
plt.show()

# Graficar para Bala 2
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# Dividir los datos en dos grupos según el estatusLeft (1 o 0)
mask_left_1 = np.array(estatus_left_bala2) == 1
mask_left_0 = np.array(estatus_left_bala2) == 0

# Mostrar los puntos en la gráfica con colores diferentes según el estatusLeft
ax2.scatter(data_bala2[mask_left_1, 0], data_bala2[mask_left_1, 1], data_bala2[mask_left_1, 2], label='Estatus Left - 1', marker='^', color='green')
ax2.scatter(data_bala2[mask_left_0, 0], data_bala2[mask_left_0, 1], data_bala2[mask_left_0, 2], label='Estatus Right - 0', marker='^', color='yellow')

ax2.set_xlabel('Desplazamiento Bala 2')
ax2.set_ylabel('Velocidad Bala 2')
ax2.set_zlabel('Estatus Left')

ax2.legend()
ax2.set_title('Gráfica para Bala 2')
plt.show()
