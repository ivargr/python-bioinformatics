import sys



# Exercise 2
def sequence_has_pattern(reference_sequence, query_sequence):

	# Exercise 1 (only the code below outside a function)
	if query_sequence in reference_sequence:
		return True
	else:
		return False


# Exercise 3

"""
f = open("sequences.txt")
for line in f:
	line = line.strip()
	
	if sequence_has_pattern(line, "TTC"):
		print(line)
	
	print(line)
"""

# Exercise 4
def read_sequences_from_file(file_name):

	sequences = []

	f = open(file_name)
	for line in f:
		line = line.strip()
		sequences.append(line)
		
	return sequences


def get_sequences_with_pattern(list_of_sequences, query_sequence):
	matched_sequences = []
	for sequence in list_of_sequences:
		if sequence_has_pattern(sequence, query_sequence):
			matched_sequences.append(sequence)
			
	return matched_sequences

file_name = sys.argv[1]
query_sequence = sys.argv[2]

sequences = read_sequences_from_file(file_name)
sequences_with_match = get_sequences_with_pattern(sequences, query_sequence)

for seq in sequences_with_match:
	print(seq)




