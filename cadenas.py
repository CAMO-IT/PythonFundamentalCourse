'''
    Tercera sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== Strings
'''
# slicing rebanado
cad ="python"
print(cad[0:7])
print(cad[0:2])

# pyth  [0:3]
print(cad[3:])
# th
print(cad[2:4])
print(cad[-6:])

print(cad[-4:-2])

print('\n\tI\'m love python')

# operadores * + 
cad = "ingenieria informatica"
cad1 = "ingenieria de sistemas"
print(cad*3)
print(cad+" "+cad1)

# metdodos
nombre = "          alejandro miranda CAYOJA                 "
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
print(nombre)
print(nombre.lstrip())
print(nombre.rstrip())
print(nombre.strip())


cad = 'banana'
print(cad.count('a'))

# 
web = "http://www.cisco.com"
print(web.removeprefix("http://"))
print(web.removesuffix(".com"))
'''

# Casting
'''
nombre = input('Ingrese su nombre:')
print('Bienvenido '+ nombre.capitalize())
edad = int(input('por favor ingrese su edad:'))
edad = edad + 5
print('su nueva edad es '+str(edad))
# ingresese su peso y lo restamos 2 kg
peso = float(input(" Ingrese su peso"))
peso = peso - 2.0
print("su nuevo peso[kg] es"+ str(peso))
'''
print('=====================')
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad:'))
peso = float(input('Ingrese su peso[kg]'))

edad += 5
peso -= 2.0

# F-string

print(f'Bienvenido {nombre} \n su nueva edad es  {edad} \n su nuevo peso en [kg] es {peso}')

print(type(nombre))
print(type(edad))
print(type(peso))