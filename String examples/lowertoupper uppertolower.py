s1 = input("Enter a string to convert to lowercase: ")
s2 = input("Enter a string to convert to uppercase: ")

lower = ""
upper = ""

for ch in s1:
    if 'A' <= ch <= 'Z':
        lower += chr(ord(ch) + 32)
    else:
        lower += ch

for ch in s2:
    if 'a' <= ch <= 'z':
        upper += chr(ord(ch) - 32)
    else:
        upper += ch

print("Lowercase:", lower)
print("Uppercase:", upper)