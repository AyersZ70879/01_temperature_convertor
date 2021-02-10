# This component is used to check that a users entered number is within given parameters


# Temp Number Checker function
def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too Cold!")

            else:
                return response

        except ValueError:
            print("Please enter a number")

# main routine
number = temp_check(-273)
print("You chose {}".format(number))

# number = temp_check(-459)
# print("You chose {}".format(number))
