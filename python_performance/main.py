def func_2_n(n):
    if n in {0, 1}:
        return 1
    else:
        return func_2_n(n - 1) + func_2_n(n - 2)


def func_n_2(mi_lista):
    result = None
    for elemento in mi_lista:
        for elemento_2 in mi_lista:
            result = elemento_2
    return result


def func_log_n(lista):
    num_a_encontrar = 100000000
    first = 0
    last = len(lista) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if lista[midpoint] == num_a_encontrar:
            found = True
        else:
            if num_a_encontrar < lista[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def func_0n(mi_lista):
    result = None
    for elemento in mi_lista:
        result = elemento
    return result


def func_0c(mi_lista):
    result = mi_lista[0]
    return result


def my_function():
    # func_0c([i for i in range(500)])
    # func_0n([i for i in range(500)])
    # func_log_n([i for i in range(500)])
    func_n_2([i for i in range(500)])
    # func_2_n(33)
