#Python program to reverse a words in a string

string=" Deeptech Python Training "
words=string.split()
reversed_words = words[::-1]
reversed_str=' '.join(reversed_words)
print("Reversed String:",reversed_str)

