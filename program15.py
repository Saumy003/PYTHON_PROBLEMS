# Write a function to calculate and return the square of a number

def square(num):
    return num ** 2 

num = float(input("enter a number:"))
result = square(num)
print(result)


# Create a function that take multiple number as parameters and return their sum
def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

sum_result = sum(1,3,5,6)
print(sum_result)