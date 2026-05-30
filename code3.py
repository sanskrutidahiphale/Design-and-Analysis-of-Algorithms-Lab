import heapq
import random

# Number of rooms
n = 15

# Create an empty graph
graph = {i: [] for i in range(n)}

# Randomly create passages between rooms
for i in range(n):
    for j in range(i + 1, n):
        # Randomly decide if passage exists
        if random.choice([True, False]):
            time = random.randint(1, 20)  # travel time
            graph[i].append((j, time))
            graph[j].append((i, time))  # undirected graph


# Dijkstra Algorithm
def dijkstra(graph, start, n):
    # Distance array
    dist = [float('inf')] * n
    dist[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip outdated entries
        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # Mark unreachable rooms as -1
    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1

    return dist


# Start from entrance room 0
result = dijkstra(graph, 0, n)

# Print dungeon passages
print("Dungeon Passages (Room -> Neighbor, Time):")
for room in graph:
    print(room, "->", graph[room])

# Print shortest distances
print("\nShortest Time from Entrance (Room 0):")
for i in range(n):
    print(f"Room {i} : {result[i]}")