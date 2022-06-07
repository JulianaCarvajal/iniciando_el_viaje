"""Realizar un programa que le solicite a 3 usuarios ingresar por teclado información personal,
la información de cada usuario se debe guardar en una estructura de colección inmutable,
luego mostrar por pantalla la información de los usuarios agrupada en una estructura de colección mutable.

La información para solicitar es:
a.Nombres y apellidos.
b.Ocupación.
c.Edad.
d.Ciudad.
e.Número de contacto.
f.Correo electrónico.
"""

names_and_surnames_1 = input('Ingrese sus nombres y apellidos: ')
occupation_1 = input('Ingrese su ocupación: ')
age_1 = input('Ingrase su edad: ')
city_1 = input('Ingrese su ciudad: ')
contact_number_1 = input('Ingrese su número de contacto: ')
email_1 = input('Ingrese su correo electrónico: ')

user_info_1 = ('Nombres y apellidos 1: ' + names_and_surnames_1, 'Ocupación 1: ' + occupation_1,
              'Edad 1: ' + age_1, 'Ciudad 1: ' + city_1, 'Número de contacto 1: ' + contact_number_1,
              'Correo electrónico 1: ' + email_1)

names_and_surnames_2 = input('Ingrese sus nombres y apellidos: ')
occupation_2 = input('Ingrese su ocupación: ')
age_2 = input('Ingrase su edad: ')
city_2 = input('Ingrese su ciudad: ')
contact_number_2 = input('Ingrese su número de contacto: ')
email_2 = input('Ingrese su correo electrónico: ')

user_info_2 = ('Nombres y apellidos 2: ' + names_and_surnames_2, 'Ocupación 2: ' + occupation_2,
              'Edad 2: ' + age_2, 'Ciudad 2: ' + city_2, 'Número de contacto 2: ' + contact_number_2,
              'Correo electrónico 2: ' + email_2)

names_and_surnames_3 = input('Ingrese sus nombres y apellidos: ')
occupation_3 = input('Ingrese su ocupación: ')
age_3 = input('Ingrase su edad: ')
city_3 = input('Ingrese su ciudad: ')
contact_number_3 = input('Ingrese su número de contacto: ')
email_3 = input('Ingrese su correo electrónico: ')

user_info_3 = ('Nombres y apellidos 3: ' + names_and_surnames_3, 'Ocupación 3: ' + occupation_3,
              'Edad 3: ' + age_3, 'Ciudad 3: ' + city_3, 'Número de contacto 3: ' + contact_number_3,
              'Correo electrónico 3: ' + email_3)

# Concatenate the tuples and convert the result to a list:
list_users_info = list(user_info_1 + user_info_2 + user_info_3)

print(list_users_info)
