class User:
    user_id: int
    username: str

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []  # user rented books

    def get_book(self,author: str, book_name: str, days_to_return: int, library):
        if (author in library.books_available.keys()) and (book_name in library.books_available[author]):
            self.books.append(book_name)
            if self.username in library.rented_books.keys():
                library.rented_books[self.username][book_name] = days_to_return
            else:
                library.rented_books[self.username] = dict({book_name: days_to_return})
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        book_available_in_ = None
        for username in library.rented_books.keys():
            if book_name in library.rented_books[username]:
                book_available_in_ = library.rented_books[username][book_name]
                break
        return f'The book "{book_name}" is already rented and will be available in {book_available_in_} days!'

    def return_book(self, author:str, book_name:str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)  # remove it from the user's rented books
        # remove it from the library.rented_books
        del library.rented_books[self.username][book_name]
        # get it back to library.books_available
        library.books_available[author].append(book_name)

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"