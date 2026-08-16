'''
    Quinta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== if, elif

# if independientes  problema
# sistema que clasifica una temperatura.
'''
temperatura = 5

if temperatura > 30:
    print("Hace calor")
elif temperatura > 20:
    print("Está templado")
elif temperatura > 10:
    print("Hace frío")
else:
    print("helada")
'''
# anidamiento infinito
# calcular el precio de una entrada de cine 
# según la edad: gratis para menores de 4 años, 
# $5 para menores de 18, $10 para adultos y 
# $7 para mayores de 65.

edad = 25

if edad < 4:
    print("Gratis")
elif  edad < 18:
        print("Pagas $5")
elif edad < 65:
            print("Pagas $10")
else:
            print("Pagas $7")


# Un estudiante recibe una calificación de 0 a 100. Necesitamos 
# transformarla en letras (A, B, C, F). Las condiciones dependen 
# una de la otra de forma estricta.
# Tu tarea: Escribe un programa desde cero que use elif para evaluar 
# la variable nota:
#   1. Si es mayor o igual a 90, imprime "A".
#   2. Si es mayor o igual a 80 (pero menor a 90), imprime "B".
#   3. Si es mayor o igual a 70 (pero menor a 80), imprime "C".
#   En cualquier otro caso, imprime "F".
# El aprendizaje: Al usar elif, no necesitas escribir 
# if nota >= 80 and nota < 90. El operador elif ya descarta automáticamente
#  la opción anterior.