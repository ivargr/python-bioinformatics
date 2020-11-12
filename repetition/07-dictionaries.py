


gene_expressions = {}
gene_expressions["LXR"] = 100
#print(gene_expressions)
#print("GATA" in gene_expressions)
#print("LXR" in gene_expressions)
#print(gene_expressions["LXR"])
#print(gene_expressions["GATA"])


f = open("genes.tsv")
for line in f:
    splitted_line = line.strip().split(",")
    name = splitted_line[0]
    expression = float(splitted_line[1])

    gene_expressions[name] = expression

#print(gene_expressions)

print(gene_expressions["gene3"])


