number = int(input("Enter a number"))
rev=0
x=number
while(number>0):
    rev=(rev*10)+ number % 10
    number = number//10
if(x==rev):
    print("Palindrome number")
else:
    print("Not Palindrome")