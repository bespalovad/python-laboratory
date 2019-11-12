import math

def read_cont ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		read_cont()
	return None
		
def read_x ():
	try:
		x = float(input ("Введіть значення аргумента: "))
	except ValueError:
		print ("Введіть дійсне число")
		x = read_tries ()
	return x
	
def func(x, f):
	if f == "s":
		return float(math.sin(x))
	elif f == "c":
		return float(math.cos(x))
	elif f == "l":
		try:
			return float(math.log(x))
		except Exception:
			return None
	return None
	
def bubble (a, dirct):
	f = 1
	while f:
		f = 0
		for i in range (2):
			if dirct == "up":
				if (a[i] > a[i+1]):
					f = 1
					t = a[i]
					a[i] = a[i+1]
					a[i+1] = t
			elif dirct == "down":
				if (a[i] < a[i+1]):
					f = 1
					t = a[i]
					a[i] = a[i+1]
					a[i+1] = t
	return a

def main():
	x = read_x()
	a = 3*[""]
	a[0] = func(x, "l")
	if a[0] != None:
		a[1] = func(x, "c")
		a[2] = func(x, "s")
		a = bubble (a, "up")
		print (str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
	else:
		print ("Логарифм від недодатнього числа неможливий")
	print ("Продовжити? (y/n)")
	read_cont ()
	return 0
	

if __name__ == '__main__':
	print ("Беспалов Антон Дмитрович \nЛабораторна робота №4 \nВаріант 3 \nВивід результату обчислення функцій для одного значення аргумента")
	main()

