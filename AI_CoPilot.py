Here is an AI chatbot program that helps the user run the "main.py" program locally on their PC:

```python
import os

def run_program():
    # Check if main.py exists in the current directory
    if "main.py" not in os.listdir():
        print("main.py file not found in the current directory.")
        return

    # Run main.py
    os.system("python main.py")

def main():
    print("Welcome to the Program Runner Chatbot!")
    print("This chatbot will help you run the 'main.py' program locally on your PC.")

    while True:
        print("\n======== MENU =======")
        print("1. Run Program")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
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

To use the AI chatbot, simply run the above Python program. It will provide a menu with options to run the "main.py" program or exit the chatbot.