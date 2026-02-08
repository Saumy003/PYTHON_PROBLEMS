## program to find square root

#method1(exponentional method)

num1 = int(input("enter number:"))
sq_root = num1 ** 0.5
print("square root of given number is", sq_root)

#method2(math module)

import math

num2 = int(input("enter the number here:"))
sqRoot = math.sqrt(num2)

print("square root of given number is" , sqRoot)