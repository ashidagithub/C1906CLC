# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   英雄的类
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV
from package_machines.mach_naming import pick_a_full_name


class Hero():

    def __init__(self):
        ''' 初始化一个英雄的函数 '''

        # 生成英雄姓名与定位
        self.name = pick_a_full_name()       # name
        self.position = random.choice(GLV.TYPE_OF_HERO)   # position
        # 生成英雄的生命力（体力）与物理攻防数值
        self.life_force = self.__set_life_force(self.position)
        self.physical_attack = self.__set_physical_attack(self.position)
        self.physical_defense = self.__set_physical_defense(self.position)
        # 生成英雄的法力与法术攻防数值
        self.mana_power = self.__set_mana_power(self.position)
        self.mana_attack = self.__set_mana_attack(self.position)
        self.mana_defense = self.__set_mana_defense(self.position)
        # 生成英雄的移动速度
        self.move_speed = self.__set_move_speed(self.position)
        return

    # Public method
    def show_presentation(self):
        #print('-------------------------------------------------------')
        print('(%s)%s: ' %
              (GLV.DICT_OF_HERO[self.position], self.name), end='')
        print('生命=%3d，物攻=%2d，物防=%2d,' % (
            self.life_force, self.physical_attack, self.physical_defense), end='')
        print('法力=%3d，法攻=%2d，法防=%2d,' % (
            self.mana_power, self.mana_attack, self.mana_defense), end='')
        print('速度=%2d' % (self.move_speed))
        return

    def is_alive(self):
        ''' 自检，判断是否还活着 '''
        rtn = false
        if self.life_force >0:
            rtn = true
        return rtn

    # Private method
    def __set_life_force(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的生命力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.8 * GLV.MAX_LIFE_FORCE, 1.0 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_LIFE_FORCE, 0.8 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_LIFE_FORCE, 0.6 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.2 * GLV.MAX_LIFE_FORCE, 0.4 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.1 * GLV.MAX_LIFE_FORCE, 0.2 * GLV.MAX_LIFE_FORCE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_physical_attack(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的物理攻击力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.2 * GLV.MAX_ATTACK, 0.4 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.8 * GLV.MAX_ATTACK, 1.0 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_ATTACK, 0.6 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                GLV.MIN_ATTACK, 0.2 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.6 * GLV.MAX_ATTACK, 0.8 * GLV.MAX_ATTACK)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_physical_defense(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的物理防御力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.8 * GLV.MAX_DEFENSE, 1.0 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_DEFENSE, 0.8 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.2 * GLV.MAX_DEFENSE, 0.4 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                GLV.MIN_DEFENSE, 0.2 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.4 * GLV.MAX_DEFENSE, 0.6 * GLV.MAX_DEFENSE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_power(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.1 * GLV.MAX_MANA_POWER, 0.2 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4 * GLV.MAX_MANA_POWER, 0.5 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.3 * GLV.MAX_MANA_POWER, 0.4 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.5 * GLV.MAX_MANA_POWER, 1.0 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_MANA_POWER, 0.3 * GLV.MAX_MANA_POWER)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_attack(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法术攻击力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                GLV.MIN_ATTACK, 0.2 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_ATTACK, 0.8 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_ATTACK, 0.6 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.8 * GLV.MAX_ATTACK, 1.0 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_ATTACK, 0.4 * GLV.MAX_ATTACK)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_defense(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法术防御力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.6 * GLV.MAX_DEFENSE, 0.8 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4 * GLV.MAX_DEFENSE, 0.6 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                GLV.MIN_DEFENSE, 0.2 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.8 * GLV.MAX_DEFENSE, 1.0 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_DEFENSE, 0.4 * GLV.MAX_DEFENSE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_move_speed(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的移动速度 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                GLV.MIN_MOVE_SPEED, 0.2 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4 * GLV.MAX_MOVE_SPEED, 0.6 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.8 * GLV.MAX_MOVE_SPEED, 1.0 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.2 * GLV.MAX_MOVE_SPEED, 0.4 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.6 * GLV.MAX_MOVE_SPEED, 0.8 * GLV.MAX_MOVE_SPEED)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value
