"""
Print this given pattern => 

          *
        * * *
      * * * * *
        * * * 
          *
    
"""

n = 3
for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()

m = 2
for p in range(1, m+1):
    for q in range(1,p+1):
        print(" ", end=" ")
    for r in range(1,2*(m-p)+2 ):
        print("*", end=" ")
    print()