"""
Print this given pattern => 

* 
**
***
****
*****
****
***
**
*

"""

for i in range(1, 6):
    for j in range(1, i +1):
        print("❤️", end=" ")
    print()
for p in range(1, 5):
    for q in range(1 , 6-p):
        print("❤️" , end=" ")
    print()