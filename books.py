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


class Book_Manager: ...
