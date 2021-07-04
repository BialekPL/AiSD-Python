#zadanie 3 - A*
from heapq import heappop, heappush, heapify

#counting nodes from zero
h = {0: 4, 1:8, 2:3, 3:4, 4:5, 5:2, 6:1, 7:0}

def A_asterisk(neighbour_matrix):
    Q = []
    Q_nodes = []
    S = []
    pred = [-1] * len(neighbour_matrix)
    # declaring start and end node
    start = 0
    end = 7
    cost = 0
    v = None
    heappush(Q, (0, start))
    Q_nodes.append(start)
    while len(Q) > 0:
        n = heappop(Q)
        if v is not None:
            cost += neighbour_matrix[v][n[1]]
        v = n[1]
        Q_nodes.remove(v)
        S.append(v)
        # analizing neighbours:
        for node, weight in enumerate(neighbour_matrix[v]):
            if weight != 0.0 and weight != float('inf'):
                if not node in S:
                    if not node in Q_nodes:
                        heappush(Q, (cost+weight+h[node], node))
                        Q_nodes.append(node)
                        pred[node] = v   
                    
        if v == end: break
    return pred, S

# using an example from 03_algorytmy_grafowe.pdf page 12 picture 6, but i count from zero
matrix = [[float(x) for x in line.split()] for line in open("A_asterisk_input.txt").readlines()]
res = A_asterisk(matrix)
print(f"pred: {res[0]}") # result is good but shifted one behind since i count from zero
print(f"S: {res[1]}")
