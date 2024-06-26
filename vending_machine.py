

class VendingMachine:
    def __init__(self):
        self.drinks = {
            "Coke": 10,
            "Pepsi": 10,
            "Coffee": 5,
            "Tea": 5
        }
        self.notes = [200, 150, 100, 50, 20, 10, 5, 1]

    def buy_drink(self, drink_name: str, amount_inserted: int) -> str:
        if drink_name not in self.drinks:
            return f"Drink not available. The only option is {', '.join([d for d in self.drinks])}"

        else:
            drink_price = self.drinks[drink_name]

            if amount_inserted < drink_price:
                return f"Insufficient amount. Please insert at least RM{drink_price} to purchase {drink_name}."

            change = amount_inserted - drink_price
            change_notes = self.calculate_change(change)

            return f"Dispensing {drink_name} which cost RM{drink_price}. Your change is: RM{change_notes}"

    def calculate_change(self, change: int) -> list[int]:
        
        change_notes = []
        for note in self.notes:
            while change >= note:
                change -= note
                change_notes.append(note)
        return change_notes


vending_machine = VendingMachine()
# your_drink = str(input("\nWhat do you like to purchase: "))
# your_money = int(input("\nHow much money do you use to buy the drink: "))
print(vending_machine.buy_drink("Coffee", 3))