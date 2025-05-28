import os
import json

DATA_FILE = "library.json"

# Load existing books or create new list


def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save books to file


def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    save_books(books)
    print("✅ Book added successfully!")

# View all books


def view_books():
    if not books:
        print("No books found.")
        return
    print("\n📚 Your Library:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

# Search for a book


def search_books():
    query = input("Enter title or author to search: ").lower()
    found = [book for book in books if query in book['title'].lower()
             or query in book['author'].lower()]
    if found:
        print("\n🔍 Search Results:")
        for idx, book in enumerate(found, start=1):
            print(
                f"{idx}. {book['title']} by {book['author']} ({book['year']})")
    else:
        print("No matching books found.")

# Delete a book


def delete_book():
    view_books()
    try:
        choice = int(input("Enter the number of the book to delete: ")) - 1
        if 0 <= choice < len(books):
            removed = books.pop(choice)
            save_books(books)
            print(f"🗑️ Removed: {removed['title']} by {removed['author']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main menu loop


def main():
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye! 📘")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the app
books = load_books()
main()
