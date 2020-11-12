

f = open("sequences.fasta")

#for line in f:
#    print(line.strip())


# Print only short sequences
f = open("sequences.fasta")
for line in f:
    if line.startswith(">"):
        # Do nothing, skip this line
        pass
    else:
        if len(line) < 15:
            print(line)






