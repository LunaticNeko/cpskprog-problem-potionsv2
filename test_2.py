"""

TEST CODE
01219114 Computer Programming
Week 8, Long Program Assignment: Potion Shop (V1)
(C) 2023 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

from potions import Potion
import random
import time

all_ingr = [('sweetroll', 80), ('nirnroot', 10),
            ('troll fat', 15), ('fire salts', 50),
            ('nightshade', 8), ('bee', 3), ('briar heart', 20),
            ('honeycomb', 5), ('thistle branch', 1)]
all_eff = ['restore health', 'restore magicka', 'levitation', 'invisibility']

def time_multipotions(n_potions, n_ingredients, n_tests):
    time_start = time.time()
    for i in range(n_potions):
        p = Potion()
        for j in range(n_ingredients):
            p.add_ingredient(*random.choice(all_ingr))
        if n_tests > 0:
            for k in range(n_tests):
                p.ingredient_value
                p.ingredient_count()
    time_end = time.time()

def test_2a_time1():
    time_start = time.time()
    time_multipotions(1000, 100, 0)
    time_end = time.time()
    assert time_end - time_start < 4 # time limit 4s

def test_2b_time2():
    time_start = time.time()
    time_multipotions(10000, 100, 0)
    time_end = time.time()
    assert time_end - time_start < 8 # time limit 9s

def test_2c_time3():
    """ repeated access """
    time_start = time.time()
    time_multipotions(1000, 100, 10000)
    time_end = time.time()
    assert time_end - time_start < 6 # time limit 6s

def test_2d_time4():
    """ same as above but tougher """
    time_start = time.time()
    time_multipotions(3000, 100, 10000)
    time_end = time.time()
    assert time_end - time_start < 18 # time limit 18s
