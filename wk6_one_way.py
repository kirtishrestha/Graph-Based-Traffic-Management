import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Mapping intersections to real-world locations
intersections = {
    "A": "Tinkune",
    "B": "New Baneshwor",
    "C": "Kalanki",
    "D": "Maharajgunj",
    "E": "Chabahil",
    "F": "Koteshwor",
    "G": "Jawalakhel",
    "H": "Suryabinayak"
}

G.add_nodes_from(intersections.keys())

roads = [
    ("A", "B", 4), ("A", "C", 2),
    ("B", "C", 1), ("B", "D", 5), ("B", "E", 7),
    ("C", "D", 8), ("C", "F", 10),
    ("D", "E", 2), ("D", "G", 6),
    ("E", "G", 3),
    ("F", "G", 9), ("F", "H", 4),
    ("G", "H", 5)
]
G.add_weighted_edges_from(roads)

st.title("Traffic Management System Using Graphs")
st.write("Select intersections to find the shortest route based on traffic conditions.")

start = st.selectbox("Select Starting Intersection", list(intersections.keys()), format_func=lambda x: intersections[x])
destination = st.selectbox("Select Destination Intersection", list(intersections.keys()), format_func=lambda x: intersections[x])

if st.button("Find Shortest Route"):
    if start == destination:
        st.warning("Start and destination must be different!")
    else:
        shortest_path = nx.dijkstra_path(G, source=start, target=destination, weight="weight")
        st.write(f"Shortest Path: {' → '.join([intersections[node] for node in shortest_path])}")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(G, seed=42)
        
        nx.draw(G, pos, with_labels=True, labels=intersections, node_size=2000, node_color="lightblue", font_size=10, edge_color="gray", width=2, ax=ax)
        
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3, ax=ax)
        
        edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)
        
        st.pyplot(fig)
