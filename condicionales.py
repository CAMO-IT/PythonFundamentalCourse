'''
    Cuarta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== Condicionales
# si su edad es > 18 entonces ingresa al evento
'''
edad = int(input('Ingrese su edad: '))

if edad > 18:
    print('Bienvenido al evento!! pase')
else:
    print('No entra al evento, retirese por favor')
'''
# ingrese un numero por teclado y averigue si es positivo negativo o si es cero

numero = int(input('Ingrese un numero: '))

if numero > 0:
    print('es positivo')
elif numero < 0:
    print('es negativo')
elif numero == 0:
    print('es cero')