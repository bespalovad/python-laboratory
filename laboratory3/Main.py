def check ():
	ans = input ()
	if ans == "y":
		main ()
	elif ans != "n":
		print ("Напишіть y якщо хочете продовжити роботу чи n якщо потрібно завершити роботу")
		check()

def main ():
	s = str(input ("Введіть рядок: "))
	list_s = s.split(" ")
	for i in range(len(list_s)):
		if len(list_s[i]) == 5:
			w = ""
			for j in range(3):
				w += list_s[i][j]
			w += "xz"
			list_s[i] = w
	print ("Отримана строка: " + " ".join(list_s))
	print ("Продовжити? (y/n)")
	check ()

print ("Беспалов Антон Дмитрович \nЛабораторна робота №3 \nВаріант 3 \nЗаміна закінчення (останні два символи) на 'xz' у словах, довжина яких дорівнює 5")
main()
