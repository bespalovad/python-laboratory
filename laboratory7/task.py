import re
import random

def task1 (n):
	f = open (r'output.txt', 'w')
	print ("Робота з файлом розпочата...")
	for i in range (n):
		a = random.randint(50,100)
		f.write(str(a) + " ")
	f.close()
	print ("Робота з файлом завершена. Результат у файлі output.txt.")
	return 0

def main():
	print ("Беспалов Антон Дмитрович \nЛабораторна робота №7 \nВаріант 3")
	print ("Генерація випадкових чисел")
	while True:
		task1(15)
		run = input ("Чи бажаєте продовжити роботу(y/n): ")
		while not bool (re.match(r'[y]|[n]\Z', run)):
			run = input ("Введіть y або n: ")
		if run == "n":
			return 0
	return 0

if __name__ == '__main__':
	main()
