import os
Optimized Python script:

```python


def run_program(program_name):
    if not os.path.isfile(program_name):
        print(f"{program_name} file not found in the current directory.")
        return

    os.system(f"python {program_name}")


def main():
    program_name = "main.py"

    print("Welcome to the Program Runner Chatbot!")
    print("This chatbot will help you run the 'main.py' program locally on your PC.")

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
            run_program(program_name)
        elif choice == 0:
            print("Exiting chatbot...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

The code has been optimized by moving the `PROGRAM_NAME` constant to the `main` function and passing it as an argument to the `run_program` function. This allows for a more flexible and modular code structure.
