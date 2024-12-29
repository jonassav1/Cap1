import requests
from dotenv import load_dotenv
import os
import csv

load_dotenv()
api_key = os.getenv("my_key")


class Book:
    def __init__(self, book_id, title, author, rating, genre):
        self.id = book_id
        self.title = title
        self.author = author
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"ID : {self.id}, Title: {self.title}, Author: {self.author}, Rating: {self.rating}, Genre: {self.genre}"


def check_book_file():
    try:
        with open("collection.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    return True
        return "\nCurrently there are no books in a file.\n"
    except FileNotFoundError:
        return "\nCurrently there are no books in a file.\n"


def save_books_to_file(data):
    try:
        with open("collection.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)
    except Exception as e:
        print(f"\nAn error occured while trying to save books to the file {e}")


class Book_Manager:
    def __init__(self):
        self.books = []
        self.load_books_from_file()

    def load_books_from_file(self):
        check = check_book_file()
        if check == True:
            with open("collection.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.books.append(row)

    def view_books(self):
        check = check_book_file()
        if check == True:
            with open("collection.csv", "r") as f:
                print("\n")
                reader = csv.reader(f)
                for row in reader:
                    print(
                        f"Book ID:{row[0]}, Title: {row[1]}, Author: {row[2]}, Rating: {row[3]}, Genre: {row[4]}"
                    )

    def add_books(self):
        id = len(self.books) + 1
        title = input("\nEnter book title: ")
        author = input("\nEnter book author: ")
        genre = input("\nEnter book genre: ")
        if not title or not author or not genre:
            print("\nInvalid input. Enter required information.")
            return self.add_books()
        while True:
            rating = input("\nEnter book rating(0-5): ")
            try:
                rating = float(rating)
                if rating < 0 or rating > 5:
                    print("\nRating must be between 0 and 5.")
                else:
                    break
            except ValueError:
                print("\nRating must be a number.")
        save_books_to_file([id, title, author, rating, genre])
        print("\n\nBook has been added to file!")

    def remove_books(self):
        check = check_book_file()
        print(check)


class Book_Recommendation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.book = []

    def get_book_recommendation_from_api(): ...

    def view_book_recommendation(): ...

    def save_book_recommendation(): ...


class Book_Search:
    def __init__(self):
        pass
