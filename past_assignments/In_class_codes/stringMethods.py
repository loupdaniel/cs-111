

text = " hello WORLD! world"
print("Consider the text \"" + text + "\"")

print(".lower() lowercases the string")
print(text.lower())
print()

print(".upper() uppercases the string")
print(text.upper())
print()

print(".capitalize() capitalizes the first character of string (and capitalizing space does nothing!)")
print(text.capitalize())
print()

print(".count(\"l\") counts the number of instances of a substring (in this case \"l\")")
print(text.count("l"))
print()

print(".replace(\"l\", \"m\") replaces all instances of a substring with another")
print(text.replace("l","m"))
print()

print(".strip() removes whitespace around the text")
print(text.strip())
print()

print(".startswith(\" hello\") tells you if the text starts with a substring")
print(text.startswith(" hello"))
print()

print(".endswith(\" hello\") tells you if the text ends with a substring")
print(text.endswith("LD! "))
print()

print(".index(\"l\") gives the index of the first instance of a substring (here \"l\"), and raises an exception if the substring is not present at all")
print(text.index("l"))
print()

print(".find(\"potato\") is just index(\"potato\") except that it will silently fail and return -1 when the substring is not present")
print(text.find("potato"))
print() # -1 --> silent failure

print(".split(" ") splits the string along the given substring (here space) and gives a list of the results")
print(text.split(" "))
print() 

print(".join() reverses .split and concatenates together string iterables with text between each part")
print(text.join(["part 1","part 2","part 3"]))
