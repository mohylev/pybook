import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedźmin", "Sapkowski", 2000)
    def test_get_info(self):
        text_correct = "Książka: Wiedźmin Autor: Sapkowski Rok: 2000"
        text_result = self.book.get_info()
        self.assertEqual(text_result, text_correct)
    def test_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        self.assertEqual("Miecz przeznaczenia", self.book.title)
    def test_change_author(self):
        self.book.change_author("Dick")
        self.assertEqual("Dick", self.book.author)
    def test_change_year(self):
        self.book.change_year(3000)
        self.assertEqual(3000, self.book.year)

if __name__ == 'main':
    unittest.main()
