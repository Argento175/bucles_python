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
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0
secuencia = [inicio,fin]

for num in secuencia:
    sumatoria = sumatoria + num
print("El valor de la sumatoria es",sumatoria,"\n")
print("Fin primera parte\n")
# for ... in range(....)

for i in range(inicio,fin):
    print(i)
    sumatoria =sumatoria + i

# Imprimir el valor de la sumatoria
print("El valor de la sumatoria es:",sumatoria,"\n")
print("terminamos!")
