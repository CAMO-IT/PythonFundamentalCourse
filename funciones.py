'''
    Sexta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== funciones
'''
mensaje = 'Bienvenido'
print(mensaje)
print(mensaje)
print(mensaje)
print(mensaje)
print(mensaje)


def mensaje_saludo():
    mensaje = 'Bienvenido'
    print(mensaje)
mensaje_saludo()



def suma(a,b,c):
    return a+b+c
def resta(a,b):
    return a-b

#print(suma(2,5))
print(resta(2,5))
#print(suma(6,3))

# parametros pocisionales

# parametros de palabra clave
#print(suma(a=2, b=5))

# parametros mix
print(suma(b=4,a=1,c=1))


def intro(first_name, last_name):
    print(f'Hello my name is {first_name} {last_name}.')

intro("Alex",last_name="Perez")


# None
#print(2+None)
print(type(None))

a = None
print(a)
print(type(a))


valor = None
if valor is None:
    print("no contiene ningun valor ")

def otra_funcion(n):
    if n % 2 == 0:
        return True

print(otra_funcion(3))


def list_sum(lista):
    s = 0
    for elem in lista:
        s += elem
    return s

print(list_sum([5,4,2]))


# globlal

def my_function():
    global var
    var = 2
    print("conosco esa variable 2",var)

var = 1
my_function()
print(var)

'''

def message():
    global alt 
    alt = 3
    print("Hello word!!")
    print(alt)

alt = 1
print(alt)
message()
