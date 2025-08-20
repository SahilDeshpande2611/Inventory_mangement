class store:
  def __init__(self,product):
    print(F"You are currently shopping for {product} ")

 
  @staticmethod
  def discount_products():
    discount = {"shoes" : "50%" ,"accessiors" : "20%" , "bag" : "10%"}
    print("The heavly discounted products are :")


    for key,value in discount.items():
        print(f"{key} {value}")

    
  
class shoes(store):
    def __init__(self, product, total_brands=9):
        print(f"Total brands in inventory for shoes are {total_brands}")
        super().__init__(product)
        store.discount_products()
        

    def discount_products(self):
        brands = ["Nike", "Puma", "Adidas"]
        print(f"The heavy discounted brands for shoes  includes : {brands}")

    def set_price(self):
        product_category = input("Enter the shoe brand from -- > [nike,puma,adidas] :")
        if product_category.lower() == "nike":
            self.amount = 3000
        elif product_category.lower() == "puma":
            self.amount = 5000
        elif product_category.lower() == "adidas":
            self.amount = 2000
        else:
            self.amount = 700
        return self.amount

  
class bag(store):
    def __init__(self, product, total_brands=5):
        print(f"Total brands for bag  in inventory are {total_brands}")
        
        

    def discount_products(self):
        brands = ["Wildraft", "Safari"]
        print(f"The heavy discounted  brands for bags includes : {brands}")

    def set_price(self):
        product_category = input("Enter the bag brand form  -- > [ wildcraft , skybags , safari , american Tourister, wrogn ] :")
        if product_category.lower() == "wildcraft":
            self.amount =  1200
        elif product_category.lower() == "skybags":
            self.amount =  1000
        elif product_category.lower() == "safari":
            self.amount =  800
        elif product_category.lower() == "american Tourister":
            self.amount = 2000
        elif product_category.lower() == "wrogn":
            self.amount = 900
        else :
            self.amount=0
        return self.amount
   
     
class accessiors(store):
    def __init__(self, product, total_category=3):
        print(f"Total categories of accessiors in inventory are {total_category}")
        super().__init__(product)
        store.discount_products()
        

    def discount_products(self):
        brands = ["Sunglasses", "Bracelets", "Watches"]
        print(f"The 20% discounted accessiors are : {brands}")

    def set_price(self):
        product_category = input("Enter the accessiors from -- > to shop for  [Sunglasses,Bracelets,Watches] :")
        if product_category.lower() == "sunglasses":
            self.amount = 2000
        elif product_category.lower() == "bracelets":
            self.amount = 1500
        elif product_category.lower() == "watches":
            self.amount = 10000
        else:
            self.amount = 0
        return self.amount


class Totalamount(shoes,bag,accessiors):
    def __init__(self, products):
        print("Your total amount is 0 ! ")
        
        self.amounts=[]


        for p in products:
            price=p.set_price()
            self.amounts.append(price)

    def totalamount(self):
        finalamount = sum(self.amounts)
        print(f"Total amount is {finalamount}")


    
  

# Ask user for product
user_products = input("Enter the products to shop for (comma separated: shoes, bag, accessiors): ").lower().split(",")


selected_objects=[]

for prod in user_products:
    prod=prod.strip()
    if prod == "shoes":
        s = shoes("shoes")
        s.discount_products()
        selected_objects.append(s)

    elif prod == "bag":
        b = bag("bag")
        b.discount_products()
        selected_objects.append(b)

    elif prod == "accessiors":
        a = accessiors("accessiors")
        a.discount_products()
        selected_objects.append(a)
    else:
        print("Invalid product choice!")

if selected_objects:
    t=Totalamount(selected_objects)
    t.totalamount()

print(Totalamount.__mro__)


    


