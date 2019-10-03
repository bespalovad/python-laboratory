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
		print ("Введіть число від 0 до 180")
		a = read ()
	if (a<0) | (a>180):
		print ("Введіть число від 0 до 180")
		a = read ()
	return a

def main ():
	print ("Введіть перший і другий кут трикутника")
	a = read ()
	b = read ()
	g = 180 - a - b
	if (a!=0) & (b!=0) & (g > 0):
		if (a==90) | (b==90) | (g==90):
			print ("Трикутник існує і є прямокутним")
		else: print ("Трикутник існує, але не є прямокутним")
	else: print ("Трикутник не існує")
	print ("Продовжити? (y/n)")
	check ()

print ("Беспалов Антон Дмитрович \nЛабораторна робота №1 \nВаріант 3 \nПеревірка на існування трикутника")
main()

