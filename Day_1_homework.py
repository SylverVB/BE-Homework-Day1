# 1. Showcase Your Dance Moves!

# Task 1: Code correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


# Task 2: Your Mood Today

mood = input("What is your mood: happy or sad? ")

if mood == "happy" or mood == "Happy":
    print("That's great to hear!")
elif mood == "sad" or mood == "Sad":
    print("I hope your day gets better!")
else:
    print("That's not a valid option. Try again.")


# 2. Python Naming Convention Practice

# Task 1: Code Correction

# Correct:

PI_VALUE = 3.14             # Pi is a constant
user_age = 25               # Snake case
USER_LOCATION = "New York"  # It depends. If user location is constant, we should use upper case for this variable
MAX_LIMIT = 1000            # Snake case for the constant variable


# 3. Arithmetic Operations in Daily Life

bread_price = 4.5
peanut_butter_price = 2.25
jelly_price = 3.15

total = bread_price + peanut_butter_price + jelly_price

print(f'The total cost of three items is {total} dollars.')

# Task 2: Bank Interest

def total_money(money_on_savings_account, bank_interest):
    total_money = money_on_savings_account + money_on_savings_account * bank_interest / 100
    return total_money

print(total_money(money_on_savings_account=10000, bank_interest=7))
