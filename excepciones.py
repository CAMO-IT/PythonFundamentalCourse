'''
    Octaba sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== Exepciones


 # try except  // try catsh
'''
try:
    numero1 = int(input('Insertar un numero: '))
    numero2 = int(input('Insertar otro numero: '))

    resultado = numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print('no es posible divir entre cero')
except ValueError:
    print('ingreso dato incorrecto')
except TypeError:
    print('no ingresi un numero, por favor corrigalo')

else:
    print('algo')


# indexError
try:
    lista =['manzana','banana','cereza']
    print(lista[3])
except IndexError:
    print('el elemento no exite')


tareas = ["Lavar ropa", "Estudiar Python", "Ir al supermercado"]

print("Tus tareas pendientes:")
for i, tarea in enumerate(tareas):
    print(f"{i} - {tarea}")

try:
    opcion = int(input("\nElige el número de la tarea que ya completaste: "))
    # Buscamos en la lista
    tarea_completada = tareas[opcion]
except IndexError:
    print("Error: El número de tarea seleccionado no existe en la lista.")
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
else:
    print(f"¡Felicidades! Completaste: {tarea_completada}")


try:
    # Puede fallar por división por cero, o por tipo de dato si 'num' fuera texto
    num = 10
    divisor = 'casa'
    resultado = num / divisor
except Exception as error:
    # Captura CUALQUIER error que herede de Exception y te dice qué pasó
    print(f"Ocurrió un error inesperado de tipo: {type(error).__name__}")
    print(f"Detalles del error: {error}")
'''
# Un diccionario con base de datos de usuarios
usuario = {
    "nombre": "Carlos",
    "edad": 28,
    "pais": "México"
}


try:
    # Buscamos la clave "correo", la cual no está definida en nuestra base
    correo_usuario = usuario["correo"]
except KeyError as clave_faltante:
    print(f"Error: No se encontró la información solicitada.")
    print(f"La clave base que falta es: {clave_faltante}")

