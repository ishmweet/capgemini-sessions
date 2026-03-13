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

print(keyword.kwlist)


# ============================================
# NUMBER OF KEYWORDS
# ============================================
# The total number of keywords in Python is
# usually around 35 (depending on Python version).

print("Total keywords:", len(keyword.kwlist))


# ============================================
# SPECIAL KEYWORDS
# ============================================

# Boolean keywords
a = True
b = False

print(a)
print(b)


# None keyword
# None represents absence of value (similar to null)

c = None
print(c)


# ============================================
# NOTES
# ============================================
# True  -> Equivalent to 1
# False -> Equivalent to 0
# None  -> Represents null / no value