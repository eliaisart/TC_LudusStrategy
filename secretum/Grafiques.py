
"""Iteratiu"""
def iteratiu(value):
    suma = 0
    for i in value:
        suma = suma + int(i)

    while (suma > 10):
        suma2 = 0
        for i in str(suma):
            suma2 = suma2 + int(i)
            suma = suma2
    return suma

"""Recursiu"""
def recursiu(value,count=0):
    s = int(value)
    if (s < 10):
        count = count+1
        return [s,count]
    else:
        suma = 0
        for i in str(value):
            suma = suma + int(i)
    return recursiu(str(suma),count)

"""Complexitat:(𝑙𝑜𝑔(𝑛))"""



import random
import math

n = [10, 100, 1000, 10000, 1000000, 100000000000000]
steps_experimental = [0, 0, 0, 0, 0, 0]
steps_loglog = [0, 0, 0, 0, 0, 0]
steps_log = [0, 0, 0, 0, 0, 0]
steps_n = [0, 0, 0, 0, 0, 0]

for i in range(len(n)):
    steps_experimental[i] = recursiu(n[i])[1]

    for j in range(n[i]):
        steps_n[i] = steps_n[i] + 1

    for j in range(math.ceil(math.log(n[i]))):
        steps_log[i] = steps_log[i] + 1

    for j in range(math.ceil(math.log(math.log(n[i], 2), 2)) + 1):
        steps_loglog[i] = steps_loglog[i] + 1



import matplotlib.pyplot as plt
import numpy as np

plt.plot(n,steps_experimental, 'g',label='te(x)')
plt.plot(n,steps_log, 'r', label='f(x)=log(x)')
plt.plot(n,steps_loglog, 'y', label='(x)=log(log(x))')
plt.plot(n,steps_n, 'b', label='(x)= n')
plt.xscale('log')
plt.xlabel('Mida entrada (n)')
plt.ylabel('Operacions')
plt.title('Anàlisis de la complexitat')
plt.legend()
plt.show()


"""Eficiencia"""

import random
import math
import time
n = [10,100,1000,1000000,10000000000000,10000000000000000000000000]
for i in range(len(n)):
    %timeit iteratiu(str(n[i]))
    %timeit recursiu(n[i])


n = [10,100,1000,1000000,10000000000000,10000000000000000000000000]
recursiu  = [2.13,2.59,3.25,3.65,6.51,9.5]
iteratiu = [1.09,1.41,1.62,2.7,4.95,7.89]

import matplotlib.pyplot as plt
import numpy as np

plt.plot(n,recursiu, 'g',label='recursiu')
plt.plot(n,iteratiu, 'b',label='iteratiu')
plt.xscale('log')
plt.xlabel('Mida entrada (n)')
plt.ylabel('Temps (microsegons)')
plt.title('Temps Iteratiu/Recursiu')
plt.legend()
plt.show()

plt.plot(n,iteratiu, 'b',label='iteratiu')
plt.xscale('log')
plt.xlabel('Mida entrada (n)')
plt.ylabel('Temps (microsegons)')
plt.title('Temps Iteratiu/Recursiu')
plt.legend()
plt.show()


