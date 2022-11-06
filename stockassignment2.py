import random
from math import *


print("####  Welcome to Programming Prinicples Sample Product Inventory# ####")


### in this class we will take inputs from user aboutthe product details
### during this process there might be some exception where the user may enter a wrong type of data which might cause an error in code and our code may not be able to run.
## to overcome this error we use try and axcept method

class allinputs:

    

    def inputting():
### taking inputs and using try except method
        try:

            

            productcode=int(input("Enter product code:"))
        except:
            print("Type error please enter correct data")
            productcode=int(input("Enter product code:")) 

        try:  
            name=input("Enter product name:")

        except:
            print("type error please enter correct data")
            name=input("Enter product name:")


        try:
            stocks=input("please enter current stock:")
        except:
            print("type error please enter correct data")
            stocks=input("please enter current stock:")

        try:
            pricing=float(input("please enter sale price:"))
        except:
            print("type error please enter correct data")
            pricing=float(input("please enter sale price:"))

        try:

            manufacturingcost=float(input("enter manufacture cost of the product:"))
        except:
            print("type error please enter correct data")
            manufacturingcost=float(input("enter manufacture cost of the product:"))

        try:
            montthproduction=int(input("please enter monthly production:"))
        except:
            print("type error please enter correct type of data")
            montthproduction=int(input("please enter monthly production:"))

            ## we use try except method to overcome if any error shows up in this program

        
c= allinputs()
allinputs.inputting()
print()
print()
print()
print()
print()
print("for confirmation of product please re --enter exact same details  ")
class inputs_statement():
    
    def confirmation():
    
        codename=int(input("enter the product code:"))
        print()
        name=input("enter the product name:")
        print()
        global sellingprice
        global manufacturingcost
        sellingprice=float(input("please enter Sale Price:"))
        print()
        manufacturingcost=float(input("please enter Manufacturing cost:"))
        print()
        print()
        print("monthly production should be more than 10")
        monthlyproduction=int(input("please enter Monthly Production:"))
        print()



    def products_manufactured_stocks():
        global manufacturedp
        global soldp
        global stockp
        manufacturedp = 0
        soldp = 0
        stockp = 0
        for i in range(1,13):
            print("Month:",i)

            manufacturedp=random.randint(1,101)
            print("         Manufactured:", manufacturedp , "units")
            soldp=random.randint(manufacturedp-10,manufacturedp+10)
            print("         Sold:", abs(soldp) , "units")
            stockp=random.randint(90,101)
            print("         Stock:", stockp ,  "units")

v=inputs_statement()
inputs_statement.confirmation()
inputs_statement.products_manufactured_stocks()
   


print("Net profit is---")


##print(((soldp * sellingprice)) - (manufacturedp * sellingprice))

sp =  soldp * sellingprice
mp = manufacturedp * sellingprice

print(sp-mp)

print()

print("THANKS FOR USING THE PROGRAM")



















             



        