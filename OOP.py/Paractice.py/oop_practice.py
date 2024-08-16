class Library:
    no_of_books : int =0
    Books : list =[]
    def menu(self):
        option=0
        while option !=4:
            option=int(input('Enter 1 : Show all Books \nEnter 2 : Add a Book \nEnter 3 : Show number of books '))
            match option:
                case 1 :
                    self.show_all_books()
                case 2 :
                    self.Add_Book()
                case 3 :
                    self.show_book()
                case _:
                    print('Invalid input : ')


    def show_all_books(self):
        for no , book in enumerate(Library.Books):  # name of class with variable 
            print(f'Book no {no+1} is {book}')

    def Add_Book(self):
        book=input('Enter a Book :')
        Library.Books.append(book)
        with open('Library.txt','a') as f :
            f.write(book+'\n')
        Library.no_of_books+=1
        
    def show_book(self):
        print('Number of books : ',Library.no_of_books)


Library1=Library()
Library1.menu()