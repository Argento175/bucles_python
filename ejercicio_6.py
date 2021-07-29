# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0

secuencia = [inicio,fin]                # Creo una 'lista' de números...

if inicio < fin:                        # Con la condición de si el primer número ingresado es menor al segundo,
    num = inicio                        # creo un bucle 'while' para agregar elementos a la lista...
    while num < fin:
        num += 1
        secuencia.append(num)
        if num == fin:                  # Cuando el número a ingresar es igual al segundo valor ingresado por
            secuencia.remove(num)       # el usuario, salgo del bucle sin ingresar el último número.
            break  
else:
    num = inicio                        # Repito el proceso, pero a la inversa...
    while num > fin:
        num -= 1
        secuencia.append(num)
        if num == fin:
            secuencia.remove(num)
            break
print(secuencia)
# for ... in range(....)
secuencia_len = len(secuencia)

neg = 0
pos = 0

for i in range(secuencia_len):
    numeros = secuencia[i]
    if numeros < 0:
        neg = numeros
    if numeros > 0:
        pos = numeros
        
# Imprimir el valor de la cantidad de números positivos y negativos
print("Hay",neg,"números negativos...\n")
print("Hay",pos,"números positivos...\n")

print("terminamos!")
