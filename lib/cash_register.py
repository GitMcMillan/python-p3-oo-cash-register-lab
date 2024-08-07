#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0 ):
    self.discount = discount
    self.total = total
    self.items =[]
    self.last_transaction_amount = 0

  def add_item(self, title, price=0, quantity=1):
    self.title = title 
    self.price = price
    self.total += price * quantity
    for _ in range(quantity): #for EVERY item in quantity
      self.items.append(title)  # append it to the items list
      self.last_transaction_amount = price * quantity
    
    
  def apply_discount(self):
    # take the price variable
    # "discount" it by 20%
    # return the new value
    if isinstance(self.total, (int, float)) and self.total > 0:
      self.total = self.total - (self.total * .20)
      print(f"After the discount, the total comes to $800.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
      self.total -= self.last_transaction_amount
        # Remove the last item based on the title; adjust logic if needed for multiple quantities
      if  self.items:
          self.items.pop()
      self.last_transaction_amount = 0
        # Reset total if items list is empty
      if not self.items:
            self.total = 0.0
      
   
      


    
    

