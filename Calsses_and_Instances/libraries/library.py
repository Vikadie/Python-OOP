class Library:
    user_records = []
    books_available = {}  # { authors: list(books) }
    rented_books = {}  # {usernames: {book names: days left}}

    def add_user(self, user):
        if user in Library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        Library.user_records.append(user)

    def remove_user(self, user):
        if user not in Library.user_records:
            return "We could not find such user to remove!"
        Library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        user_ids = [user.user_id for user in Library.user_records]
        if user_id not in user_ids:
            return f"There is no user with id = {user_id}!"
        idx = user_ids.index(user_id)
        if Library.user_records[idx].username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        Library.user_records[idx].username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
