# Program to add digits of a number
n=input("Enter a number: ")
count=0
if (n.isnumeric()) :
    for i in range(0,len(n)):
        count=count+int(n[i])
    print("Sum of digits of the given number:",count)

else:
    print("Given input is not a number. Please enter a number")

    



