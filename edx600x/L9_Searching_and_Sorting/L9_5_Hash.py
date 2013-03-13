import string
print("index of a : ",string.ascii_lowercase.index("a"))
print("index of m : ",string.ascii_lowercase.index("m"))
print("index of z : ",string.ascii_lowercase.index("z"))

def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26

print hash('fgdf')