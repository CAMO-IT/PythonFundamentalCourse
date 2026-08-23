'''
    Septima sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== diccionarios

traductor = {"cat":"gato","dog":"perro"}
print(traductor)
print(type(traductor))

lenguajes_favoritos = {
    "jose":"Python",
    "Maria":"c++",
    "Marcela":"java",
    "Marco": ["c#","prolog","java"]
}
# acceder a un value especifo
var1 = lenguajes_favoritos["jose"]
print(var1.upper())

# cambiar el lenguaje favorito de marcela

lenguajes_favoritos["Marcela"] = "PHP"

# mostrar las keys del lenguajes_favoritos
for key in lenguajes_favoritos.keys():
    print(key)

# mostrar las values del lenguajes_favoritos
for value in lenguajes_favoritos.values():
    print(value)

# mostrar los items(key:value) del lenguajes_favoritos
for key,value in lenguajes_favoritos.items():
    print(key,":",value)

# eliminar un item
del lenguajes_favoritos["Maria"]
print(lenguajes_favoritos)

#  
var2 = lenguajes_favoritos["Marco"]
var2.remove("c#")
print(lenguajes_favoritos)

# ordenar el diccionario

for key in sorted(lenguajes_favoritos.keys()):
    print(key)

# adicionar  Pamelay su lenguaje favorito go
lenguajes_favoritos["Pamela"]= "go"
print(lenguajes_favoritos)

# eliminar el ultimo item
ultimo = lenguajes_favoritos.popitem()
print(lenguajes_favoritos)
print(ultio)
