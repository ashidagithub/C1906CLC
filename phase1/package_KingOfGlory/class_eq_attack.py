# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   攻击类道具
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
# 引用自定义的类及功能包
from package_KingOfGlory.class_equipment import Equipment
import package_KingOfGlory.global_var as GLV


class EQAttack(Equipment):

    # 添加独有加成
    critical_strike = 0.0
    physical_suck = 0.0

    def __init__(self):
        '''按规则随机生成攻击类道具 '''
        # 随机挑选一个道具名称
        self.name = self.__set_name()

        # 随机生成各类加成值
        for i in range(GLV.MAX_FORGE_TIMES):
            n = random.randint(0, 10)
            self.__forge_eq(n)

        return

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +暴击率:%0.2f' % (self.critical_strike))
        print('     +物理吸血:%0.2f' % (self.physical_suck))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '铁剑',
            '匕首',
            '搏击拳套',
            '吸血之镰',
            '鸣刃',
            '冲能拳套',
            '风暴巨剑',
            '日冕',
            '狂暴双刃',
            '陨星',
            '碎星锤',
            '末世',
            '名刀·司命',
            '冰霜长矛',
            '速击之枪',
            '制裁之刃',
            '泣血之刃',
            '无尽战刃',
            '宗师之力',
            '闪电匕首',
            '影刃',
            '暗影战斧',
            '破军',
            '纯净苍穹',
            '逐日之弓',
            '破魔刀',
            '穿云弓',
            '破晓'
        )

        return random.choice(all_eq_name)

    def __forge_eq(self, skill_num):
        ''' 锻造道具 '''
        if skill_num == 0:  # +物理攻击
            self.add_physical_attack += 0.05 * GLV.MAX_ATTACK
        elif skill_num == 1:  # +物理防御
            pass
        elif skill_num == 2:  # +法术防御
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 3:  # +回蓝
            pass
        elif skill_num == 4:  # +移动速度
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        elif skill_num == 5:  # +最大生命
            self.add_life_force += 0.05 * GLV.MAX_LIFE_FORCE
        elif skill_num == 6:  # +最大法力
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 7:  # +暴击率
            self.critical_strike = random.uniform(0.1, 0.5)
            if self.critical_strike>= 0.5:
                self.critical_strike = 0.5
        elif skill_num == 8:  # +物理吸血
            self.physical_suck = random.uniform(0.01, 0.1)
            if self.physical_suck >= 0.1:
                self.physical_suck = 0.1
        elif skill_num == 9:  # +法术攻击
            pass
        elif skill_num == 10:  # +回血
            pass
        else:
            pass

        return
