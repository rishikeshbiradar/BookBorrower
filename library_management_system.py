class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displayavailablebooks(self):
        print("The books present in this library are:")
        for book in self.books:
            print("\t", book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f'''you have been issued {bookname} book,keep it safe and return within 30 daysThank you''')
            self.books.remove(bookname)
        else:
            print('''Sorry this book is not available,just wait for some days,as soon as someone return it,you will get it.Thank you''')
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book")
    
class student:
    # def __init__(self):
    def requestbook(self):
        reqbook=input("Enter the name of the book you want to borrow:")
        self.book=reqbook
        return self.book
    def returnbook(self):
        retbook=input("Enter the name of the book you want to return:")
        self.book=retbook
        return self.book
    

if __name__=="__main__":
    centrallibrary=library(["C Language-Balaguruswamy","C++ Language-Balaguruswamy" "Data Science","Data Structures And Algorithm","Python"])
    student=student()
    while(True):
        
        Welcomemsg='''=======  Welcome to Central Library  =======

        Please choose an option
        1. list all the book
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print( Welcomemsg)
        a=int(input("Enter your choice:"))
        if a==1:
            centrallibrary.displayavailablebooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestbook())
        elif a==3:
            centrallibrary.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing Central library !")
            exit(0)
        else:
            print("Invalid Choice")
        


