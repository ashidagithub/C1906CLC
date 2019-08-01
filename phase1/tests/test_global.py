# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用全局变量
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV

# 测试全局变量1
print('\n-------- cutting line --------')
value = random.randint(0.8 * GLV.MAX_LIFE_FORCE, GLV.MAX_LIFE_FORCE)
print(value)

# 测试全局变量2
print('\n-------- cutting line --------')
type = random.choice(GLV.TYPE_OF_HERO)
print(type)

# 测试全局变量及字典
print('\n-------- cutting line --------')
print(GLV.DICT_OF_HERO['TANK'])
print('\n-------- cutting line --------')
name = GLV.DICT_OF_HERO[type]
print(name)
