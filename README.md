# Traffic Management System Using Graphs

## Overview
This project implements a graph-based traffic management system using NetworkX and Streamlit. The application models road networks as a bidirectional graph, where intersections are nodes and roads are edges with weights representing traffic conditions (distance, congestion, or time). The system calculates the shortest path between two intersections using Dijkstra's Algorithm and visually represents the network.

## Features
- **Graph Representation**: Intersections and roads modeled as a weighted, bidirectional graph.
- **Shortest Path Calculation**: Uses Dijkstra's algorithm to determine the optimal route.
- **Interactive Visualization**: Displays the network and highlights the computed shortest route.
- **User Input**: Users select start and destination points via dropdowns.
- **Real-World Mapping**:

      A → Tinkune
      B → New Baneshwor
      C → Kalanki
      D → Maharajgunj
      E → Chabahil
      F → Koteshwor
      G → Jawalakhel
      H → Suryabinayak

## Installation
### Prerequisites
Ensure you have Python 3.7+ installed along with the following dependencies:

_pip install streamlit networkx matplotlib_

### Running the Application
Run the Streamlit app with:

_streamlit run app.py_

## How It Works
**Select Start and Destination**: Choose intersections from dropdown menus.
**Compute Shortest Path**: Click the button to calculate the optimal route.
**Visualize**: The network graph highlights the computed shortest route in red.

## Technologies Used
**Python**: Backend processing
**NetworkX**: Graph processing and shortest path computation
**Matplotlib**: Visualization
**Streamlit**: Interactive UI

## Alternative Approaches Considered
**Grid-Based Traffic Modeling**: Simplistic but inaccurate for irregular road layouts.
**AI-Driven Optimization**: Computationally heavy but useful for real-time predictions.
**Queue-Based Traffic Simulation**: Good for traffic flow prediction but lacks direct routing efficiency.
