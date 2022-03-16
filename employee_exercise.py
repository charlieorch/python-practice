employee_list = []
max_employees = 3
num_employees = 0
class NumberEmployeesException(Exception): pass
class AgeException(Exception): pass

while True:
    try: 
        num_employees = int(input("How many employees will you add? "))
        if num_employees >= max_employees:
            raise NumberEmployeesException
    except ValueError:
        print("Number of eomplyees must be an integer")
    except NumberEmployeesException:
        print(f"Number of employees must be less than {max_employees}")
    else: break

counter = 1
while counter <= num_employees:
    employee = {}
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 18:
                raise Exception
            
            year = 2022 - age
            
            full_name = input("Enter your first and last name, sepearated by a comma: ").split(", ")
            first_name = full_name[0].capitalize()
            last_name = full_name[1].capitalize()
            email = f"{full_name[0].lower()}.{full_name[1].lower()}{year%100}@comapny.com"

            employee["name"] = full_name
            employee["email"] = email
            employee["id"] = counter

            employee_list.append(employee)
        except ValueError:
            print("Age must be an int")
        except Exception:
            print("You must be 18 or over to work here.")
            break
        else: 
            break
    counter += 1