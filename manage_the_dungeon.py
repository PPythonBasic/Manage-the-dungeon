import random
list_items = []

def add_items():
    global list_items
    while True:
        item = input('Enter Item name : ')
        if item != '':
            if len(item) <= 2:
                item = item.upper()
            else:
                item = item.capitalize()
            break
    while True:
        price = input('Enter Price : ')
        if price != '':
            price = int(price)
            break
    while True:
        amount = input('Enter Amount : ')
        if amount != '':
            amount = int(amount)
            break

    dict_item = {
        'Item_name': item, 
        'Price': price, 
        'Amount': amount
    }
    list_items.append(dict_item)
    print('-------')
    print(f'{item} {price}G {amount}x')


def view_item():
    print(' Show All Items in the Dungeon '.center(40,"-"))
    for i in list_items:
        print(f"- {i['Item_name']} {i['Price']}G {i['Amount']}x")

def enter_dungeon():
    global list_items
    random_item = random.choice(list_items)
    key_man = list_items.index(random_item)
    lost_item = list_items.pop(key_man)
    print(f"Hero receives {lost_item['Amount']}x {lost_item['Item_name']} item.")




















def match_funct(choice:int):
    match choice:
        case 1:
            pass

def run_dungeon():

    while True:
        print('<|Manage The Dungeon|>'.center(40," "))
        print('[1] Add items to the dungeon')
        print('[2] View items in the dungeon')
        print('[3] Let the hero enter the dungeon.')
        print('[0] Close the dungeon.')
        choice = input('Choice : ')
        match_funct(choice)
