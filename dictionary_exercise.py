programmer = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "years_coding": input("Enter the number of years you've been coding: ")
}

first = tuple(input("What were the first three programming languages you learned? ").split(" "))

favorite = input("What are your three favorite programming languages you learned? ").split(" ")

first_favorites = set(first).intersection(set(favorite))

programmer["first"] = first
programmer["favorite"] = favorite
programmer["first_favorites"] = first_favorites

print(programmer)