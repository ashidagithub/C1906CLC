# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   练习创建一个完整的英雄类
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys

sys.path.append('..')
from package_KingOfGlory.class_hero import Hero
from package_machines.mach_naming import pick_a_full_name


# 测试起名机器
print('\n---测试起名机器--------')
print(pick_a_full_name())

# 测试英雄生成
print('\n---测试产生一批英雄--------')
for i in range(100):
    hero = Hero()
    hero.show_presentation()
