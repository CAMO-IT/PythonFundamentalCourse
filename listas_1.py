'''
    quinta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== listas
'''
my_list = [2,8,2.3,"python",False,10]

# accediendo a los elementos de la lista
elemento = my_list[-1]
elemto2 = my_list[2]
print(elemento)
print(elemto2)

# eliminando elemementos

#del my_list[2]
#print(my_list)

my_list.append("Linux")

print(my_list)

my_list.append(True)
print(my_list)

# insertar elementos en una posicion especifica
my_list.insert(4,"PCEP")
print(my_list)

print(my_list[-2])

s = my_list.pop(-2)

print(my_list)
print(s)

for e in my_list:
    print(e)

'''

my_list1 = [10,2.5,"python","Linux",True]
print(len(my_list1))

# slicing
print(my_list1[-3:-2])
print(len(my_list1))

print(my_list1[:])

# copia de listas
my_list2 = my_list1[-3:-1]
print(my_list2)
print(my_list1)
print('============')
#del my_list1[-1]
print(my_list1)
print(my_list2)

# ordenar lista
my_list1 = [5,10,20,2,0,1]
'''
my_list1.sort()
print(my_list1)
my_list1.sort(reverse=True)
print(my_list1)

print(my_list1)

print(sorted(my_list1))
print(my_list1)

for elem in my_list1:
    print(elem)

print(20 in my_list1)
print(20 not in my_list1)

my_list1 = [5,10,20,2,0,1]
my_listpor2=[]
# multiplicar a cada elemento *2

for e in my_list1:
    e *= 2
    my_listpor2.append(e)

print(my_listpor2)

lista3 = [e*2 for e in my_list1]
print(lista3)
'''
# 128 64 32 16 8 4 2 1
lista_clave = []
for x in range(8):
    x = 2**x
    lista_clave.append(x)
lista_clave.reverse()
print(lista_clave)

# usando compresecion de listas
lista_clave2 = [2**x for x in range(8)]
lista_clave2.reverse()
print(lista_clave2)