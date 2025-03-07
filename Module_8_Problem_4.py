#Martha Moreno Gonzalez
#03/06/2025
#identifies if there is a leap year
def is_it_leap_year():
    year = int(input("What year are you trying to check if its a leap year : "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It is a leap year!")
        return True
    else:
        print("It is not a leap year")
        return False
is_it_leap_year()
        

