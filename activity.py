import heapq

graph = [[] for i in range(23)]

def add(u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

add(1, 2, 1)
add(1, 11, 1)
add(2, 3, 1)
add(2, 21, 1)
add(3, 4, 1)
add(3, 8, 2)
add(4, 5, 1)
add(5, 6, 2)
add(5, 7, 1)
add(5, 22, 1)
add(6, 7, 2)
add(7, 8, 2)
add(8, 9, 1)
add(9, 10, 1)
add(9, 19, 2)
add(10, 11, 1)
add(10, 18, 2)
add(11, 12, 2)
add(11, 17, 1)
add(12, 13, 2)
add(13, 14, 2)
add(13, 21, 1)
add(14, 15, 1)
add(14, 16, 1)
add(14, 20, 1)
add(16, 17, 2)
add(17, 18, 2)
add(18, 19, 2)
add(20, 21, 2)
add(20, 22, 1)
add(21, 22, 2)

distances = {i: float('inf') for i in range(23)} # initialize with inf dist

distances[1] = 0 # start at vertex 1

pq = [(0, 1)] # stores (distance, vertex)

while pq: 
    curr_dist, vertex = heapq.heappop(pq)

    for neighbor, weight in graph[vertex]:
        distance = curr_dist + weight
        if distance < distances[neighbor]: # update distance
            distances[neighbor] = distance 
            heapq.heappush(pq, (distance, neighbor))

# print(distances)

print("Question 4: The weights from Node 1 to the following:")
print(f"Node 6: {distances[6]}")
print(f"Node 8: {distances[8]}")
print(f"Node 9: {distances[9]}")
print(f"Node 15: {distances[15]}")
print(f"Node 16: {distances[16]}")
print(f"Node 22: {distances[22]}")


