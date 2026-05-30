def karatsuba(X, Y):
    # Base case
    if X < 10 and Y < 10:
        return X * Y

    # Find the maximum length of the numbers
    n = max(len(str(X)), len(str(Y)))
    m = n // 2

    # Split the numbers
    X1 = X // (10 ** m)
    X0 = X % (10 ** m)
    Y1 = Y // (10 ** m)
    Y0 = Y % (10 ** m)

    # Recursive calls
    z0 = karatsuba(X1, Y1)
    z1 = karatsuba(X1 + X0, Y1 + Y0)
    z2 = karatsuba(X0, Y0)

    # Karatsuba formula
    ans = z0 * (10 ** (2 * m)) + (z1 - z0 - z2) * (10 ** m) + z2

    return ans


# Input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Output
result = karatsuba(a, b)
print("Product =", result)
