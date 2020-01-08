# -*- coding: utf-8 -*-
import networkx as nx
import csv
import matplotlib.pyplot as plt

# Set alpha coefficient
alpha = 0.2

# Generate Instance
g = nx.DiGraph()

# Read data
data = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

# Add nodes
for element in data:
    if not element[0] == "":
        g.add_node(element[0])

# Add edges
for element in data:
    if not element[0] == "":
        from_element = element[0]
        for to_element in element[1:]:
            if not to_element == "":
                g.add_edge(from_element, to_element)

# Calculate with PageRank alghorithm
pagerank = nx.pagerank(g,alpha=alpha)

# Output result
n = len(pagerank)
for key, value in zip(pagerank.keys(), pagerank.values()):
    print("{}\t{}".format(key, value * n * 20))
