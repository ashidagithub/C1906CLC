# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   练习创建一个完整的士兵
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV

from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_soldier import Soldier

from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_move import EQMove

# 创建一个手持攻击类武器的士兵
h = Hero()
eq = EQAttack()
s = Soldier(h, eq)
s.show_me()

# 创建一个手持防御类武器的士兵
h = Hero()
eq = EQDefense()
s = Soldier(h, eq)
s.show_me()

# 创建一个手持法术类武器的士兵
h = Hero()
eq = EQMana()
s = Soldier(h, eq)
s.show_me()

# 创建一个手持移动类武器的士兵
h = Hero()
eq = EQMove()
s = Soldier(h, eq)
s.show_me()
