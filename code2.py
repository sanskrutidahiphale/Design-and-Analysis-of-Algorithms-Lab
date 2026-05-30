# Fractional Greedy Knapsack

# Take inputs
n = int(input("Enter number of objects: "))
m = float(input("Enter capacity of sack: "))

weights = []
profits = []

for i in range(n):
    w = float(input(f"Enter weight of object {i + 1}: "))
    p = float(input(f"Enter profit of object {i + 1}: "))
    weights.append(w)
    profits.append(p)

# Compute profit/weight ratio
items = []
for i in range(n):
    ratio = profits[i] / weights[i]
    items.append((ratio, weights[i], profits[i]))

# Sort in descending order of ratio
items.sort(reverse=True)

# Apply Greedy Selection
total_profit = 0
remaining_capacity = m

for ratio, weight, profit in items:
    if remaining_capacity == 0:
        break

    if weight <= remaining_capacity:
        # Take full item
        remaining_capacity -= weight
        total_profit += profit
    else:
        # Take fractional part
        fraction = remaining_capacity / weight
        total_profit += profit * fraction
        remaining_capacity = 0

# Output
print("\nMaximum Profit =", total_profit)