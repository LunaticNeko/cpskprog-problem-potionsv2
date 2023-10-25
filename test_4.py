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
            ('honeycomb', 5), ('thistle branch', 1), ('pepsi', 10), ('milk', 5)]
all_eff = ['restore health', 'restore magicka', 'levitation', 'invisibility']

def test_4a_bigmix():
    time_start = time.time()
    ingrs = []
    sum_value = 0
    p1 = Potion()
    for i in range(1000):
        ingr, value = random.choice(all_ingr)
        p1.add_ingredient(ingr, value)
        ingrs.append(ingr)
        sum_value += value
    p2 = Potion()
    for i in range(1000):
        ingr, value = random.choice(all_ingr)
        p2.add_ingredient(ingr, value)
        ingrs.append(ingr)
        sum_value += value
    p3 = p1 + p2
    time_end = time.time()
    assert p3.ingredients == ingrs
    assert p3.sale_price == int(sum_value * 1.2)
    assert time_end - time_start < 10 # time limit 10s

def test_4b_ultramix(capsys):
    time_start = time.time()
    try:
        p0 = Potion('changed later')
    except Exception:
        p0 = Potion()
        with capsys.disabled():
            print("Well, the potion name can't be changed later, after all.")
            print("This incident will be reported.")
    for i in range(1000):
        p = Potion()
        for j in range(10):
            p.add_ingredient(*random.choice(all_ingr))
        p0 = p0 + p
    time_end = time.time()
    assert time_end - time_start < 10 # time limit 10s
