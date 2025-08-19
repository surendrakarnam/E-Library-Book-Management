class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None

class Library:
    def __init__(self):
        self.head = None
        self.undo_stack = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        new_book.next = self.head
        self.head = new_book
        print(f"✅ Added book: '{title}' by {author}")

    def borrow_book(self, title):
        prev = None
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.undo_stack.append(('borrow', current))
                print(f"📚 Borrowed: '{current.title}'")
                return
            prev = current
            current = current.next
        print("❌ Book not found.")

    def return_book(self, title, author):
        book = Book(title, author)
        book.next = self.head
        self.head = book
        self.undo_stack.append(('return', book))
        print(f"↩️ Returned: '{title}' by {author}")

    def undo_action(self):
        if not self.undo_stack:
            print("⚠️ No actions to undo.")
            return
        action, book = self.undo_stack.pop()
        if action == 'borrow':
            book.next = self.head
            self.head = book
            print(f"↩️ Undo borrow: '{book.title}' restored to inventory.")
        elif action == 'return':
            self.borrow_book(book.title)

    def search_book(self, keyword):
        current = self.head
        found = False
        print(f"
🔍 Search results for '{keyword}':")
        while current:
            if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                print(f"- '{current.title}' by {current.author}")
                found = True
            current = current.next
        if not found:
            print("No matching books found.")

    def display_inventory(self):
        print("\n📚 Library Inventory:")
        current = self.head
        if not current:
            print("No books available.")
            return
        while current:
            print(f"- '{current.title}' by {current.author}")
            current = current.next

# --- Demo ---
if __name__ == "__main__":
    lib = Library()

    # Add books
    lib.add_book("1984", "George Orwell")
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    lib.display_inventory()

    # Borrow and return
    lib.borrow_book("1984")
    lib.return_book("1984", "George Orwell")
    lib.undo_action()

    lib.search_book("Harper")
    lib.display_inventory()