import timeit

import matplotlib.pyplot as plt


def calcular_tiempos_lista_str(func, num_elements=500):
    results = []
    for x in range(1, num_elements):
        lista_elementos = [str(i) for i in range(x)]
        results.append(timeit.timeit(lambda: func(lista_elementos), number=1000))
    return results


def calcular_tiempos_lista_int(func, num_elements=500):
    results = []
    for x in range(1, num_elements):
        lista_elementos = [i for i in range(x)]
        results.append(timeit.timeit(lambda: func(lista_elementos), number=1000))
    return results


def calcular_tiempos_enteros(func, num_elements=500):
    result = []
    for element in range(num_elements):
        result.append(timeit.timeit(lambda: func(element), number=1000))
    return result


def calcular_tiempos_diccionario(func, num_elements=500):
    results = []
    for x in range(1, num_elements):
        lista_elementos = {str(i): i for i in range(x)}
        results.append(timeit.timeit(lambda: func(lista_elementos), number=1000))
    return results


def print_grafica(tiempos):
    plt.plot(tiempos, 'b')
    plt.xlabel('Inputs')
    plt.ylabel('Steps')
    plt.show()
