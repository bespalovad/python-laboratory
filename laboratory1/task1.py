import math

def check ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		check()

def read ():
	try:
		a = float(input ())
	except ValueError:
		print ("Введіть число")
		a = read ()
	return a

def main ():
	print ("Введіть перший і другий катет трикутника")
	a = read ()
	b = read ()
	hyp = math.sqrt(a*a + b*b)
	per = a + b + hyp
	area = a * b / 2
	print ("Гіпотенуза трикутника дорінює %.10f" % hyp)
	print ("Периметр трикутника дорівнює %.10f" % per)
	print ("Площа трикутника дорівнює %.10f" % area)
	print ("Продовжити? (y/n)")
	check ()
	
print ("Беспалов Антон Дмитрович \nЛабораторна робота №1 \nВаріант 3 \nЗнахождення гіпотенузи, периметра та площі трикутника")
main()
