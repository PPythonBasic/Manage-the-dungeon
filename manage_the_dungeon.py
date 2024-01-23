import random

class Dungeon:
    def __init__(self) -> None:
        self.list_items = []

    def add_item_to_dungeon(self):
        name_item = input("Enter Item name : ")
        price = int(input("Enter Price : "))
        amount = int(input("Enter Amount : "))
        item_dict = {'Item_name': name_item,'Price':price,'Amount': amount}
        self.list_items.append(item_dict)
        print("-------")
        print(f"Added {name_item} {price} {amount}x")
    
    def view_item_in_dungeon(self):
        print("---- Show All Items in the Dungeon -----")
        for i in self.list_items:
            print(f"- {i["Item_name"]} {i["Price"]}G {i["Amount"]}x")
    
    def let_the_hero_enter_the_dungeon(self):
        random_index = random.randint(0,len(self.list_items)) - 1
        item = self.list_items.pop(random_index)
        print(f"Hero receives 1x {item["Item_name"]} item.")

    def match_funct(self):
        match int(self.choice):
            case 1:
                self.add_item_to_dungeon()
            case 2:
                self.view_item_in_dungeon()
            case 3:
                self.let_the_hero_enter_the_dungeon()

    def run_dungeon(self):
        while True:
            print('<|Manage The Dungeon|>'.center(40," "))
            print('[1] Add items to the dungeon')
            print('[2] View items in the dungeon')
            print('[3] Let the hero enter the dungeon.')
            print('[0] Close the dungeon.')
            self.choice = input('Choice : ')
            if self.choice == "0":
                break
            self.match_funct()
