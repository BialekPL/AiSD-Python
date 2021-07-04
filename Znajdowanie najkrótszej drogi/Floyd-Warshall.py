#zadanie 3 - Floyd-Warshall
def floyd_Warshall(d):
    p = [row[:] for row in d]
    # initializing p with i's nad zeros
    for row, i in enumerate(p):
        for column, j in enumerate(i):
            if p[row][column] != 0.0 and p[row][column] != float('inf'):
                p[row][column] = row
            else:
                p[row][column] = -1
    for u in range(len(d)):
        for v in range(len(d)):
            for w in range(len(d)):
                if u!=v and v!=w and u!=w:
                    l = d[v][u] + d[u][w]
                    if l < d[v][w]:
                        d[v][w] = l
                        p[v][w] = p[u][w]

    return d, p
# im using the example from 03_algorytmy_grafowe.pdf page 15 picture 7, but i count from zero
matrix = [[float(x) for x in line.split()] for line in open("Floyd_Warshall_input.txt").readlines()]
dp = floyd_Warshall(matrix)
print("d:")
for row in dp[0]:
    print(row)
# again, i count nodes from 0 so they shifted one behind
print("p:")
for row in dp[1]:
    print(row)