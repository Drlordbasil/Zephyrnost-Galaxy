Sure! Here's the refactored version of the script:

```python

import os


def run_program(program_name):
    if not os.path.isfile(program_name):
        print(f"{program_name} file not found in the current directory.")
        return

    os.system(f"python {program_name}")


def main():
    print("Welcome to the Program Runner Chatbot!")
    print("This chatbot will help you run a program locally on your PC.")

    while True:
        print("\n======== MENU =======")
        print("1. Run Program")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

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

In this refactored version, the `PROGRAM_NAME` constant has been removed and replaced with user input within the `main` function. This allows the user to enter the name of any program they want to run, making the code more flexible.