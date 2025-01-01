import pytest
from books import Book
from books import genre_check


def test_book_str():
    book = Book(1, "test", "tester", 0, "testing")
    assert str(book) == "ID : 1, Title: test, Author: tester, Rating: 0, Genre: testing"


def test_genre_check():
    assert genre_check("fiction") == True
    assert genre_check("123") == False
