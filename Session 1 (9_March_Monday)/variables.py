# ============================================
# VARIABLES IN PYTHON
# ============================================
# Variables are containers used to store values.
# Each variable refers to a memory location where
# the actual value is stored.

# Python stores the value in memory and the variable
# holds the reference (address) to that memory location.


# ============================================
# MEMORY ADDRESS
# ============================================
# The function id() is used to find the memory
# address of a variable.

# Syntax:
# id(variable_name)


# ============================================
# SINGLE VARIABLE CREATION
# ============================================

a = 10
b = 20
c = 30

# Printing memory addresses of variables

print("Value of a:", a)
print("Address of a:", id(a))

print("Value of b:", b)
print("Address of b:", id(b))

print("Value of c:", c)
print("Address of c:", id(c))


# ============================================
# MULTIPLE VARIABLE CREATION
# ============================================
# Python allows assigning multiple variables
# in a single line.

a, b, c = 10, 20, 30

print("Address of a:", id(a))
print("Address of b:", id(b))
print("Address of c:", id(c))


# ============================================
# NOTES
# ============================================
# - Variables store references to values in memory.
# - id() returns the unique memory address of the object.
# - Multiple variables can be created in one line.
# - This is called multiple assignment.