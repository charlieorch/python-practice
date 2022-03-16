

class OutOfRangeException(Exception): pass

def user_input():
    while True:
        choice = input("Would you like to enter an integer number ocler a float number(i for integer/f for float)? ").lower()
        if(choice == "i" or choice == "f"):
            if choice == "i":
                while True:
                    try:
                        number = int(input("Please enter a number(integer): "))
                        if(number < 0 or number > 500):
                            raise OutOfRangeException
                        return number
                    except ValueError:
                        print("Number must be an integer")
                    except OutOfRangeException:
                        print("Number(integer) must be greater than 0 or less than 500")
            if choice == "f":
                while True:
                    try:
                        number = float(input("Please enter a number(float): "))
                        if(number < 0 or number > 500):
                            raise OutOfRangeException
                        return number
                    except ValueError:
                        print("Number must be an float")
                    except OutOfRangeException:
                        print("Number(float) must be greater than 0 or less than 500")
        else:
            print("Please enter a valid choice.")


print(user_input())
