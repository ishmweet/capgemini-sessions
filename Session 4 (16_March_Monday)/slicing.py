# Strings support positive indexing and negative indexing
# Strings are immutable (cannot be changed after creation)
# Slicing extracts a part of the string

# Creating a string
text = "PYTHONPROGRAM"


# Using len() to get the length of the string
print(len(text))


# Using type() to check the datatype
print(type(text))


# STRING INDEXING

# Positive indexing starts from 0
# Negative indexing starts from -1 (from the end)

text = "PYTHON"

# Accessing characters using positive indexing
print(text[0])   # P
print(text[3])   # H

# Accessing characters using negative indexing
print(text[-1])  # N
print(text[-3])  # H


# STRING SLICING

# Syntax
# string[start:stop:step]

# start → index where slicing begins
# stop → index where slicing ends (not included)
# step → number of positions to move


# BASIC STRING SLICING

text = "PYTHON"

# Extract characters from index 0 to 3
print(text[0:4])   # PYTH


# DEFAULT VALUES IN SLICING

text = "PYTHON"

# If start is omitted → starts from beginning
print(text[:4])    # PYTH

# If stop is omitted → goes till end
print(text[2:])    # THON


# USING STEP IN SLICING

text = "PYTHONPROGRAM"

# Print every 2nd character
print(text[::2])


# STARTING FROM A SPECIFIC INDEX

text = "PYTHON"

# Start from index 1 and take every second character
print(text[1::2])


# NEGATIVE INDEX SLICING

text = "PYTHON"

# Extract last 3 characters
print(text[-3:])   # HON


# REVERSING A STRING

text = "programming"

# Reverse the string using slicing
print(text[::-1])


# COPYING A STRING

text = "HELLO"

# Copy the entire string
copy = text[:]

print(copy)


# COMMON STRING SLICING PATTERNS

s = "CYBERSECURITY"

print(s[:4])    # first 4 characters
print(s[4:])    # characters from index 4 to end
print(s[-3:])   # last 3 characters
print(s[:-3])   # everything except last 3 characters
print(s[::2])   # every 2nd character
print(s[::3])   # every 3rd character
print(s[::-1])  # reverse the string


# IMPORTANT POINTS

# 1. The stop index is NOT included in slicing
# 2. Slicing does not modify the original string
# 3. Slicing returns a new string
# 4. Negative step means reverse direction