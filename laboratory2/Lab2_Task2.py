import re

def cont ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		cont()
	
def read_natur ():
	a = input ()
	while not bool (re.match(r'[1-9](\d+)?\Z', a)):
		print ("Введіть натуральне число")
		a = input ()
	return a

def main ():
	print ("Введіть число")
	n = str(read_natur ())
	even_count = 0
	n_len = len(n)
	i = 0
	while (i < n_len):
		if (int(n[i]) % 2 == 0):
			even_count += 1
		i += 1
	print ("Кількість парних цифр дорівнює", even_count)
	print ("Продовжити? (y/n)")
	cont ()
	
print ("Беспалов Антон Дмитрович \nЛабораторна робота №2 \nВаріант 3 \nЗнахождення кількості парних цифр числа")
main()
