import math
import numpy as np

def sumar_n_numeros():
    numeros_a_sumar = int(input('Cuantos numeros quieres sumar? '))

    lista_numeros = []

    for numero in range(0, numeros_a_sumar):
        numero_a_sumar = float(input(f'Ingresa el numero {numero} a sumar: '))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)

def multi_n_numeros():

    multiplicar = int(input('Cuantos numeros quieres multiplicar: '))
    lista = []

    for number in range(1, multiplicar + 1):
        numero_multi = float(input(f'Ingresa el numero {number} a multiplicar: '))
        lista.append(numero_multi)

    return math.prod(lista)

def div_2():
    number_one = float(input(f'Ingresa el primer numero: '))
    number_second =float(input(f'Ingresa el segundo numero: '))
    if number_second == 0:
        print(f'No se puede dividir entre 0!.')
        return None


    division_x = number_one / number_second
    return division_x
    
# y = mx + b
def resolver_para_y():
    pendiente = float(input('Porfavor ingresa la pendiente: '))
    ordenada_al_origen = float(input('Porfavor ingresa la ordenada al origen: '))
    punto_x = int(input('Ingresa el punto en x: '))
    resultado = (pendiente * punto_x) + ordenada_al_origen

    return {'resultado' :resultado, 'pendiente' :pendiente, 'ordenada_al_origen':ordenada_al_origen, 'punto_en_x' :punto_x}

def resolver_matrices():
    filas_matriz = int(input('Ingrese el numero de filas de las matriz: '))
    columnas_matriz = int(input('Ingrese el numero de columnas de la matriz: '))

    a = np.zeros((filas_matriz, columnas_matriz))
    print('Ingrese los valores de x e y si es el caso: ')
    for x in range(filas_matriz):
        for y in range(columnas_matriz):
            a[x, y] = float(input('Ingrese el valor para la posicion [{x+1}, {y+1}]: '))

    b = np.zeros(filas_matriz)
    print('Ingrese los valores de la igualdad en la ecuacion: ')
    for x in range(filas_matriz):
        b[x] = float(input('Ingrese el valor para la posicion {x+1}: '))

    resultado = np.linalg.solve(a, b)

    return resultado

    


