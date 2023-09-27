list_items = []

def add_items():
    global list_items
    while True:
        item = input('Enter Item name : ').upper()
        if item != '':
            break
    while True:
        price = input('Enter Price : ').upper()
        if price != '':
            price = int(price)
            break
    while True:
        amount = input('Enter Amount : ').upper()
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
