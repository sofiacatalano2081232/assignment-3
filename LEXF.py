from itertools import product

def generate_strings(alphabet, n):
    return [''.join(letter) for letter in product(alphabet, repeat=n)]


ordered_alphabet = "ABCDE"  
length_n = 4  

strings = generate_strings(ordered_alphabet, length_n)
for string in strings:
    print(string)




