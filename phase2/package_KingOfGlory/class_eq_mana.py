# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   法术类道具
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
# 引用自定义的类及功能包
import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_equipment import Equipment


class EQMana(Equipment):

    # 添加独有加成
    add_mana_attack = 0.0

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
        print('      法术攻击+%2d' % (self.add_mana_attack))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '咒术典籍',
            '蓝宝石',
            '炼金护符',
            '圣者法典',
            '元素杖',
            '大棒',
            '破碎圣杯',
            '光辉之剑',
            '魅影面罩',
            '进化水晶',
            '血族之书',
            '炽热支配者'
            '梦魇之牙',
            '虚无法杖',
            '博学者之怒'
            '辉月',
            '回响之杖',
            '冰霜法杖',
            '痛苦面具',
            '巫术法杖',
            '圣杯',
            '时之预言',
            '贤者之书',
            '噬神之书'
        )

        return random.choice(all_eq_name)

    def __forge_eq(self, skill_num):
        ''' 锻造道具 '''
        if skill_num == 0:  # +物理攻击
            pass
        elif skill_num == 1:  # +物理防御
            pass
        elif skill_num == 2:  # +法术防御
            pass
        elif skill_num == 3:  # +回蓝
            self.add_mana_restore += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 4:  # +移动速度
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        elif skill_num == 5:  # +最大生命
            self.add_life_force += 0.05 * GLV.MAX_LIFE_FORCE
        elif skill_num == 6:  # +最大法力
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 7:  # +暴击率
            pass
        elif skill_num == 8:  # +物理吸血
            pass
        elif skill_num == 9:  # +法术攻击
            self.add_mana_attack += 0.05 * GLV.MAX_ATTACK
        elif skill_num == 10:  # +回血
            pass
        else:
            pass

        return
