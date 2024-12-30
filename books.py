import requests
from dotenv import load_dotenv
import os
import csv
import random

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


def generate_ids():
    existing_ids = []
    try:
        with open("collection.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                existing_ids.append(int(row[0]))
        random_id = random.randint(1, 1000)
        if random_id not in existing_ids:
            return random_id
    except FileNotFoundError:
        return 1

class Book_Manager:
    def __init__(self):
        self.books = []
        self.load_books_from_file()

    def load_books_from_file(self):
        check = check_book_file()
        if check == True:
            with open("collection.csv", "r") as f:
                reader = csv.reader(f)
                self.books = [
                    Book(
                        book_id=row[0],
                        title=row[1],
                        author=row[2],
                        rating=row[3],
                        genre=row[4],
                    )
                    for row in reader
                ]

    def view_books(self):
        check = check_book_file()
        if check == True:
            for book in self.books:
                print(book)

    def add_books(self):
        id = generate_ids()
        title = input("\nEnter book title: ")
        author = input("\nEnter book author: ")
        genre = input("\nEnter book genre: ")
        if not title or not author or not genre:
            print("\nInvalid input. Enter required information.")
            return self.add_books()
        while True:
            try:
                rating = input("\nEnter book rating(0-5): ")
                rating = float(rating)
                if rating < 0 or rating > 5:
                    print("\nRating must be between 0 and 5.")
                else:
                    break
            except ValueError:
                print("\nRating must be a number.")
        new_book = Book(
            book_id=id, title=title, author=author, rating=rating, genre=genre
        )
        self.books.append(new_book)
        save_books_to_file(
            [
                new_book.id,
                new_book.title,
                new_book.author,
                new_book.rating,
                new_book.genre,
            ]
        )
        print("\n\nBook has been added to file!")

    def remove_books(self):
        check = check_book_file()
        if check == True:
            try:
                book_to_remove = int(
                    input("\nEnter ID of the book you would like to delete: ")
                )
            except ValueError:
                print("\nInvalid input! Enter a number ID.")
                return self.remove_books()
            updated_books = []
            with open("collection.csv", "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if int(row[0]) != book_to_remove:
                        updated_books.append(row)
            if len(updated_books) == len(self.books):
                print("\nNo book found with entered ID.")
            else:
                with open("collection.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_books)
                    print(
                        f"\nBook with ID {book_to_remove} has been deleted from the collection."
                    )

class Book_Recommendation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.book = []

    def get_book_recommendation_from_api(): ...

    def view_book_recommendation(): ...

    def save_book_recommendation(): ...
