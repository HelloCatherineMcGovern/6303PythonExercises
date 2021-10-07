# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

# Catherine McGovern

# Program requests input
month = ""
# Begin while loop
while month != "quit":
    input_month = input("Learn your birthstone! \n Enter any month or 'quit'")
    month = input_month.lower()
    # Program checks to see if there is a match with input and a month
    if month == "january":
        birthstone = "garnet"
    elif month == "february":
        birthstone = "Amethyst"
    elif month == "march":
        birthstone = "Aquamarine"
    elif month == "april":
        birthstone = "Diamond"
    elif month == "may":
        birthstone = "Emerald"
    elif month == "june":
        birthstone = "Pearl or Alexandrite"
    elif month == "july":
        birthstone = "Ruby"
    elif month == "august":
        birthstone = " Peridot"
    elif month == "september":
        birthstone = " Sapphire"
    elif month == "october":
        birthstone = "Tourmaline or Opal"
    elif month == "november":
        birthstone = "Topaz or Citrine"
    elif month == "december":
        birthstone = "Tanzanite, Zircon or Turquoise"
    elif month == "quit":
        break
    else:  # The user enters invalid information
        print("Invalid input")
        input_month = input(
            "Learn your birthstone! \n Enter any month or 'quit'")
    print(f"Thanks for playing, your birthstone is {birthstone} ")
    print("*" * 30)


# Exit while loop and exite program.
print(f"Thanks for playing! Good-bye! ")
