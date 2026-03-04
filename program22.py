# WAP a program to check if the number is Armstrong or Not?

num = int(input("enter the number:"))
order = len(str(num))

sum = 0
temp = num

while temp >0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print("it is an armstrong number")
else:
    print("it is not an armstrong nnumber")
