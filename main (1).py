drinkDetails = ""
drink = input(
    "What type of drink would you like to order?\nWater\nCoffee\nTea\nEnter your choice: "
)
drink = drink.title()
if drink == "Water":
  drinkDetails = drink
  temperature = input("Would you like your water hot or cold?: ")
  temperature = temperature.title()
  if temperature == "Hot":
    drinkDetails += ", " + temperature
  elif temperature == "Cold":
    drinkDetails += ", " + temperature
    ice = input("Would you like ice? \nYes\nNo\nEnter your choice: ")
    ice = ice.title()
    if ice == "Yes":
      drinkDetails += ", Ice"
    else:
      drinkDetails += ", No Ice"
  else:
    drinkDetails += ", unknown temperature entered."

elif drink == "Coffee":
  drinkDetails = drink
  decaf = input("Would you like decaf coffee? \nYes\nNo\nEnter your choice: ")
  decaf = decaf.title()
  if decaf == "Yes":
    drinkDetails += ", Decaf"
    milk_cream_black = input(
        "Would you like milk, cream, or black? \nMilk\nCream\nBlack\nEnter your choice: "
    )
    milk_cream_black = milk_cream_black.title()
    if milk_cream_black == "Milk":
      drinkDetails += ", Milk"
    elif milk_cream_black == "Cream":
      drinkDetails += ", Cream"
    elif milk_cream_black == "Black":
      drinkDetails += ", Black"
    else:
      drinkDetails += ", unknown customization entered."
  elif decaf == "No":
    drinkDetails += ", Regular"
    milk_cream_black = input(
        "Would you like milk, cream, or black? \nMilk\nCream\nBlack\nEnter your choice: "
    )
    milk_cream_black = milk_cream_black.title()
    if milk_cream_black == "Milk":
      drinkDetails += ", Milk"
    elif milk_cream_black == "Cream":
      drinkDetails += ", Cream"
    elif milk_cream_black == "Black":
      drinkDetails += ", Black"
    else:
      drinkDetails += ", unknown customization entered."
  else:
    drinkDetails += ", unknown drink entered."

elif drink == "Tea":
  drinkDetails = drink
  teaType = input(
      "What type of tea would you like? \nBlack\nGreen\nEnter your choice: ")
  teaType = teaType.title()
  if teaType == "Black":
    drinkDetails += ", Black"
  elif teaType == "Green":
    drinkDetails += ", Green"
  else:
    drinkDetails += ", unknown tea entered."
else:
  print("Sorry, we did not have that drink available for you.")
print("Your drink selection:", drinkDetails)
