# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   英雄所使用的全局变量
#   字典类型的学习
# ------------------------(max to 80 columns)-----------------------------------


# 定义最大及最小生命值
MAX_LIFE_FORCE = 1000
#MIN_LIFE_FORCE = 100

# 定义最大及最小法力值
MAX_MANA_POWER = 1000
#MIN_MANA_POWER = 100

# 定义最大及最小移动速度值
MAX_MOVE_SPEED = 100
MIN_MOVE_SPEED = 1

# 定义最大及最小攻击力、防御力
MAX_ATTACK = 100
MIN_ATTACK = 1
MAX_DEFENSE = 100
MIN_DEFENSE = 1

# 用字典定义战士的类型
TYPE_OF_HERO = ('TANK', 'WARRIOR', 'ASSASSIN', 'MAGE', 'ARCHER')
DICT_OF_HERO = {
    'TANK': '坦克',
    'WARRIOR': '战士',
    'ASSASSIN': '刺客',
    'MAGE': '法师',
    'ARCHER': '射手'
}

# 道具有效条件
TYPE_OF_EQUIPMENT_EFFECT = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
DICT_OF_EQUIPMENT_EFFECT = {
    0:'持续有效',
    1:'一次性有效',
    2:'仅物攻时有效',
    3:'仅物防时有效',
    4:'仅法攻时有效',
    5:'仅法防时有效',
    6:'物攻或法攻时都有效',
    7:'物防或法防时都有效',
    8:'当生命值高于10%时有效',
    9:'当法力值高于10%时有效'
}

# 定义最大及最小锻造次数
MAX_FORGE_TIMES = 20
