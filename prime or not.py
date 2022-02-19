number = int(input("Enter a number"))
if number<2:
    print("Not a Prime number")
else:
    for i in range(2,number):
        if number % i==0:
            print("Not a Prime")
            break
    else:
        print("Number is Prime")
