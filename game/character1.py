#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-28 17:59
# @Author : yooli
# @file : character1.py
from random import random

from characters import *

p1 = Characters()
p2 = Characters()
#列表推导式
power = [x for x in range(1,301)]
print(power)
print(type(power))
#从列表中随机挑选一个值
#自动导包 ： alt + 回车
p2_power = random.choice(power)
print(p2_power)
while True:
	p1_hp = p1.fight(200)
	p2_hp = p2.fight(p2_power)
	print("p1:",p1_hp)
	print("p2:",p2_hp)
	if p1_hp <= 0 and p1_hp < p2_hp:
		print("p1我输了")
		break
	elif p2_hp <= 0 :
		print("p1我赢了")
		break