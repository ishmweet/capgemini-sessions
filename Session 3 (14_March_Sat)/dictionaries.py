# Dictionary = {key: value}
# A collection of key:value pairs.
# Dictionaries are ordered (Python 3.7+), mutable (changeable), and keys must be unique.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


# dir() -> shows all available dictionary methods
# print(dir(capitals))


# get() -> returns value of the specified key
# print(capitals.get("USA"))


# update() -> adds a new key:value pair
# capitals.update({"Germany": "Berlin"})


# update() can also modify an existing value
# capitals.update({"USA": "Detroit"})


# pop() -> removes a specific key
# capitals.pop("China")


# popitem() -> removes the last inserted key:value pair
# capitals.popitem()


# clear() -> removes all elements
# capitals.clear()


# keys() -> returns all keys
# keys = capitals.keys()
# print(keys)


# values() -> returns all values
# values = capitals.values()
# print(values)


# items() -> returns key:value pairs as tuples
# items = capitals.items()
# print(items)


# Checking if a key exists
# print("USA" in capitals)


# Accessing values using key
# print(capitals["India"])


# Looping through keys
# for key in capitals:
#     print(key)


# Looping through values
# for value in capitals.values():
#     print(value)


# Looping through key-value pairs
for key, value in capitals.items():
    print(f"{key}: {value}")


# Important notes

# Dictionaries store data in key:value pairs.
# Keys must be unique but values can be duplicated.
# Dictionaries use curly braces {}.
# Dictionaries are mutable (values can be changed).
# Dictionaries do not allow duplicate keys.

# Memory concept
# Python stores the dictionary object in memory,
# and the variable holds a reference to that memory location.

# print(id(capitals))