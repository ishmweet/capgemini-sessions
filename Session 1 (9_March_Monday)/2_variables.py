# Containers that store certain values (reference address)

# single variable creation
a = 10
id(a)  # address of a

b = 20
id(b)  # address of b

c = 30
id(c)  # address of c

print(id(a))
print(id(b))
print(id(c))

print("--------")

# multiple variable creation
a, b, c = 10, 20, 30
print(id(a))
print(id(b))
print(id(c))