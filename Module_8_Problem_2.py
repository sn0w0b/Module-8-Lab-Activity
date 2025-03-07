#Martha Moreno Gonzalez
#03/06/2025
#takes two inputs from a user and prints whether the sum is greater than 10,
#less than 10, or equal to 10.

def the_sum():
    x = int(input("First # you want to add: "))
    y = int(input("Second # you want to add: "))

    total = x + y 

    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sume is less than 10.")
    else:
        print("The sum is equal to 10.")
the_sum()