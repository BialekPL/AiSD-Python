#zadanie 3 - Prima
from heapq import heappop, heappush, heapify
def prima(neighbour_matrix):
    # counting nodes from zero!
    pred = [-1 for _ in range(len(neighbour_matrix))]
    k = [float('inf')] * len(neighbour_matrix)
    #starting node s
    s = 0
    k[s] = 0
    #priority queue
    pq = []
    for v in range(len(neighbour_matrix)):
        heappush(pq, (float(k[v]), v))
    pq_nodes = [x[1] for x in pq]

    while len(pq) > 0:
        u = heappop(pq)[1]
        pq_nodes.remove(u)
        for v, weight in enumerate(neighbour_matrix[u]):
            # if theres a connection:
            if weight != 0.0 and weight != float('inf'):
                if v in pq_nodes:
                    if weight < k[v]:
                        pred[v] = u
                        k[v] = weight
                        pq[pq_nodes.index(v)] = (weight, v)
                        heapify(pq)
    return pred, k

# using an example from 03_algorytmy_grafowe.pdf page 8 picture 4
# result is correct but i count nodes from 0, so pred values are shifted one behind
matrix = [[float(x) for x in line.split()] for line in open("Prima_Djikstra_input.txt").readlines()]
print(prima(matrix))


