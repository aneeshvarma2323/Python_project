s = input("Enter a sentence: ")

words = s.split()

letters = 0

for ch in s:
    if ch.isalpha():
        letters += 1

print("Number of words:", len(words))
print("Number of letters:", letters)