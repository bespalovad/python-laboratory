def cont ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		cont()

def read_float ():
	try:
		a = float(input ())
	except ValueError:
		print ("Введіть число")
		a = read_float ()
	return a
	
def read_natur ():
	try:
		a = int(input ())
	except ValueError:
		print ("Введіть натуральне число")
		a = read_natur ()
	if (a < 1):
		print ("Введіть натуральне число")
		a = read_natur ()
	return a

def main ():
	print ("Введіть кількість ітерацій")
	n = read_natur ()
	print ("Введіть значення константи")
	x = read_float()
	s = 0
	for i in range (1, n+1):
		s += i*i - x*x
	print ("Сума дорівнює %.10f" % s)
	print ("Продовжити? (y/n)")
	cont ()
	
print ("Беспалов Антон Дмитрович \nЛабораторна робота №2 \nВаріант 3 \nЗнахождення суми послідовності")
main()
