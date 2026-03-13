# ============================================
# IDENTIFIERS IN PYTHON
# ============================================
# An identifier is the unique name given to a
# variable, function, class, or object in Python.
# It is used to identify a memory location that
# stores a value.

# Identifiers are case sensitive.
# Example: name, Name, and NAME are different.


# ============================================
# RULES FOR IDENTIFIERS
# ============================================

# 1. An identifier should NOT start with a number

# Invalid
# 1name = "John"

# Valid
name1 = "John"


# 2. An identifier should NOT be a Python keyword

# Invalid
# class = 10
# for = 5

# Valid
class_name = "Cybersecurity"


# 3. An identifier should NOT contain special characters
# except underscore (_)

# Invalid
# user-name = "Alex"
# price$ = 100

# Valid
user_name = "Alex"
price_value = 100


# 4. An identifier should NOT contain spaces
# either at the beginning or in between

# Invalid
# user name = "John"

# Valid
userName = "John"
user_name = "John"


# 5. Identifiers can contain:
# - Alphabets (A-Z, a-z)
# - Numbers (0-9)
# - Underscore (_)

student_name = "Alice"
roll_no = 25
student2 = "Bob"


# 6. Industrial Standard Rule
# The recommended maximum length of an identifier
# should be around 78 characters for readability.


# ============================================
# EXAMPLES OF IDENTIFIERS
# ============================================

name = "John"     # 'name' is an identifier
age = 19          # 'age' is an identifier
course = "Python"
marks = 92

print(name)
print(age)
print(course)
print(marks)


# Checking the type of stored values
print(type(name))
print(type(age))
print(type(course))
print(type(marks))