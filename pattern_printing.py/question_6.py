"""
Print this given pattern => 

    *
   **
  ***
 ****
*****

"""

n = 5

for i in range(1, n + 1):
    # print spaces
    for spaces in range(1, n+1 - i):
        print(" ", end="")
    
    # print stars
    for k in range(1, i+1):
        print("*", end="")
    
    print()  # move to next line
