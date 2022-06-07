"""Realizar un programa que permita ingresar grados Fahrenheit y muestre 
por pantalla el dato en grados centígrados o pasar de grados centígrados 
a grados Fahrenheit (puede realizar cualquiera de los dos programas).
"""

fahrenheit = float(input('Ingrese los grados en Fahrenheit: '))
# Round the conversion result:
celsius = round((fahrenheit - 32)*(5/9),2)

print(f"{fahrenheit}°F es igual a {celsius}°C.")
