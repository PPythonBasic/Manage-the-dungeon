import inspect
import mock
import builtins
from manage_the_dungeon import add_items, view_item

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_add_item_sword_and_price_300_and_amount_1(capfd):
    with mock.patch.object(builtins, 'input', side_effect=['Sword', 300 , 1]):
        add_items()
        out, err = capfd.readouterr()
        if out == "-------\nSword 300G 1x\n":
            assert True
        else:
            print(bcolors.FAIL+"FAILED",end="")
            print("\n" + bcolors.FAIL)
            print(" The function must be like this ".center(40, "="),end="\n\n")
            print(f"""Enter Item name : Sword
Enter Price : 200
Enter Amount : 1
-------
Sword 200G 1x <-- \n""")
            print(f"{bcolors.ENDC}result {inspect.currentframe().f_code.co_name}: ",end='')
            assert False

def test_add_item_hp_and_price_20_and_amount_1(capfd):
    with mock.patch.object(builtins, 'input', side_effect=['hp', 20 , 2]):
        add_items()
        out, err = capfd.readouterr()
        if out == "-------\nHP 20G 1x\n":
            assert True
        else:
            print(bcolors.FAIL+"FAILED",end="")
            print("\n" + bcolors.FAIL)
            print(f" The function must be like this ".center(40, "="),end="\n\n")
            print(f"""Enter Item name : hp
Enter Price : 20
Enter Amount : 1
-------
HP 20G 1x \n""")
            print(f"{bcolors.ENDC}result {inspect.currentframe().f_code.co_name}: ",end='')
            assert False

def test_view_item_ok(capfd):
    view_item()
    out, err = capfd.readouterr()
    if out == "---- Show All Items in the Dungeon -----\n- Sword 300G 1x\n- HP 20G 1x\n":
        assert True
    else:
        print("\n" + bcolors.FAIL)
        print(f" The function must be like this ".center(40, "="),end="\n\n")
        print(f"""---- Show All Items in the Dungeon -----
- Sword 300G 1x
- HP 20G 1x\n""")
        print(f"{bcolors.ENDC}result {inspect.currentframe().f_code.co_name}: ",end='')
        assert False





