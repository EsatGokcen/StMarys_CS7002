
class LibraryCatalogue():

    library_name = "Esat's Library"
    next_book_id = 2000

    def __init__(self,title,author,genre):
        self.__id = LibraryCatalogue.next_book_id
        LibraryCatalogue.next_book_id += 1
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = True 

    @classmethod
    def set_library_name(self, new_library_name):
        LibraryCatalogue.library_name = new_library_name
        print(f"Default library name set to: {LibraryCatalogue.library_name}")

    def checkout(self):
        self.availability = False
        print(f"Book {self.title} checked out successfully!")

    def return_book(self):
        self.availability = True
        print(f"Book {self.title} returned successfully!")

    def display_info(self):
        print(f"\n\nBook ID: {self.__id}\nBook Title: {self.title}")
        print(f"Book Author: {self.author}\nBook Genre: {self.genre}")
        if self.availability == True:
            ava = "Available"
        else:
            ava = "Not available"
        print(f"Book Availability: {ava}\n\n")

if __name__ == "__main__":
    book1 = LibraryCatalogue("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    book2 = LibraryCatalogue("To Kill a Mockingbird", "Harper Lee", "Classics")

    LibraryCatalogue.set_library_name("My Personal Library")

    book1.checkout()

    book1.display_info()
    book2.display_info()

