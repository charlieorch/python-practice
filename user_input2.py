full_name = input("Enter your first and last name, seperated by a comma: ").split(", ")
first_name = full_name[0].capitalize()
last_name = full_name[1].capitalize()
print(f"Last name: {last_name}, First name: {first_name}")

age = int(input("Enter your age: "))
year = 2022 - age
print("Age:", age, "Year:",year)

email = f"{full_name[0].lower()}.{full_name[1].lower()}{year%100}@company.com"
print(email)


