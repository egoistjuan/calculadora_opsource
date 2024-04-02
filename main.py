from funciones_calculadora import sumar_n_numeros
from funciones_calculadora import multi_n_numeros
from funciones_calculadora import div_2
from funciones_calculadora import resolver_para_y
from funciones_calculadora import resolver_matrices

#importamos librerias para poder graficar
import matplotlib.pyplot as plt
import numpy as np


while True:
    print('''
    Bienvenido a mi calculadora, por favor ingresa la opcion que desees.
    -------------------------------------------------------------------
    1)Hacer una suma de N numeros,
    2)Hacer una multiplicacion de N numeros,
    3)Hacer una division de 2 numeros
    4)Resolver la posicion en Y (para la ecuacion y = mx + b)
    5)Resolver ecuaciones lineales
          
    0)Salir del programa

    ''')
    
    opcion = int(input('> '))
 
    if opcion == 0:
        break

    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f'El resultado de tu suma es {resultado}')

    elif opcion == 2:
        multiplicacion = multi_n_numeros()
        print(f'El resultado es: {multiplicacion}')
    
    elif opcion == 3:
        division_resultado = div_2()
        print(f'El resultado es: {division_resultado}')
    
    elif opcion == 4:
        resultado = resolver_para_y()
        print(f'El resultado es: {resultado}')

        x = np.linspace(-10, 10)
        y = resultado['pendiente'] * x + resultado['ordenada_al_origen']

        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        ax.plot(resultado['punto_en_x'], resultado['resultado'], 'yo')
        
        ax.grid(True, linestyle='-.')
        #ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()
    
    elif opcion == 5:
        resultado = resolver_matrices()
        print(f'El resultado de la ecuacion lineal es: {resultado}')


    
    else:
        print('Ejecuta una opcion valida')


print('_________________________________')
print('Bye Bye gracias por usar mi calculadora')