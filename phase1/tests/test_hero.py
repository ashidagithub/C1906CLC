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


# 测试英雄生成
print('\n---测试产生一批英雄--------')
for i in range(100):
    hero = Hero()
    hero.show_me()
