## pattern 1
for row in range(1 ,6):
    for column in range(1 , row+1):
        print("*" , end= " ")
    print()


## pattern 2
for i in range(1 ,5):
    for j in range(1 , 5):
        print("*" , end= " ")
    print()

## pattern 3
for a in range(1,6):
    for b in range(1,a+1):
        print(b , end = " ")
    print()