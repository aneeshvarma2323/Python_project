s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

max_char = ""
max_count = 0

for ch in frequency:
    if frequency[ch] > max_count:
        max_count = frequency[ch]
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)