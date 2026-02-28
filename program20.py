# Write a Python program to print the Fibonacci sequence using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# number of terms
terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
