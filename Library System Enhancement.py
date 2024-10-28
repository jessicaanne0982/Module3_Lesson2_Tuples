# Task 1
 
def add_books(library):
    while True:
        new_book = input("Enter the title of the book to be added: ")
        author = input("Enter the author: ")
        found = False
        for book in library:
            if book[0].lower() == new_book.lower():
                print("That book already exists and cannot be added again.")
                break
            elif not found:
                library.append((new_book, author))
                print(f"{new_book} by {author} has been added to the library.")
                found = True
                break
        
        continue_input = input("Would you like to add another book? (yes/no): ").lower()
        if continue_input != 'yes':
            break
 
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
 
add_books(library)
print(library)
