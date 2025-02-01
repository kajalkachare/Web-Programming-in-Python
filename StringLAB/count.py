#Python program to count occurrences of each word in a given sentences

def count_word(str):
    count={}
    for char in str.split():
        char= char.strip('.,?!').lower()
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count

print(count_word("To change the overall look of your document. To change the look available in the gallery"))