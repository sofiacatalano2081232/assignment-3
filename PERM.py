from itertools import permutations

n = 5
my_list = [1,2,3,4,5]

# Generate all permutations
all_permutations = list(permutations(my_list))

# Print all permutations
for perm in all_permutations:
    perm_1 = str(perm).replace(",", "").replace("(", "").replace(")", "")
    print(perm_1)

print(len(all_permutations))

# Define the file name where you want to store the output
output_file = "output.txt"

# Writing the cleaned data to a text file
with open(output_file, 'w') as file:
    for perm in all_permutations:
        perm_1 = str(perm).replace(",", "").replace("(", "").replace(")", "")
        #print(perm_1)
        file.write(perm_1 + '\n')
