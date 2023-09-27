import pytest
import mock
import builtins
from manage_the_dungeon import add_items, view_item

def test_add_item_sword_and_price_300_amount_1_ok(capfd):
    with mock.patch.object(builtins, 'input', side_effect=['Sword', 300 , 1]):
        add_items()
        out, err = capfd.readouterr()
        assert out == "-------\nSword 300G 1x\n"

def test_add_item_hp_and_price_20_amount_1_ok(capfd):
    with mock.patch.object(builtins, 'input', side_effect=['hp', 20 , 1]):
        add_items()
        out, err = capfd.readouterr()
        assert out == "-------\nHP 20G 1x\n"

def test_view_item_ok(capfd):
    view_item()
    out, err = capfd.readouterr()
    assert out == "---- Show All Items in the Dungeon -----\n- Sword 300G 1x\n- HP 20G 1x\n"