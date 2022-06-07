"""A partir del ejercicio anterior, crea un programa para calcular la nota final
de un estudiante universitario. Para ello, el usuario debe ingresar 3 notas
y el valor porcentual de cada nota, realiza y devuelve la media por pantalla.
"""

number_1 = float(input('Ingrese la nota 1: '))
percentage_1 = float(input('Ingrese el valor porcentual de la nota 1: '))

number_2 = float(input('Ingrese la nota 2: '))
percentage_2 = float(input('Ingrese el valor porcentual de la nota 2: '))

number_3 = float(input('Ingrese la nota 3: '))
percentage_3 = float(input('Ingrese el valor porcentual de la nota 3: '))

media = (number_1*percentage_1 + number_2*percentage_2 + number_3*percentage_3)/100

print(f"{media} es la nota media.")
