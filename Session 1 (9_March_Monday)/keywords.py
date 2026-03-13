# ============================================
# KEYWORDS IN PYTHON
# ============================================
# Keywords are reserved words in Python.
# They have predefined meanings and cannot
# be used as identifiers (variable names,
# function names, class names, etc.)

# Example:
# Invalid variable names because they are keywords
# class = 10
# for = 5


# ============================================
# LIST OF PYTHON KEYWORDS
# ============================================
# Python provides a module called 'keyword'
# which contains a list of all reserved keywords.

import keyword

print(f"List of Python keywords: {keyword.kwlist}")


# ============================================
# NUMBER OF KEYWORDS
# ============================================
# The total number of keywords in Python is
# usually around 35 (depending on Python version).

print(f"Total keywords: {len(keyword.kwlist)}")


# ============================================
# SPECIAL KEYWORDS
# ============================================

# Boolean keywords
a = True
b = False

print(f"Value of a: {a}")
print(f"Value of b: {b}")


# None keyword
# None represents absence of value (similar to null)

c = None
print(f"Value of c: {c}")


# ============================================
# NOTES
# ============================================
# True  -> Equivalent to 1
# False -> Equivalent to 0
# None  -> Represents null / no value