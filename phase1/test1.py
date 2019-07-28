# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   练习创建一个完整的英雄类
#   学习使用全局变量
# ------------------------(max to 80 columns)-----------------------------------

import random

import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_hero import Hero
from package_machines.mach_naming import pick_a_full_name

# 测试全局变量1
value = random.randint(GLV.MIN_ATTACK, GLV.MAX_ATTACK)
print(value)

# 测试全局变量2
type = random.choice(GLV.TYPE_OF_HERO)
print(type)
name = GLV.DICT_OF_HERO[type]
print(name)

# 测试起名机器
print('\n---起名机器测试--------')
print(pick_a_full_name())

# 测试英雄生成
for i in range(50):
    hero = Hero()
    hero.show_presentation()
