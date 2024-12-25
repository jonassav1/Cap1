import requests
from dotenv import load_dotenv
import os
import csv
import time

load_dotenv()
api_key = os.getenv("my_key")


class Book:
    def init(self, title, author, rating, genre):
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


class Book_Manager:
    def __init__(self):
        pass

    def view_books(self):
        check = check_book_file()
        print(f"{check}")

    def add_books(self): ...

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
