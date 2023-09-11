Certainly! Here's a refactored version of your script that improves performance and follows best practices:

```python
import os


def run_program(program_name):
    if not os.path.isfile(program_name):
        print(f"{program_name} file not found in the current directory.")
        return

    os.system(f"python {program_name}")


def get_user_choice():
    while True:
        print("\n======== MENU =======")
        print("1. Run Program")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            return int(choice)
        else:
            print("Invalid choice. Please try again.")


def main():
    print("Welcome to the Program Runner Chatbot!")
    print("This chatbot will help you run a program locally on your PC.")

    while True:
        choice = get_user_choice()

        if choice == 1:
            program_name = input("Enter the program name: ")
            run_program(program_name)
        elif choice == 0:
            print("Exiting chatbot...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```

In this refactored version, the `get_user_choice` function has been introduced to handle user input validation. It checks if the input is a digit and returns the integer value. This prevents any potential `ValueError` exceptions.

Additionally, the `PROGRAM_NAME` constant has been removed, and the user is prompted to enter the program name within the `main` function. This offers more flexibility to the user.

Finally, function and variable names have been made more descriptive, improving the readability of the code.