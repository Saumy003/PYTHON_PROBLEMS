"""
Print this given pattern => 

          *
         * *
        * * *
       * * * *
      * * * * * 
    
"""

n = 5
for rows in range(1, n+1):
    for spaces in range(1, (n-rows)+1):
        print(" ", end="")
    for cols in range(1, rows+1):
        print("*", end=" ")
    print()
   