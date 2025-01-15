class Inventory:
    def __init__(self):
        self.items = []
        self.coins = 10  #the player starts with 10 coins by default

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return f"{item} has been added to your inventory."
        return f"{item} is already in your inventory."

    def view_inventory(self):
        if not self.items:
            return f"Your inventory is empty. You have {self.coins} coins."
        return f"Your inventory contains:\n" + "\n".join(self.items) + f"\n\nYou have {self.coins} coins."

    def earn_coins(self, amount):
        self.coins += amount
        return f"You earned {amount} coins! You now have {self.coins} coins."

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        return False

    def buy_clue(self, clue, cost):
        if self.spend_coins(cost):
            self.add_item(clue)
            return f"You purchased the clue: {clue} for {cost} coins."
        return f"You don’t have enough coins to buy this clue. It costs {cost} coins."

