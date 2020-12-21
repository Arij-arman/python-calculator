
"""CREATED ON *DATE=21 DEC,2020 *TIME=23:00-23.38 """
########################################
# DEVELOPER'S NAME:- ARIJ ARMAN MANDAL #
# CONTACT:-mrxanonymous633@gmail.com   #
# KEEP SUPORTING ME..... THANK YOU     #
########################################
#A Simple python code using only IF-ELIF-ELSE conditios .
i = 1
while 1 :
	print('###########_W_E_L_C_O_M_E###########')
	print('  ________________________________')
	print('  ___________CALCULATOR___________')
	print('************************************')
	print('[1] Add or Plus                  [99] Exit(press 99 and enter)')
	print('[2] Substract or Minus')
	print('[3] Multiply or into(x)')
	print('[4] Division or x/y')
	user = int(input('(@)_Choose a number[1-4]: '))
	if user == 1 :
		num1 = input('[*] Enter the 1st number: ')
		num2 = input('[*] Enter the 2nd number: ')
		print('>>>>Answer is= ',num1+num2)
	elif user == 2 :
		num1 = input('[*] Enter the 1st number: ')
		num2 = input('[*] Enter the 2nd number: ')	
		print('>>>>Answer is= ',num1-num2)
	elif user == 3 :
		num1 = input('[*] Enter the 1st number: ')
		num2 = input('[*] Enter the 2nd number: ')	
		print('>>>>Answer is= ',num1*num2)
	elif user == 4 :
		num1 = input('[*] Enter the 1st number: ')
		num2 = input('[*] Enter the 2nd number: ')	
		print('>>>>Answer is= ',num1/num2)
	elif user == 99 :
		print('>>>> Exited claculator. Have a nice day...')
		exit()
	else  :
		print('>>>> Error! Invalid input. Try 1 or 2 or 3 or 4')
i += 1
