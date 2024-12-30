import requests
import os
import csv
import random
import json


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
        print("\nCurrently there are no books in a file.\n")
        return False
    except FileNotFoundError:
        print("\nCurrently there are no books in a file.\n")
        return False


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
        self.recommended_books = []

    def get_book_recommendation_menu(self):
        try:
            selection = int(
                input(
                    "\nWould you like to search get book recommendation by author(1) or genre(2)?"
                )
            )
            if selection == 1:
                self.get_book_recommendation_from_api_author()
            elif selection == 2:
                self.get_book_recommendation_from_api_genre()
            else:
                print("\nYou entered invalid number. Please try again.")
                return self.get_book_recommendation_menu()
        except ValueError:
            print("\nYou entered invalid number. Please try again.")
            return self.get_book_recommendation_menu()

    def get_book_recommendation_from_api_genre(self, max_results=3):
        genre = input("\nEnter the genre: ").strip()
        try:
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&maxResults={max_results}&key={self.api_key}"
            )
            response.raise_for_status()
            info = response.json()
            if "items" in info:
                print("\nHere are the book recommendations: ")
                for item in info["items"]:
                    volume_info = item["volumeInfo"]
                    title = volume_info.get("title")
                    authors = volume_info.get("authors")
                    genres = volume_info.get("categories")[0]
                    rating = volume_info.get("averageRating", None)
                    if rating is None:
                        continue
                    print(f"\nTitle: {title}")
                    print(f"Author: {', '.join(authors)}")
                    print(f"Genre: {genres}")
                    print(f"Rating: {rating}")
            else:
                print("\nNo books found in this genre.")
        except requests.exceptions.RequestException as e:
            print(f"\nError fetchiing books by author: {e}")

    def get_book_recommendation_from_api_author(self, max_results=3): ...

    def save_book_recommendation(self, title, author, genre, rating): ...
