#zadanie 3 - Djikstra
from heapq import heappop, heappush, heapify
def dijkstra(neighbour_matrix):
    pred = [-1] * len(neighbour_matrix)
    dist = [float('inf')] * len(neighbour_matrix)
    Q = [(float('inf'), i) for i in range(len(neighbour_matrix))]
    Q_nodes = [x[1] for x in Q]
    s = 0
    dist[s] = 0
    Q[Q_nodes.index(s)] = (0, s)
    heapify(Q)
    
    while len(Q) > 0:
        v = heappop(Q)[1]
        Q_nodes.remove(v)
        for u, weight in enumerate(neighbour_matrix[v]):
            # if theres a connection:
            if weight != 0.0 and weight != float('inf'):
                d = dist[v] + neighbour_matrix[v][u]
                if d < dist[u]:
                    dist[u] = d
                    pred[u] = v # according to pdf page 10 there should be u but i think its typo
    return pred, dist

# using an example from 03_algorytmy_grafowe.pdf page 8 picture 4
# same as in Prima, result same as in example from platforma but pred elements shifted by 1
matrix = [[float(x) for x in line.split()] for line in open("Prima_Djikstra_input.txt").readlines()]
print(f"pred: {dijkstra(matrix)[0]}, dist: {dijkstra(matrix)[1]}")

