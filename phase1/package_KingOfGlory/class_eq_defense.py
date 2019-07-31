# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   防御类道具
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
# 引用自定义的类及功能包
from package_KingOfGlory.class_equipment import Equipment
import package_KingOfGlory.global_var as GLV


class EQDefense(Equipment):

    # 添加独有加成
    restore_life_force = 0.0

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
        print('       +回血:%0.2f' % (self.restore_life_force))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '红玛瑙',
            '布甲',
            '抗魔披风',
            '提神水晶',
            '力量腰带',
            '熔炼之心',
            '神隐斗篷',
            '雪山圆盾',
            '守护者之铠',
            '反伤刺甲',
            '血魔之怒',
            '红莲斗篷',
            '霸者重装',
            '不祥征兆',
            '不死鸟之眼',
            '魔女斗篷',
            '极寒风暴',
            '冰痕之握',
            '护贤者的庇护',
            '暴烈之甲'
        )

        return random.choice(all_eq_name)

    def __forge_eq(self, skill_num):
        ''' 锻造道具 '''
        if skill_num == 0:  # +物理攻击
            self.add_physical_attack += 0.05 * GLV.MAX_ATTACK
        elif skill_num == 1:  # +物理防御
            self.add_physical_defense += 0.05 * GLV.MAX_ATTACK
        elif skill_num == 2:  # +法术防御
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 3:  # +回蓝
            pass
        elif skill_num == 4:  # +移动速度
            pass
        elif skill_num == 5:  # +最大生命
            self.add_life_force += 0.05 * GLV.MAX_LIFE_FORCE
        elif skill_num == 6:  # +最大法力
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 7:  # +暴击率
            pass
        elif skill_num == 8:  # +物理吸血
            pass
        elif skill_num == 9:  # +法术攻击
            pass
        elif skill_num == 10:  # +回血
            self.restore_life_force = random.uniform(0.01, 0.1)
        else:
            pass

        return
