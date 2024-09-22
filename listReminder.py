number = int(input("Add the number of coworkers: "))
numbers = []

# Loop for getting coworkers' information
for i in range(1, number + 1):
    coworkers = {
        "Name": input("Name: "),
        "familyName": input("Family Name: "),
        "age": int(input("Age: "))
    }
    numbers.append(coworkers)

# Print the list of coworkers
print(numbers)

# Loop for calculating coworkers' ages in days
number_of_coworkers = int(input("How many coworkers for the birthday list? "))
birthday = []
for i in range(1, number_of_coworkers + 1):
    age_in_years = int(input(f"How old is coworker {i}? "))
    birthday.append(365 * age_in_years)

# Print the list of ages in days
print(birthday)

# Generate and print a list of numbers multiplied by 365
number = int(input("Add your number here: "))
print([365 * i for i in range(1, number + 1)])

# Generate and print a list of numbers from 1 to `number`
number = int(input("Add your number here: "))
numbers = [i for i in range(1, number + 1)]
print(numbers)
