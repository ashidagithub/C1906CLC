# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   练习创建一个完整的攻击道具类
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
# 引用自定义的类及功能包
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_move import EQMove

print('\n---- 测试生成一个攻击类道具 ---')
test_eq = EQAttack()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---- 测试生成一个法术类道具 ---')
test_eq = EQMana()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---- 测试生成一个防御类道具 ---')
test_eq = EQDefense()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---- 测试生成一个移动类道具 ---')
test_eq = EQMove()
test_eq.show_me()
test_eq.show_me_unique()
