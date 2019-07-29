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
from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_move import EQMove


class Soldier():

    _name = 'ddd'

    @def name():
        doc = "The  property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._ = value
        def fdel(self):
            del self._name
        return locals()
     = property(**())
