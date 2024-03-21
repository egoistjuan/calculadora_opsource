import math

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
    



