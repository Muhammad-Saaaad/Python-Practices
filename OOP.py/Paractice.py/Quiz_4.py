class Product:
    __category ='none'
    Storage=[]
    def __init__(self):
        self .pId=0
        self .pName = 'mo name'
        self . pPrice=0.0 
        self . pStatus='Sold' 

    def menu(self):
        options = 0 
        products=0
        while options!=8:

            options=float(input('''
        Press 1 to Add Product (Status of Each Product must be Available at Start)
        Press 2 to Show All Products
        Press 3 to Sell Product (This will change status of specific product which will be searched by pID from “Available” to “Sold”)
        Press 3.1 to Search Product by Name
        Press 4 to Show Sold Products
        Press 5 to Show Available Products (Also Show Count of Available Products)
        Press 6 to Show Total Price of All Products
        press 7 to exit : 
            '''))
            match options:
                case 1:
                    self.add_product()
                    products+=1
                case 2 :
                    self.show_all_products()
                case 3 :
                    self.sell_product()
                case 3.1:
                    self . Search_product()
                case 4 : 
                    self . sold_products()
                case 5 :
                    self . Avalible_Product()
                case 6 :
                    self . Show_total_price()
                case 7 :
                    print('Exit :' )
                case _:
                    print('Invalid input : ')

    
    def add_product(self):
        self.pId=int(input('Enter id of product : '))
        self.pName=input('Enter name of the product : ')
        self.pPrice=float(input('Enter price of product : '))
        self.pStatus='Avalible'
        Product.__category=input('Enter the category of the product : ')
        store = [self.pId, self.pName ,self.pPrice , self.pStatus , Product.__category ]
        Product.Storage.append(store)

    def show_all_products(self):
        for index , product in enumerate(Product.Storage):
            print(f'No . {index+1} {product}')

    def sell_product(self):
        get_id=int(input('Enter id of the product : '))
        for product in Product.Storage:
            if get_id == product[0]:
                print('Sold Sucessfully : ')
                product[-2]='sold'

    def Search_product(self):
        name=input('Enter the name of product : ')
        for product in Product.Storage:
            if product[1] == name :
                print(product)

    def sold_products(self):
        for product in Product.Storage:
            if product[-2] == 'sold':
                print(product)

    def Avalible_Product(self):
        counts=0
        for product in Product.Storage:
            if product[-2] == 'Avalible':
                print(product)
                counts+=1
        print(f'The total counts of Avalible products are : {counts}')

    def Show_total_price(self):
        total_price=0.0
        for product in Product.Storage:
            total_price=total_price+product[2]
        
        print('Total price of all the products are : ', total_price)

# Class ended 
obj=Product()
obj.menu()