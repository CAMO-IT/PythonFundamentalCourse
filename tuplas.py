'''
    Sexta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== Tuplas

my_tuple = (5,2,6,1)

#my_tuple[2] = 10
print(my_tuple[2])
print(type(my_tuple))

for e in my_tuple:
    print(e)

my_tuple2 = ()
print(type(my_tuple2))

# convertir una tupla en una lista
my_list = list(my_tuple)
print(my_list)
print(type(my_list))
my_list.append(0)
print(my_list)

# convertir lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

# slicing

my_tuple3 = my_tuple[:]
print(my_tuple3)
print('+++++++++')
print(my_tuple)

my_tuple = (5,2,6,1,2,5,2,1,0)
my_tuple4 = my_tuple[1:3]
print(my_tuple4)

print(my_tuple.count(2))