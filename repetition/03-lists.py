

my_sequences = ["ACTG", "AAAAACCC", "ATTAGCCA", "AACACTG"]

for sequence in my_sequences:
    print(sequence)

# Note that variables defined outside the for-loop exists inside.
joined_sequences = ""
for sequence in my_sequences:
    joined_sequences = joined_sequences + sequence

print("All sequences joined together: ", joined_sequences)

# Note that string in itself also is iterable!
list_of_bases = []
for base in "AACCTTG":
    list_of_bases.append(base)

print(list_of_bases)
