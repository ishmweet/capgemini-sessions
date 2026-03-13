# ============================================
# PYTHON DATA TYPES
# ============================================
# Data types specify the type of data that a
# variable can store in Python.


# ============================================
# 1. SINGLE VALUE DATA TYPES
# ============================================
# These data types store only one value.


# --------------------------------------------
# NUMERIC DATA TYPES
# --------------------------------------------
# Python has three main numeric types:
# 1. Integer (int)
# 2. Float (float)
# 3. Complex (complex)


# --------------------------------------------
# INTEGER (int)
# --------------------------------------------
# Used to store whole numbers (without decimal point)
# Default value of integer = 0

a = 10
b = -25
c = 0

print(a, type(a))
print(b, type(b))
print(c, type(c))


# --------------------------------------------
# FLOAT (float)
# --------------------------------------------
# Used to store decimal numbers
# Default value of float = 0.0

x = 26.3
y = -3.14
z = 0.0

print(x, type(x))
print(y, type(y))
print(z, type(z))


# --------------------------------------------
# COMPLEX (complex)
# --------------------------------------------
# Used to represent complex numbers
# Format: a + bj

# a -> real part
# b -> imaginary part
# j -> imaginary unit (√-1)

c1 = 3 + 4j
c2 = 5 - 2j
c3 = 0 + 0j

print(c1, type(c1))
print(c2, type(c2))
print(c3, type(c3))

# Accessing real and imaginary parts
print(c1.real)
print(c1.imag)


# --------------------------------------------
# BOOLEAN (bool)
# --------------------------------------------
# Boolean represents logical values

# Possible values
t = True
f = False

print(t, type(t))
print(f, type(f))


# --------------------------------------------
# USES OF BOOLEAN
# --------------------------------------------

# 1. As a value
status = True
print("Status:", status)

# 2. As a result of a condition

print(10 > 5)   # True
print(5 > 10)   # False
print(7 == 7)   # True
print(8 != 3)   # True


# ============================================
# 2. MULTI VALUE DATA TYPES (COLLECTION TYPES)
# ============================================
# These data types store multiple values
# inside one variable


# --------------------------------------------
# STRING (str)
# --------------------------------------------
# Used to store text

name = "Python"
sentence = "Cybersecurity is interesting"

print(name)
print(sentence)
print(type(name))

# Accessing characters in string
print(name[0])
print(name[3])


# --------------------------------------------
# LIST (list)
# --------------------------------------------
# Ordered collection
# Allows duplicate values
# Mutable (can be changed)

numbers = [1, 2, 3, 4, 5]
mixed = [10, "Python", 3.5]

print(numbers)
print(mixed)
print(type(numbers))

# Access element
print(numbers[2])


# --------------------------------------------
# TUPLE (tuple)
# --------------------------------------------
# Ordered collection
# Immutable (cannot be changed)

coordinates = (10, 20)
data = ("Alice", 25, "Engineer")

print(coordinates)
print(data)
print(type(coordinates))


# --------------------------------------------
# SET (set)
# --------------------------------------------
# Unordered collection
# Does not allow duplicates

unique_numbers = {1, 2, 3, 4, 4, 5}

print(unique_numbers)
print(type(unique_numbers))


# --------------------------------------------
# DICTIONARY (dict)
# --------------------------------------------
# Stores data in key-value pairs

student = {
    "name": "John",
    "age": 20,
    "course": "Cybersecurity"
}

print(student)
print(type(student))

# Access dictionary value
print(student["name"])
print(student["age"])


# ============================================
# DEFAULT VALUES
# ============================================

# Integer default value
default_int = 0
print(default_int)

# Float default value
default_float = 0.0
print(default_float)

# Complex default value
default_complex = 0 + 0j
print(default_complex)

# Boolean default value
default_bool = True
print(default_bool)


# ============================================
# NON-DEFAULT VALUES
# ============================================
# Any value other than the default value

int_example = 50
float_example = 9.8
complex_example = 2 + 3j
bool_example = False

print(int_example)
print(float_example)
print(complex_example)
print(bool_example)