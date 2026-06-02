user_one_details = []
user_two_details = []

user_one_name = input("User one, enter your name: ")
user_one_details.append(user_one_name)
user_one_age = int(input("User one, enter you age: "))
user_one_details.append(user_one_age)
user_one_height = float(input("User one, enter your height: "))
user_one_details.append(user_one_height)


user_two_name = input("User two, enter your name: ")
user_two_details.append(user_two_name)
user_two_age = int(input("User two, enter you age: "))
user_two_details.append(user_two_age)
user_two_height = float(input("User two, enter your height: "))
user_two_details.append(user_two_height)

print(user_one_details)
print(user_two_details)

users = [user_one_details, user_two_details]

for user in users:
    print(f"{user[0]} is {user[1]} years old and {user[2]}cm tall.")

import combined_height_funtion
users_combined_height = combined_height_funtion.combined_height(user_one_height, user_two_height)
print(f"Combined height is: {users_combined_height}cm")