#this is simple project for online store
class category():
    Shopping_cart=[]
   
    def category_info(slef):
        category_id=1
        
        
    Electronics = {
            "-1- Smartphones =" : 5000,
            "-2- Laptops ="     : 20000,
            "-3- Cameras ="     : 3000,
            "-4- Headphones ="  : 500,
            "-5- Smartwatches =": 900
         }
       
    
    Fashion = {
            "-1- dresses =" :1000,
            "-2- shirts ="     :200,
            "-3- jeans ="     :300,
            "-4- Shoes ="  :400,
            "-5- bags =" :100
        }
    
    Toys_and_Games = {
            "-1- Board games =" : 500,
            "-2- Toys for children ="   : 2000,
            "-3- Video games ="     : 6000,
            
        }
    
    Books_and_Stationery = {
            "-1- Novels ="        : 200,
            "-2- Notebooks ="     : 100,
            "-3- Pens ="          : 50,
           
        }
    def total_p(self):
        
        total_price = 0
        for cat in category().Shopping_cart:
            total_price += cat
        return total_price
class order (category):
    
    def order_info(self):
        order_id=1
       
        
    def choose_category(self):
        choose = input("choose category \n1-Electronics   2-Fashion   3-Toys_and_Games   4-Books_and_Stationery\n")            
        if choose == "1":
            print("\n\n","choose product from electronics :\n",category().Electronics,"\n\n")
            choose_elc = input( )
            match choose_elc:
                case "1":
                    confirm_choice= input("you want buy smartphone and its price =5000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Electronics['-1- Smartphones ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            
                            return self.choose_category()
                        elif new_buy=="n":
                            return self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())                          
                case "2":
                    confirm_choice= input("you want buy laptopo and its price =20000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Electronics['-2- Laptops ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "3":
                    confirm_choice= input("you want buy camera and its price =3000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Electronics['-3- Cameras ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())                        
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())  
                case "4":
                    confirm_choice= input("you want buy headphone and its price =500 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Electronics['-4- Headphones ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                          return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())            
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())
                case "5":
                    confirm_choice= input("you want buy smartwatche and its price =900 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Electronics['-5- Smartwatches ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                          return   self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
        elif choose =="2":
            print("\n\n","choose product from Fashion :\n",category().Fashion,"\n\n")
            choose_f = input( )
            match choose_f:
                case "1":
                    confirm_choice= input("you want buy dresses and its price =1000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Fashion['-1- dresses ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "2":
                    confirm_choice= input("you want buy shirts and its price =200 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Fashion['-2- shirts ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                            return self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "3":
                    confirm_choice= input("you want buy jeans and its price =300 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Fashion['-3- jeans ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category()) 
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())                                                    
                case "4":
                    confirm_choice= input("you want buy Shoes and its price =400 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Fashion['-4- Shoes ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                            return self.customer_info()
                        else :
                            print("invalid input",self.choose_category()) 
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())                   
                case "5":
                    confirm_choice= input("you want buy bags and its price =100 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Fashion['-5- bags ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                          return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
        elif choose=="3":
            print("\n\n","choose product from Toys_and_Games :\n",category().Toys_and_Games,"\n\n")
            choose_t = input( )
            match choose_t:
                case "1":
                    confirm_choice= input("you want buy Board games and its price =500 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Toys_and_Games['-1- Board games ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            
                            return self.choose_category()
                        elif new_buy=="n":
                           return self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "2":
                    confirm_choice= input("you want buy Toys for children and its price =2000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Toys_and_Games['-2- Toys for children ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                            return self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "3":
                    confirm_choice= input("you want buy Video games and its price =6000 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Toys_and_Games['-3- Video games ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                          return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())          
        elif choose =="4":
            print("\n\n","choose product from Books_and_Stationery :\n",category().Books_and_Stationery,"\n\n")
            choose_t = input( )
            match choose_t:
                case "1":
                    confirm_choice= input("you want buy Novels and its price =200 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Books_and_Stationery['-1- Novels ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            
                            return self.choose_category()
                        elif new_buy=="n":
                            return self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "2":
                    confirm_choice= input("you want buy Notebooks and its price =100 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Books_and_Stationery['-2- Notebooks ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category())
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
                case "3":
                    confirm_choice= input("you want buy Pens and its price =50 to confirm enter \"y\" to cancel enter \"n\"")
                    if confirm_choice =="y":
                        category().Shopping_cart.append( category().Books_and_Stationery['-3- Pens ='])
                        print(self.total_p())
                        new_buy = input("success!!  do you want to buy another thing \'y\' or \'n\'")
                        if new_buy =="y":
                            return self.choose_category()
                        elif new_buy=="n":
                           return  self.customer_info()
                        else :
                            print("invalid input",self.choose_category()) 
                    elif confirm_choice=="n":
                        cancel_order = input("did you want to cancel order : \"y\"\"n\"")
                        if cancel_order=="y":
                            print("thank you") 
                        elif cancel_order=="n":
                            return self.choose_category()
                        else:
                          print("invalid input",self.choose_category())    
                    else:
                          print("invalid input",self.choose_category())        
        else :return print("invalid choice Try again\n",self.choose_category())           
    def display(self):
        while True:
            self.fname = input("To make order enter this imformation\nfirst name :")   
            self.lname = input("last name :")
            self.c_address = input("address :")
            self.phone = input("phone :")
            self.c_email = input("email :")

    
            if self.fname!= "" and self.lname!= "" and self.c_address!= "" and self.phone != "" and self.c_email != "":
                self.choose_category()
                break
            else:
                self.display() 




class Online_Store(order):
    def default_info_store(self):
        s_name = "elgarhy store"
        s_address ="egypt"
        s_email="elgarhyStore@gmail.com"
        print(f"\n{s_name}\n{s_address}\n{s_email}")
    def customer_info(self):
         
        print(f"{self.default_info_store()}\nyour information is \nname: {self.fname} {self.lname}\nadress: {self.c_address}\nphone: {self.phone}\nemail:{self.c_email}\norder total price = {self.total_p()}")
        
            
    
 
    







os = Online_Store()
os.display()
