# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   测试起名机器
# ------------------------(max to 80 columns)-----------------------------------

import sys

sys.path.append('..')
from package_machines.mach_naming import pick_a_full_name

# 测试起名机器
print('\n---测试起名机器--------')
print(pick_a_full_name())
