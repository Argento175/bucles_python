# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números.
Al finalizar el bucle, utilice la variable "cantidad_numeros" y la variable
"sumatoria" para calcular el promedio de todos los números ingresados.
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

inicio = int(input("Ingrese un número entero:\n"))
fin = int(input("Ingrese un número entero diferente al anterior:\n"))

cantidad_numeros = 0
sumatoria = 0

# for ... in range(....)
if inicio < fin:
    for i in range(inicio,fin+1):
        cantidad_numeros += 1
        sumatoria += i
else:
    for i in range(fin,inicio+1):
        cantidad_numeros += 1
        sumatoria += i
# bucle.....

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros
    promedio = (sumatoria / cantidad_numeros)
# Imprimir resultado en pantalla
print("La cantidad de números es:",cantidad_numeros)
print("La sumatoria es:",sumatoria)
print("El promedio es:",promedio)

# Gente, creanme que me puse las pilas para resolver esta vaina... Espero que esté bien. 
# Lo mando para saber si estoy en el camino correcto y así continuar con el resto...