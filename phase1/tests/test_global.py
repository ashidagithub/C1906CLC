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
value = random.randint(0.8 * GLV.MAX_LIFE_FORCE, GLV.MAX_LIFE_FORCE)
print(value)

# 测试全局变量2
type = random.choice(GLV.TYPE_OF_HERO)
print(type)
name = GLV.DICT_OF_HERO[type]
print(name)
