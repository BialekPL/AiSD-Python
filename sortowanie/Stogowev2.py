from heapq import heappush, heappop
def heapSort(tab):
    heap = []
    for value in tab:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]

if __name__ == "__main__":
    
    tab = [4, 9, 12, 2, 1, 7, 16]
    print("Przed sortowaniem:")
    print(tab)
    tab = heapsort(tab)
    print("Po:")
    print(tab)