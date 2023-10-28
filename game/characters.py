#!D:\pythonProject\test1\venv python
# -*- coding:utf-8 -*-
# @Time : 2023-10-28 15:59
# @Author : yooli
# @file : characters.py

class Characters:

	hp = 1000
	power = 200

	def fight(self,power):
		self.hp = self.hp - power
		return self.hp


def main():
	p1 = Characters()
	p2 = Characters()
	p1_hp = p1.fight(300)
	p2_hp = p2.fight(200)
	print("p1_final_hp:",p1_hp)
	print("p2_final_hp:",p2_hp)

	#三目运算 等同于下面的 if-else ,只是语法简洁一些
	print("p1我赢了") if p1_hp > p2_hp else print("p1我输了")

	# 注释快捷键 ：ctrl + /
	# 复制当前行的代码 ：ctrl + d
	# if p1_hp > p2_hp:
	# 	print("我赢了")
	# else:
	# 	print("我输了")




if __name__ == '__main__':
	main()


