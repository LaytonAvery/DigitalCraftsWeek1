meal_total = float(input("Enter the total amount of your meal: "))

tip_percentage = float(input("What percent would you like to tip?: "))

total_tip = meal_total * tip_percentage


def calculate_tip(total_tip):
    return total_tip


message = f"Your tip will be {total_tip} dollar."
print(message)
