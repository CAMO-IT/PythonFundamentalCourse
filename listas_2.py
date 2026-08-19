'''
    Sexta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== listas2
#    listas de listas
'''
my_lista = [5,[3,9],"python",True]
elemento = my_lista[1][1]
print(elemento)


# Lista con [Nombre, Edad, País]
usuarios = [
    ["Ana", 25, "México"],
    ["Luis", 30, "España"],
    ["María", 22, "Argentina"]
]
# españa
e = usuarios[1][2]
print(e)
# maria 20
usuarios[2][1]=20
print(usuarios)
# adicinar Ale,39,"Bolivia"
usuarios.append(["ale",39,'Bolivia'])
print(usuarios)
'''
# immrpimir un triagulo de * 

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()