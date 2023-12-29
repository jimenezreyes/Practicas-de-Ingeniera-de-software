import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import numpy as np

# Definir la función a graficar
def funcion(x):
    return x ** 5

# Generar valores de x
x = np.linspace(2, 8, 10) # Valores de 2 a 8, con 10 puntos

# Calcular los valores de y usando la función
y = funcion(x)

# Crear el gráfico
plt.title('Gráfico de la función y = x^5')
plt.plot(x, y, label='y = x^5')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar el gráfico
plt.show()
