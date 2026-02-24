# WAP to print the following patterns using loops:-
for row in range(1 , 5):
    for column in range(1, row+1):
        print("*" , end=" ")
    print()

# Write a program to write multiplication table of 8, 15, 69.
for i in range(1 , 11):
    print(8 * i)

for j in range(1 , 11):
    print(69 * j)

# Wap to check ehether the given input is digit , uppercase or lowercase & special char.

choice = input("Enter a character:")

if len(choice) != 1:
    print("Please enter only a single character.")
else:
    if choice >= "0" and choice <= "9":
        print("It is a digit.")
    elif choice >= "a" and choice <= "z":
        print("It is a lowercase character.")
    elif choice>= "A" and choice <= "Z":
        print("It is an uppercase character.")
    else:
        print("It is a special character.")
