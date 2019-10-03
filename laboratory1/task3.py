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
		print ("Введіть дійсне число")
		a = read ()
	return a

def main ():
	print ("Введіть значення аргументу")
	x = read ()
	if (x<=(-3)):
		f = 9
	else:
		f = 1/(x*x +1)
	print ("f = %.10f" % f)
	print ("Продовжити? (y/n)")
	check ()

print ("Беспалов Антон Дмитрович \nЛабораторна робота №1 \nВаріант 3 \nОбчислення функції в залежності від значення введеної змінної")
main()


