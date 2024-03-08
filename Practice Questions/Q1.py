#Q1. Write a PYTHON program for calculating the price of a product after adding the sales tax to its original price. Where rate of tax and price is inputted by user.

price,salestax = map(int,input("Enter price and the sales taxt to be added: ").split())
print("price after adding sales tax: ",price + price/100*salestax)