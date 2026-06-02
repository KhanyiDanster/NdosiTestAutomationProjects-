user_one_name = input("User one, enter your name: ")
user_one_age = int(input("User one, enter you age: "))
user_one_height = float(input("User one, enter your height: "))

user_two_name = input("User two, enter your name: ")
user_two_age = int(input("User two, enter you age: "))
user_two_height = float(input("User two, enter your height: "))

print(f"User one your name is {user_one_name},you are {user_one_age} years old and your height is {user_one_height}cm.")
print(f'User two your name is {user_two_name}, you are {user_two_age} years old and your height is {user_two_height}cm.')
combined_height = user_one_height + user_two_height
print(f"Your combined height is: {combined_height}.")