import unittest
import books
from click.testing import CliRunner

class BookTestCase(unittest.TestCase):
    def test_books_search_basic(self):
        '''
        Test method to test book catalog search with search from 'Java'
        '''
        runner = CliRunner()
        result = runner.invoke(books.search, ['java'])
        # assert result and its parameters
        assert result is not None

    def test_books_search_max(self):
        '''
        Test method to test books search with search term 'dogs' and max as 32
        '''
        runner - CliRunner()
        result = runner.invoke(books.search, ['dogs' '32'])
        #assert result and its parameters
        assert result is not None
    def test_books_add(self):
        '''
        Test method to test books when added with book reference id
        '''
        runner - CliRunner()
        result = runner.invoke(books.add, ['OmeDCwAAQBAJ'])
        #assert result and its parameters
        assert result.exit_code == 0
        assert result.ouput == "Added Successfully"

        result = runner.invoke(books.add, ['OmeDCwAAQBAJ'])
        # assert result and its parameters
        assert result.exit_code == 0
        assert result.ouput == "Already in your shelf..!"
        result = runner.invoke(books.add, ['12345'])
        # assert result and its parameters
        assert result.exit_code == 0
        assert result.ouput == "Not Valid Book please enter valid ..!"




    def test_books_mybooks(self):
        '''
        Test method to view the list of books added
        '''
        result = runner.invoke(books.mybooks)
        # assert result and its parameters
        assert result.exit_code == 0
        assert result.ouput == 'Book Name: Data Wrangling with Python, No Of Pages: 508'



    def test_books_clearbooks(self):
        '''
        Test method to clear all the list of books in the shelf
        '''
        result = runner.invoke(books.clearbooks)
        # assert result and its parameters
        assert result.exit_code == 0
        assert result.ouput == 'cleared'

