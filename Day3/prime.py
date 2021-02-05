
def division():
    number = int(input("Please enter a number: "))
    for index in range(2, number-1):

        if number % index == 0:
            print("Not prime.")
            break
    print("Prime.")


division()
