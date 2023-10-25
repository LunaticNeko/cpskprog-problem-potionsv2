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
import copy

all_ingr = [('sweetroll', 80), ('nirnroot', 10),
            ('troll fat', 15), ('fire salts', 50),
            ('nightshade', 8), ('bee', 3), ('briar heart', 20),
            ('honeycomb', 5), ('thistle branch', 1)]
all_eff = ['restore health', 'restore magicka', 'levitation', 'invisibility']

def test_1a_object_creation():
    p0 = Potion()
    assert p0.name == 'Potion'
    assert p0.ingredients == []
    assert p0.effects == []

    p1 = Potion('A')
    assert p1.name == 'A'

def test_1b_add_ingredient_name():
    p0 = Potion()
    n_ingredients = random.randint(2,5)
    ingredients_test = []
    for i in range(n_ingredients):
        (ingr, val) = random.choice(all_ingr)
        p0.add_ingredient(ingr, val)
        ingredients_test.append(ingr)
    assert p0.ingredients == ingredients_test

def test_1c_add_ingredient_value():
    p0 = Potion()
    n_ingredients = random.randint(2,5)
    total_val = 0
    for i in range(n_ingredients):
        (ingr, val) = random.choice(all_ingr)
        p0.add_ingredient(ingr, val)
        total_val += val
    assert p0.sale_price == int(total_val * 1.2)

def test_1d_add_ingredient_count():
    p0 = Potion()
    n_ingredients = random.randint(10,20)
    for i in range(n_ingredients):
        (ingr, val) = random.choice(all_ingr)
        p0.add_ingredient(ingr, val)
    assert p0.ingredient_count == n_ingredients

temp = None

def test_1e_add_effect():
    global temp
    p0 = Potion()
    n_effects = random.randint(1,4)
    effects_test = []
    for i in range(n_effects):
        effect = random.choice(all_eff)
        p0.add_effect(effect)
        effects_test.append(effect)
    assert p0.effects == effects_test
    temp = p0

def test_1f_clear_effects():
    global temp
    temp.clear_effects()
    assert temp.effects == []

def test_1g_sale_price():
    p0 = Potion()
    n_ingredients = random.randint(20,30)
    expected_value = 0
    for i in range(n_ingredients):
        ingr, value = random.choice(all_ingr)
        p0.add_ingredient(ingr, value)
        expected_value += value
    assert p0.sale_price == int(expected_value * 1.2)

def test_1h_comp_1():
    p0 = Potion()
    p1 = Potion()
    n_ingredients = random.randint(20,30)
    for i in range(n_ingredients):
        ingr = random.choice(all_ingr)
        p0.add_ingredient(*ingr)
        p1.add_ingredient(*ingr)
    assert p0 == p1

def test_1i_comp_2():
    p0 = Potion()
    p1 = Potion()
    shuf_list = copy.copy(all_ingr)
    random.shuffle(shuf_list)
    for ingr in all_ingr:
        p0.add_ingredient(*ingr)
    for ingr in shuf_list:
        p1.add_ingredient(*ingr)
    assert p0 != p1

def test_1j_comp_3():
    p0 = Potion()
    p1 = Potion()
    n_ingredients = random.randint(20,30)
    for i in range(n_ingredients):
        ingr = random.choice(all_ingr)
        p0.add_ingredient(*ingr)
        p1.add_ingredient(*ingr)
    p0.add_effect('laughing')
    assert p0 != p1
