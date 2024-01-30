import matplotlib.pyplot as plt
import networkx as nx

# Nodes represent different scenes or locations in the game
nodes = ["Crashed Ship", "Alien Forest", "Ancient Ruins", "Underground Caves", "Mysterious Lake", "Abandoned Outpost"]

# Edges represent possible paths between the scenes
edges = [("Crashed Ship", "Alien Forest"), ("Crashed Ship", "Ancient Ruins"),
         ("Crashed Ship", "Underground Caves"), ("Crashed Ship", "Mysterious Lake"),
         ("Crashed Ship", "Abandoned Outpost"), ("Alien Forest", "Ancient Ruins"),
         ("Alien Forest", "Mysterious Lake"), ("Ancient Ruins", "Underground Caves"),
         ("Underground Caves", "Abandoned Outpost"), ("Mysterious Lake", "Abandoned Outpost")]

# Create the graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define the layout for the graph
pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight="bold")
plt.title("Scene Layout Planar Graph")
plt.show()
