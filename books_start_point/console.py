import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()


author1 = Author("J.K", "Rowling")
author_repository.save(author1)
author2 = Author("J.R.R", "Tolkien")
author_repository.save(author2)
author3 = Author("Enid", "Blyton")
author_repository.save(author3)

author_repository.select_all()

book1 = Book("Harry Potter and the Philosphers Stone", "Fiction", "Bloomsbury", author1, %s)
book_repository.save(book1)

book2 = Book("The Fellowship of the Ring", "Fiction", "Allen & Unwin", author2, %s)
book_repository.save(book2)

book3 = Book("Five on a Treasure Island", "Fiction", "Hodder & Stoughton", author3, %s)
book_repository.save(book3)

pdb.set_trace()
