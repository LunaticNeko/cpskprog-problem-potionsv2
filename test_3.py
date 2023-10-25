"""

TEST CODE
01219114 Computer Programming
Week 10, Long Program Assignment: Potion Shop (V2)
(C) 2023 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

from potions import Potion
import random
import time
import pytest

all_ingr = [('sweetroll', 80), ('nirnroot', 10),
            ('troll fat', 15), ('fire salts', 50),
            ('nightshade', 8), ('bee', 3), ('briar heart', 20),
            ('honeycomb', 5), ('thistle branch', 1)]
all_eff = ['restore health', 'restore magicka', 'levitation', 'invisibility']

def test_3a_privacy():
    assert isinstance(Potion.name, property)
    assert isinstance(Potion.ingredients, property)
    assert isinstance(Potion.effects, property)
    assert isinstance(Potion.sale_price, property)
    assert Potion.name.fset is None
    assert Potion.ingredients.fset is None
    assert Potion.effects.fset is None

def test_3b_validation_initialization_1():
    with pytest.raises(TypeError):
        p = Potion(1)

def test_3c_validation_initialization_2():
    with pytest.raises(ValueError):
        p = Potion(' ')

def test_3d_validation_ingredient_1():
    p = Potion()
    with pytest.raises(TypeError):
        p.add_ingredient(1, 1)

def test_3e_validation_ingredient_2():
    p = Potion()
    with pytest.raises(TypeError):
        p.add_ingredient('nirnroot', 1.1)

def test_3f_validation_ingredient_3():
    p = Potion()
    with pytest.raises(ValueError):
        p.add_ingredient(' ', 1)
    with pytest.raises(ValueError):
        p.add_ingredient('', 1)

def test_3g_validation_ingredient_4():
    p = Potion()
    with pytest.raises(ValueError):
        p.add_ingredient('nirnroot', -2)

def test_3h_validation_effects_1():
    p = Potion()
    with pytest.raises(TypeError):
        p.add_effect(1)

def test_3i_validation_effects_2():
    p = Potion()
    with pytest.raises(ValueError):
        p.add_effect(' ')
    with pytest.raises(ValueError):
        p.add_effect('')

def test_3j_mixing():
    p1 = Potion()
    p1.add_ingredient('fire salts', 50)
    p1.add_effect('restore mana')
    p1.add_effect('resist fire')
    p2 = Potion()
    p2.add_ingredient('frost salts', 100)
    p2.add_effect('restore mana')
    p2.add_effect('resist frost')
    p3 = p1 + p2
    assert p3.name == 'Mixed Potion'
    assert p3.ingredient_count == 2
    assert p1 + p2 == p1 + p2
    assert p1 + p2 != p2 + p1
