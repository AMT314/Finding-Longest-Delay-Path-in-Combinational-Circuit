# Finding Longest Delay Path in Combinational Circuit using Directed Acyclic Graph

## Overview
This project implements an algorithm to compute the longest weighted path in a Directed Acyclic Graph (DAG), representing a digital circuit netlist. By leveraging topological sorting and dynamic programming, the approach efficiently determines the critical delay path.

## Features
- **Adjacency List Representation:** The netlist is stored using an adjacency list for efficient traversal. Each edge (gate/net) is represented by its source node, destination node, and associated weight.
- **Topological Sorting:** Kahn's algorithm is used to generate a valid topological order of nodes in the DAG, ensuring each node is processed only after all its predecessors.
- **Dynamic Programming Approach:** Iterating through the topological order, the algorithm dynamically computes the maximum path weight for each node, updating paths accordingly. Primary inputs initialize the computation with a path weight of zero.
- **Path Extraction:** The longest weighted path is determined by comparing computed weights of all primary outputs, ultimately identifying the circuit’s critical delay path.

## Dependencies
- Python 3.13
- Google Colab or other platform for Python coding

## Example 
Circuit:
![image](https://github.com/user-attachments/assets/2221673a-0323-4fcf-8fa3-6c8df33207da)
Result:
![image](https://github.com/user-attachments/assets/b9cd3e10-f035-4d45-a79e-6997694f9b65)
