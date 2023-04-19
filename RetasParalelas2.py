# 0,5
# 4,2

# Coef = 2-5/4-0

#12x+6y=180
#y=(180-12x)/6
#y=15-2x

# import numpy as np
# import matplotlib.pyplot as plt

# def coeficiente_angular(x1, y1, x2, y2):
#     m = (y2 - y1) / (x2 - x1)
#     return m

# print(coeficiente_angular(15,30,30,15))

import matplotlib.pyplot as plt
import numpy as np

def plot_function(func, x_range):
    x = np.linspace(*x_range, num=1000)
    y = func(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da função')
    plt.show()

def f(x):
    return x*2 + 15

plot_function(f, (-5, 5))