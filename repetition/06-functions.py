

def read_genes_into_list(file_name):
    f = open("genes.tsv")
    genes = []
    for line in f:
        splitted_line = line.strip().split(",")
        gene_name = splitted_line[0]
        expression_value = float(splitted_line[1])

        genes.append([gene_name, expression_value])

    return genes


def print_genes_with_expression_value_above(gene_list, minimum_value):
    for gene in gene_list:
        if gene[1] > minimum_value:
            print(gene[0])


genes = read_genes_into_list("genes.tsv")

print_genes_with_expression_value_above(genes, 100)

print("Highly expressed genes")
print_genes_with_expression_value_above(genes, 500)
