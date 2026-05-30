import random

INF = float('inf')

# Input
while True:
    n = int(input("Enter number of caves (at least 8): "))
    if n >= 8:
        break
    else:
        print("Please enter a number >= 8")

# Create graph
dist = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            if random.choice([True, False]):
                row.append(random.randint(1, 20))
            else:
                row.append(INF)
    dist.append(row)


# Improved print function
def print_matrix(matrix, title):
    print("\n" + title)

    # Header row
    print("     ", end="")
    for j in range(n):
        print(f"{'C' + str(j + 1):>5}", end="")
    print()

    # Matrix rows
    for i in range(n):
        print(f"{'C' + str(i + 1):>5}", end="")
        for j in range(n):
            if matrix[i][j] == INF:
                print(f"{'∞':>5}", end="")
            else:
                print(f"{matrix[i][j]:>5}", end="")
        print()


# Print initial matrix
print_matrix(dist, "Initial Danger Matrix:")

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

# Print result
print_matrix(dist, "Safest Paths (Minimum Danger):")