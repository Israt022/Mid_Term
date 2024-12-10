class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
   
    def get_book_id(self):
        return self.__book_id
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You Have Successfully Borrowed '{self.__title}'")
        else:
            print(f"Sorry '{self.__title}' is Not Available")
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You Have Successfully return '{self.__title}' this Book")
        else:
            print(f"'{self.__title}' This Book not Borrowed so no need to return")
    
    def View_All_Books(self,book_list):
        print("*****Library Menu*****")
        
        for i in book_list:
            print(f"{i.__title}\t{i.__author}\t")
            if i.__availability:
                print("available")
            else:
                print("Not Available")
    @staticmethod
    def exit():
        print("Thanks you for Visiting our Library")
    book_list = []
    
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)
        print(f"Book Name : '{book.Bookname}' and Tital :  {book.tital}")

class Library:
    book_list = []
    
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)
        print(f"Book Name : '{book.Bookname}' and Tital :  {book.tital}")
        
        
def main():
    Book1 = Book(1,'Design Patterns: Elements of Reusable Object Oriented Software','Erich Gamma et al',True)
    Book2 = Book(2,'Head First Programming','Paul Barry and David Griffiths',True)
    
    book_list = [Book1,Book2]
    
    while(True):
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit.")
        
        choice = int(input("Please Enter Your Choice : "))
        if choice not in [1,2,3,4]:
            print("Invalid Input")
            continue
        
        if choice == 1:
            Book1.View_All_Books(book_list)
            
        elif choice == 2:
            Book_Title = input("Enter the title of Your Book Name : ")
            found = False
            for i in book_list:
                if i._Book__title.lower() == Book_Title.lower():
                    i.borrow_book()
                    found = True
                    break
            if not found:
                print(f"{Book_Title} Not Found ")
            
        elif choice == 3:
            Book_Title = input("Enter the title of Your Book Name : ")
            found = False
            for i in book_list:
                if i._Book__title.lower() == Book_Title.lower():
                    i.return_book()
                    found = True
                    break
            if not found:
                print(f"{Book_Title} Not Found ")
        elif choice == 4:
            Book.exit()
            break
        


main()