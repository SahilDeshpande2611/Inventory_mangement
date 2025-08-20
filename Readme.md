# 🛒 Inventory Management System (OOP with Inheritance)

This is a simple Inventory Management project built using Python and Object-Oriented Programming (OOP) concepts.
The system allows users to shop for different product categories such as Shoes, Bags, and Accessories, view available discounts, and calculate the total purchase amount.

## 🚀 Features

- **Store Base Class**
  - Displays product categories.
  - Shows general discounts on products.

- **Shoes Class (`shoes`, child of `store`)**
  - Displays available shoe brands.
  - Provides brand-specific discounts.
  - Allows setting price based on user’s selected shoe brand.

- **Bag Class (`bag`, child of `store`)**
  - Displays available bag brands.
  - Provides brand-specific discounts.
  - Allows setting price based on user’s selected bag brand.

- **Accessories Class (`accessiors`, child of `store`)**
  - Displays accessory categories.
  - Provides category-specific discounts.
  - Allows setting price based on user’s selected accessory.

- **TotalAmount Class (`Totalamount`, multiple inheritance)**
  - Takes selected products and calculates the total purchase amount.

## 📚 Inheritance Concepts Used

- **Single Inheritance**
  - Example: `shoes(store)` → `shoes` inherits from `store`.
  - The `super()` keyword is used to call the parent (`store`) constructor.

- **Method Overriding (Polymorphism)**
  - The `discount_products()` method is overridden in each subclass (`shoes`, `bag`, `accessiors`).
  - Parent class defines general discounts, child classes redefine them with specific brand/category discounts.

- **Multiple Inheritance**
  - Example: `class Totalamount(shoes, bag, accessiors)`
  - This class inherits from all three product categories, letting it access their methods.

- **Method Resolution Order (MRO)**
  - The program prints `Totalamount.__mro__` to show the order in which Python resolves methods in multiple inheritance.

## 📝 How It Works

1. User enters products to shop (e.g., shoes, bag, accessiors).
2. The program creates objects for selected categories.
3. For each product, the user chooses a brand/category → price is assigned.
4. The `Totalamount` class sums up all selected items and prints the final bill.
5. Finally, the MRO is displayed.

## ▶️ Example Run

```
Enter the products to shop for (comma separated: shoes, bag, accessiors): shoes, bag

Total brands in inventory for shoes are 9
You are currently shopping for shoes 
The heavly discounted products are :
shoes 50%
accessiors 20%
bag 10%
The heavy discounted brands for shoes  includes : ['Nike', 'Puma', 'Adidas']

Total brands for bag  in inventory are 5
The heavy discounted  brands for bags includes : ['Wildraft', 'Safari']

Enter the shoe brand from -- > [nike,puma,adidas] : nike
Enter the bag brand form  -- > [ wildcraft , skybags , safari , american Tourister, wrogn ] : safari

Your total amount is 0 ! 
Total amount is 3800

(<class '__main__.Totalamount'>, <class '__main__.shoes'>, <class '__main__.bag'>, <class '__main__.accessiors'>, <class '__main__.store'>, <class 'object'>)
```

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts Used:** OOP (Classes, Inheritance, Polymorphism, Method Overriding, Multiple Inheritance, MRO)