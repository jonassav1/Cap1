import requests
from dotenv import load_dotenv
import os

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


def check_book_file(): ...


class Book_Manager:
    def __init__(self):
        pass

    def view_books():
        pass

    def add_books():
        pass

    def remove_books():
        pass


class Book_Recommendation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.book = []

    def get_book_recommendation_from_api(): ...

    def view_book_recommendation(): ...

    def save_book_recommendation(): ...
