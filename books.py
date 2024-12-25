import requests
from dotenv import load_dotenv
import os
import csv

load_dotenv()
api_key = os.getenv("my_key")


class Book:
    def __init__(self, title, author, rating, genre):
        self.title = title
        self.author = author
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Rating: {self.rating}, Genre: {self.genre}"


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
        with open ("collection.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)
    except Exception as e:
        print(f"\nAn error occured while trying to save books to the file {e}")

class Book_Manager:
    def __init__(self):
        pass

    def view_books(self):
        check = check_book_file()
        print(f"{check}")

    def add_books(self): ... #cia bus galima sudeti knyga kokia nori tada pasiusim zinute i book class kad bam knyga sudeta jei values gauna taisyklingai jas sudes i reikiamas vietas ir gausim tada saugoti jas i faila

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