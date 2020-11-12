

f = open("genes.tsv")

for line in f:
    splitted_line = line.strip().split(",")

    gene_name = splitted_line[0]
    expression_value = float(splitted_line[1])

    #print(gene_name, expression_value)

    # Only print genes with expression value larger than 100
    if expression_value > 100:
        print(gene_name)
