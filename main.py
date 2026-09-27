import data
import sandwich_maker
import cashier

from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    ###  write the rest of the codes ###
    machine = SandwichMachine(resources)

    user_input = input("What size sandwich?")

    if user_input in recipes:
        sandwich = recipes[user_input]
        if machine.check_resources(sandwich["ingredients"]):
            coins = machine.process_coins()

            if machine.transaction_result(coins, sandwich["cost"]):
                machine.make_sandwich(user_input, sandwich["ingredients"])
                print("Enjoy!")
    else:
        print("Invalid input")


if __name__=="__main__":
    main()
