#Python program to count and display the vowels of a given string.

String ="Welcome to python Training"
Vowels= "aeiouAEIOU"
vowel_count=0
vowel_list=[]
for char in String:
    if char in Vowels:
        vowel_count+=1
        vowel_list.append(char)

print(f"Vowels in a string: {' , '.join(vowel_list)}")
print(f"Total numbers of vowel:",vowel_count)
