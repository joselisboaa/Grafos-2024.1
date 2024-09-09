from collections import deque, defaultdict

def dijkstra_bfs(graph, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for next, weight in graph[current]:
            if distances[current] + weight < distances[next]:
                distances[next] = distances[current] + weight
                queue.append(next)
    
    return distances

test = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
distances = dijkstra_bfs(test, start_vertex)
print(f"Distâncias a partir do vértice {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Distância para {vertex}: {distance}")
