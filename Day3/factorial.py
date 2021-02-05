number = int(input("Enter a number: "))


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


message = f"The factorial for {number} is {factorial(number)}."
print(message)
