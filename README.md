
1) #Software Requirements:

Python3 Version 3.7, PIP, IDE: Pycharm 

setup.bat file contains the executable commands before executing the test.

$pip install requests
$pip install pyfiglet
$pip install click


2) # Functional Requirements:

 # 2.1) The app should prompt the user for a search string.

 from the class books.py 
 search(query,max) method allows to search any query (eg: 'Python') 
    along with the max value (default/minimum here I have given is 20)
 
 #Execution:
 
 To execute this
  In the terminal
 $python3 books.py search python
 
 #OUTPUT: List of books available for given Search: 20
  
 When max value is dynamically given as 40
 
 $python3 books.py search python 40
 
 #OUTPUT: List of books available for given Search: 40
 
 
 
#  (you may use popular search strings like 'dogs','cats','New York', ‘Java’... etc.)

 $python3 books.py search Java
 
 #OUTPUT: List of books available for given Search: Java
 

# 2.2) The app should allow a user to add specific books from the search results to a virtual bookshelf

from the class books.py

add(id): method allows to add the books to the virtual bookshelf with the book id

#Execution:

 $python3 books.py add
   
   Please enter a Book Id to add it in to your shelf: diqHjRjMhW0C
   
 #OUTPUT: Added Successfully
 
  $python3 books.py add
   
   Please enter a Book Id to add it in to your shelf: OmeDCwAAQBAJ
   
 #OUTPUT: Added Successfully
 


# 2.3) The app should also be able to persist bookshelf to disk

# 2.4) The app should be able to load virtual bookshelf from step #3

A json file bookshelf.json is added each time we add the book into the list. 
Please check the file bookshelf.json for the disk content.

File is saved in local once we initiate adding a book. 
Every time a book is added we update the list.



# 2.5) The user should be able to display the books in the virtual bookshelf

from books.py class

mybooks: method allows to display the list of books added to the virtual bookshelf

#Execution:

$ python3 books.py mybooks

#OUTPUT: 
Book Name: Data Wrangling with Python, No Of Pages: 508
Book Name: Wicked Cool Java, No Of Pages: 224



# 2.6) sorted by price, avg rating, rating count, published date, or page count

from the class books.py

mybooks(sortby): method allows to sort the list based on the given parameters

#Execution:

$python3 books.py mybooks pageCount

#OUTPUT:
Book Name: Wicked Cool Java, No Of Pages: 224
Book Name: Data Wrangling with Python, No Of Pages: 508

"List is sorted based on the pageCount" 


Test Code:

#Pytest:
test_books.py has been written to work on unit testing and partly functional test cases.


3) #Execution Help

## Google Bookshelf CLI using python
The Bookshelf collection allows you to view bookshelf metadata as well as to modify the contents of a bookshelf.

## Development dependecy
You should have python 3 and pip installed in the development machine
run `setup.bat` to install all the dependencies.

## Help for every command
`python books.py --help`

`python books.py search --help`

`python books.py read --help`

`python books.py add --help`

`python books.py mybooks --help`

`python books.py clearbooks --help`

## Search for Books
`python books.py search <name>`

 You can pass a optional parameter to this like max response this is defaulted to 20
    
`python books.py search <name> <max>`

## Read Books description'
`python books.py read <bookID>`

## Adding Books in to shelf
`python books.py add <bookID>`

## Adding Books in to shelf
`python books.py add <bookID>`
    
## Reading books from Shelf
`python books.py mybooks`
`python books.py mybooks title`
`python books.py mybooks pageCount`

## Clearing all books from Shelf
`python books.py clearbooks`