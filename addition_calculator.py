def integer_checker(item):
    """Checks if the item is an integer, otherwise displays an error message."""
    try:
        item = int(item)
    except ValueError:
        print("Let's restart! Please, use only integers this time.")
        return False
    else:
        return True
print("Let's add two numbers together and avoid errors. Type 'q' to quit.")
prompt= 'Input a number: '
quit_message = "You have quit the program. Have a nice day!"
while True:
    first_number = input(prompt)
    if first_number == 'q':
        print(quit_message)
        break
    else:
        if integer_checker(first_number):
            second_number = input(prompt)
            if second_number == 'q':
                print(quit_message)
                break
            else:
                if integer_checker(second_number):
                    print(f"{first_number} + {second_number} = {int(first_number) + int(second_number)}")