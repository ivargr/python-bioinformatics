import sys

def sequence_is_valid(sequence):
	
	for n in sequence:
		if n != "A" and n != "G" and n != "T" and n != "C" and n != "N":
			return False
	return True
		

def compute_gc_content(sequence):
	n_c = sequence.count("C")
	n_g = sequence.count("G")
	length = len(sequence)

	return (n_c + n_g) / length


sequence = sys.argv[1]

if sequence_is_valid(sequence):

	result = compute_gc_content(sequence)
	print(result)
else:
	print("You need to provide a valid sequence")


