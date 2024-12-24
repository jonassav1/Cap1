from dotenv import load_dotenv
import requests
import os
import time

load_dotenv()

api_key = os.getenv("my_key")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def handle_invalid_input():
    print("\nYou entered invalid selection number. Please try again!\n")
    time.sleep(1.5)
    clear_screen()


def main():
    while True:
        try:
            print("\n1. Add books to your collection.")
            print("\n2. Edit books in your collection.")
            print("\n3. Remove books from your collection.")
            print("\n4. Generate a book recommendation.")
            print("\n5. Exit the program.")
            selection = int(
                input("\nEnter a number of an option of what you would like to do: ")
            )
            clear_screen()
            if selection == 1:
                ...
            elif selection == 2:
                ...
            elif selection == 3:
                ...
            elif selection == 4:
                ...
            elif selection == 5:
                print(
                    "\nExiting the program! Thanks for using book recommendation and management tool!"
                )
                break
            else:
                handle_invalid_input()
        except ValueError:
            handle_invalid_input()


if __name__ == "__main__":
    main()
