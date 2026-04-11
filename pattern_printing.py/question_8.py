"""
Print this given pattern => 

        A
      A B 
    A B C 
  A B C D 
A B C D E
 
"""

n= 5
for i in range(1, n+1):
    for j in range(1, (n+1)-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(chr(64+k), end=" ")
    print()