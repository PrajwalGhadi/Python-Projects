#Mini Project on Library Management

class Library:
    def __init__(self, *name, **book_name):
        self.a = {"Python", "Core Java", "Advance Java", "C++"}
        self.b = {}
        self.name = name
        self.book_name = book_name

    def Display_Book(self):

        print(self.a)


    def Add_Book(self):

        self.b[name] = book_name
        print(f"\nYour book is Successfully Added to Library...\n")

        self.a.add(book_name)
        print(f"Now the list of books in library are : \n {self.a}\n")


        print(f"Your name and book is : {self.b}")


    def Return_Book(self):
        print("Thanks for Returning Book ...\n")

        self.a.add(book_name)
        print("Your book is Added to library successfully ...\n")



print("***** Library Management *****")

numb = input("To Add book (a), To Display Book (d), To Return Book (r) :")

if __name__ == '__main__':

    while True:

        if numb == "d":

            display = Library()
            Library.Display_Book(display)

        elif numb == "a":

            name = input("Enter the your name : ")
            book_name = input("Enter the Book name : ")

            add_book = Library(name, book_name)
            Library.Add_Book(add_book)

        elif numb == "r":

            book_name = input("Name of book you want to return : ")

            return_book = Library(book_name)
            Library.Return_Book(return_book)

        else:
            print("Please try again with given values to Add, Display and Return : ")


        exit()