class CoffeeMaker:
  """Models the machine that makes the coffee."""
  def __init__(self):
    self.ressources = {
      "water": 300,
      "milk": 200,
      "coffee": 100
    }

  def report(self):
    """Prints a report of all ressources."""
    print(f"Water: {self.ressources['water']}ml")
    print(f"Milk: {self.ressources['milk']}ml")
    print(f"Coffee: {self.ressources['coffee']}g")


  def is_ressource_sufficient(self, drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    can_make = True
    for item in drink.ingredients:
      if drink.ingredients[item] > self.ressources[item]:
        print(f"Sorry there is not enough {item}.")
        can_make = False
    return can_make

  def make_coffee(self, order):
    """Deducts the required ingredients from the ressources."""
    for item in order.ingredients:
      self.ressources[item] -= order.ingredients[item]
    print(f"Here is your {order.name}☕️. Enjoy!")
