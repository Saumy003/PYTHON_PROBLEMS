## WAP to display all prime numbers within an interval of 20 and 50

for num in range(20,51):
    if(num > 1 ) :
        for i in range(2 , num):
            if(num % i == 0):
                break
        else:
            print(num)
                