def getWeaponNums(num):
	rplist = []
	for i in range(num + 1):
		for j in range(num - i + 1):
			for k in range(num - i - j + 1):
				if(i+j+k == num):
					rplist.append((i, j, k))
	return rplist

def dmgUp(num1, num2):
	return 2.2*(num1*0.16 + num2*0.2)

def enmity(num, hp):
	return 2.2*num*0.075*(1+2*(1-hp))*(1-hp)

def stamina(num, hp):
	if(hp<0.25):
		return 0
	else:
		return 2.2*num*(((hp*100)/(60.4-15))**2.9+2.1)/100

def critical(num):
	possibility = num*0.096*2.2
	return (possibility*1.5 + 1 - possibility)

def main():
	"""weaponNum = int(input('Total omega weapon number: '))"""
	weaponNum = int(input(u'方阵武器总数：'))
	hpPercent = float(input(u'目前血量(如果为50%，请输入小数0.5)：'))
	weaponList = getWeaponNums(weaponNum)
	maxDmg = 1.0
	maxDmgWeapons = (0,0,0)
	for i in range(len(weaponList)):
		tdmgUp = dmgUp(weaponList[i][0],weaponList[i][1])
		tenmity = enmity(weaponList[i][0],hpPercent)
		tstamina = stamina(weaponList[i][2],hpPercent)
		tcritical = critical(weaponList[i][2])
		totalDmg = (1 + tdmgUp) * (1 + tenmity) * (1 + tstamina) * (tcritical)
		if(totalDmg>maxDmg):
			maxDmg = totalDmg
			maxDmgWeapons = weaponList[i]

	print(u'方阵乘区倍率 = ' + str(maxDmg))
	print(u'此时乘区情况: ')
	print(u'方阵攻刃: '+str(dmgUp(maxDmgWeapons[0],maxDmgWeapons[1])))
	print(u'背水乘区: '+str(enmity(maxDmgWeapons[0],hpPercent)))
	print(u'浑身乘区: '+str(stamina(maxDmgWeapons[2],hpPercent)))
	print(u'暴击期望: '+str(critical(maxDmgWeapons[2])))
	print(u'武器选择最优解: ')
	print(u'风铳: ' + str(maxDmgWeapons[0]))
	print(u'风拳: ' + str(maxDmgWeapons[1]))
	print(u'军神琴: ' + str(maxDmgWeapons[2]))
	input()

if __name__ == '__main__':
    main()