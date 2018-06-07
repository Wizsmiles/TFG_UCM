'''
Created on 13 mar. 2018

@author: Jose J. Escudero Gomez
'''

# Codigo ejemplo 1 - Retornos de funciones anidadas

def h(param1, param2):
    f()
    return param1

def f():
    "hola"

def a():
    f()
    return 6

def b():
    return 2 + a()

def c():
    return b() + b() + a() + 3

def ejemplo1():
    h("hello", "hola")
    return c() + 5


# Codigo ejemplo 2 - Modificacion de listas

def ejemplo2_1(lista):
    lista.append("2")
    return lista

def ejemplo2_2(lista, str):
    lista.pop()
    lista.append(str)
    return lista

def ejemplo2_3(lista):
    lista.append("4")
    return lista

def ejemplo2():
    lista = []
    lista.append("1");
    ejemplo2_1(lista)
    ejemplo2_2(lista, "3")
    ejemplo2_3(lista)

# Codigo ejemplo 3 - Fusion nodos iguales

def ejemplo3_1():
    return "No igual"

def ejemplo3_2(msj):
    if msj == "hijo2":
        ejemplo3_2("hijo3")
    elif msj != "hijo3":
        ejemplo3_2("hijo2")
    else:
        return "fin"

def ejemplo3():
    ejemplo3_1()
    ejemplo3_2("hijo1")

# Codigo ejemplo 4 - Excepciones

def excepcion1():
    x = 1/0

def excepcion2():
    lista = []
    lista.pop()

def excepcion3():
    excepcion1()

def ejemplo4():
    excepcion3()
    excepcion2()

# Ejemplo algoritmo Euclides recursivo

def euclides():
    mcd = euclides_rec(256,6)
    return mcd

def euclides_rec(num1,num2):
    if num2 == 0:
        return num1
    return euclides_rec(num2, num1 % num2)

## EJEMPLOS OBTENIDOS DE ROSETTACODE ##

# Codigo ejemplo de QuickSort

def myQuickSort():
    array = [3,6,2,7,1]
    array = quickSort(array)

    for element in array:
        print(str(element) + "\n")

def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

# Codigo ejemplo de MergeSort

def myMergeSort():
    array = [3,6,2,7,1]
    array = mergeSort(array)

    for element in array:
        print(str(element) + "\n")

def mergeSort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result
