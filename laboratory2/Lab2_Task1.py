import re

def cont ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		cont()

def read_float ():
	a = input ()
	while not bool (re.match(r'[+-]?((?:[0]\.\d+)|(?:[1-9](?:\d+)?(?:\.\d+)?))\Z', a)):
		print ("Введіть дійсне число")
		a = input ()
	return float(a)
	
def read_natur ():
	a = input ()
	while not bool (re.match(r'[1-9](\d+)?\Z', a)):
		print ("Введіть натуральне число")
		a = input ()
	return int(a)

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
