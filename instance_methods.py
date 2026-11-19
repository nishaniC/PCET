class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.current_page = 1

    def read_page(self):
        print(f"Reading page {self.current_page} of '{self.title}'...")
        self.current_page += 1

# Create a Book object
my_book = Book("Pride and Prejudice", "Jane Austen")

# Call the instance method
my_book.read_page()  # "Reading page 1 of 'Pride and Prejudice'..."
my_book.read_page()  # "Reading page 2 of 'Pride and Prejudice'..."
