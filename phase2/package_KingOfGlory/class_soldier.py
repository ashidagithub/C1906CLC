# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   士兵的类
# ------------------------(max to 80 columns)-----------------------------------

import sys

sys.path.append('..')
# 引用自定义的类及功能包
import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_move import EQMove


class Soldier():

    def __init__(self, h, *arg):
        # 获取装备类
        eq = arg[0]

        # 不需要计算的属性
        self.__name = h.name
        self.__position = h.position
        self.__weapon_name = eq.name

        # 需要结合 Hero 和 EQ 进行计算的属性(计算初始值)
        self.__life_force = h.life_force + eq.add_life_force
        self.__mana_power = h.mana_power + eq.add_mana_power
        self.__move_speed = h.move_speed + eq.add_move_speed

        self.__physical_attack = h.physical_attack + eq.add_physical_attack
        self.__physical_defense = h.physical_defense + eq.add_physical_defense

        self.__mana_defense = h.mana_defense + eq.add_mana_defense

        # 仅部分道具有的特殊技能
        self.__critical_strik = 0.0
        self.__physical_suck = 0.0
        self.__mana_attack = 0
        self.__restore_life_force = 0.0

        if type(eq) is EQAttack:
            self.__critical_strik = eq.critical_strik
            self.__physical_suck = eq.physical_suck
            self.__weapon_type = '攻击类'
        elif type(eq) is EQDefense:
            self.__restore_life_force = eq.restore_life_force
            self.__weapon_type = '防御类'
        elif type(eq) is EQMana:
            self.__mana_attack = h.mana_attack + eq.add_mana_attack
            self.__weapon_type = '法术类'
        elif type(eq) is EQMove:
            self.__weapon_type = '移动类'
        else:
            pass
            print('道具类型错误')

        return

    # 显示士兵自身所有信息
    def show_me(self):
        print('\n-----招募了一个新的士兵-----')
        # print('\n-----只读（不会变化的）属性-----')
        print('士兵名称:【%s】\t' % (self.name),end='')
        print('士兵定位:%s(%s)\t' % (self.position, GLV.DICT_OF_HERO[self.position]),end='')
        print('士兵武器:%s(%s)' % (self.weapon_name, self.__weapon_type))
        #print('\n**不变的固有能力（所有士兵都具备的能力）**')
        print('物攻力=%3d\t' % (self.physical_attack),end='')
        print('法攻力=%3d\t' % (self.mana_attack),end='')
        print('移动速度=%3d' % (self.move_speed))
        #print('\n**不变的固有能力（依靠道具才具备的能力）**')
        print('暴击率=%0.2f\t' % (self.critical_strik),end='')
        print('物理吸血=%0.2f\t' % (self.physical_suck),end='')
        print('回血=%0.2f' % (self.restore_life_force))

        # print('\n-----只读（会变化的）属性-----')
        #print('\n**随着战争而变化的能力，以下为当前数值*')
        print('生命值=%3d\t' % (self.cur_life_force),end='')
        print('法力值=%3d\t' % (self.cur_mana_power),end='')
        print('物防力=%3d\t' % (self.cur_physical_defense),end='')
        print('法防力=%3d' % (self.cur_mana_defense))

        return

    # 定义士兵类的只读（不变）属性 ----------------------------
    @property # 士兵的姓名（不变）
    def name(self):
        return self.__name

    @property # 士兵的定位（不变）
    def position(self):
        return self.__position

    @property # 士兵的武器名称（不变）
    def weapon_name(self):
        return self.__weapon_name

    @property # 移动速度（不变）
    def move_speed(self):
        return self.__move_speed

    @property # 物理攻击力（不变）
    def physical_attack(self):
        return self.__physical_attack

    @property # 法术攻击力（不变）
    def mana_attack(self):
        return self.__mana_attack

    @property # 暴击率%（不变）
    def critical_strik(self):
        return self.__critical_strik

    @property # 物理吸血%（不变）
    def physical_suck(self):
        return self.__physical_suck

    @property # 回血%（不变）
    def restore_life_force(self):
        return self.__restore_life_force

    # 定义士兵类的只读（可变）属性 ----------------------------
    @property # 当前生命力
    def cur_life_force(self):
        return self.__life_force

    @property # 当前生命力
    def cur_mana_power(self):
        return self.__mana_power

    @property # 物理防御力（可变）
    def cur_physical_defense(self):
        return self.__physical_defense

    @property # 法术防御力（可变）
    def cur_mana_defense(self):
        return self.__mana_defense

    # 定义士兵类的行为 ----------------------------
