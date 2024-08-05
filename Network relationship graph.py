import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


G = nx.Graph()
file_path = r'C:\Users\Administrator\OneDrive\your.xlsx'  # Excel path
excel_data = pd.read_excel(file_path, sheet_name='Sheet1')
#  DataFrame to list
data = [(row['P1'], row['P2'], row['NUM']) for index, row in excel_data.iterrows()]
excel_data2 = pd.read_excel(file_path, sheet_name='Sheet2')
size = dict(excel_data2.values)
# add point and line
for a, b, weight in data:
    G.add_edge(a, b, weight=weight)

pos = nx.kamada_kawai_layout(G)
# color
node_color_rgba = (0.5, 0.5, 0.5, 0.5)  # RGBA
edge_color_rgba = (0.5, 0.5, 0.5, 0.5)  # RGBA
min_weight = min(weight for _, _, weight in data)
max_weight = max(weight for _, _, weight in data)
edge_widths = [(weight - min_weight) / (max_weight - min_weight) * 5 + 1 for _, _, weight in data]
# adjust widths
edges, widths = zip(*[(edge, edge_widths[i]) for i, edge in enumerate(G.edges())])
# adjust node size
node_sizes = [size[node] * 4 for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_size=node_sizes, font_size=18, node_color=node_color_rgba, edge_color=edge_color_rgba, width=widths)
# adjust labels weights
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=9, label_pos=0.6, bbox=dict(facecolor='none', edgecolor='none', alpha=0))
plt.suptitle("Fig.1 The hybridization relationship of 21 parents")
plt.show()
