# ============================================
# REFERENCE COUNT IN PYTHON
# ============================================
# Reference count is the number of references
# (variables or objects) pointing to a particular
# object in memory.

# Python uses reference counting as part of its
# garbage collection system to manage memory.

# When the reference count of an object becomes 0,
# Python automatically deletes that object from memory.


# ============================================
# EXAMPLE OF REFERENCE COUNT
# ============================================

# Creating a list object
a = [1, 2, 3]      # reference count = 1 (only 'a' refers to it)

# Creating another reference to the same object
b = a              # reference count = 2 ('a' and 'b' refer to same list)

print(f"Value of a: {a}")
print(f"Value of b: {b}")

print(f"Address of a: {id(a)}")
print(f"Address of b: {id(b)}")


# ============================================
# REMOVING A REFERENCE
# ============================================

a = [1, 2, 3]
b = a

print(f"Before deleting reference:")
print(f"Address of a: {id(a)}")
print(f"Address of b: {id(b)}")

# Deleting one reference
del a

# Now only 'b' refers to the list object
print(f"After deleting a, b still exists:")
print(f"Value of b: {b}")
print(f"Address of b: {id(b)}")


# ============================================
# NOTES
# ============================================
# - Multiple variables can refer to the same object.
# - Each reference increases the reference count.
# - Using 'del' removes a reference.
# - When reference count becomes 0, Python's
#   garbage collector removes the object from memory.