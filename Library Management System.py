# Create a library class
# Display book
# lend book - who owns the book if not present in library
# Add book
# Return book


class Library:
    def __init__(self,list, name):
        self.booklist =list
        self.name = name
        self.lenddict = {}

    def Display_book(self):
        print(f"We have following books available in1 {self.name} Library")
        for book in self.booklist:
            print(book)

    def Lend_book(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("lendict database has been updated you can take the book now")
        else:
            print(f"The book is already being used by{self.lenddict[book]}")

    def Addbook(self,book):
        self.booklist.append(book)
        print("Your book has been added in the Library ")

    def Return_book(self,book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    Pranay = Library(["Wings of fire","21 lesson for 21st century","The brief history of humankind","The unspoken name"],"Pranay's")
    while True:
        print(f"Welcome to {Pranay.name} library. Enter your choice to continue ")
        print("1.Display_book")
        print("2.Lend_book")
        print("3.Addbook")
        print("4.Return_book")

        user_choice = input()
        if user_choice not in ["1","2","3","4"]:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Pranay.Display_book()

        elif user_choice == 2:
            user = input("Enter your name")
            book  = input("Enter the name of the book you want to lend")
            Pranay.Lend_book(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            Pranay.Addbook(book)
        elif user_choice == 4:
            book = input("Enter the name of book you want to return")
            Pranay.Return_book(book)
        else:
            print("Invalid Option")

        print("Enter q to quit and c to continue")
        user_choice2 =""
        while (user_choice2!="q" and user_choice2!="c"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue







