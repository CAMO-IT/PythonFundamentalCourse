'''
    Cuarta sesion del curso
    python essential
    por CAMO ACADEMY
'''# ==== operaciones bit a bit

'''
128 64 32 16 8 4 2 1
             1 1 1 1    -> 15 =a
        0  1 0 1 1 0     -> 22 =b  

a & b            1&1=1  otro caso es 0

            0 0 1 1 0     --> 6
a | b
            1 1 1 1 1      -> 31 
a ^ b
            1 1 0 0 1      -> 25
'''
a = 15
b = 22

# a&b
print(a&b)
print(bin(a&b))

# a|b
print(a|b)
print(bin(a|b))

# a^b
print(a^b)
print(bin(a^b))

# ~ a
# 15 = -15-1=-16
print(~a)

# desp <<  17<<1
print(17<<1)


# 17<<2

'''
128 64 32 16 8 4 2 1
0   0   0 1  0 0 0 1  --> 17
     1  0  0  0 1 0 0  --> 68 
'''
print(17<<2)

'''
128 64 32 16 8 4 2 1
0   0   0 1  0 0 0 1  --> 17
             1 0 0 0 1  --> 1000 -> 8 
'''

print(17>>1)