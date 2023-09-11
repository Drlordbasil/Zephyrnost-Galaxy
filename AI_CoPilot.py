import os
Thank you for the suggestions! Here is the optimized code with the improvements you provided:

```python

PROGRAM_NAME = "main.py"


def run_program():
    if not os.path.isfile(PROGRAM_NAME):
        print(f"{PROGRAM_NAME} file not found in the current directory.")
        return

    os.system(f"python {PROGRAM_NAME}")


def main():
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
            run_program()
        elif choice == 0:
            print("Exiting chatbot...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

I hope this helps optimize the code! Let me know if you need any further assistance.
