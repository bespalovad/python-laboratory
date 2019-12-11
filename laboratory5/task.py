import re

def setOperations ():
	a = {1,2,"ee","a","d"}
	b = {"a","ee",4,2}
	f = ((a|b)&(a-b))
	return (f)

def readArr ():
	num_str = input ("Введіть ваш рядок:\n")
	while not bool (re.match(r'([ ]*((?:[0]\.\d+)|(?:[1-9](?:\d+)?(?:\.\d+)?))*)+\Z', num_str)):
		num_str = input ("Ваш рядок повинен складатися з дійсних чисел та пробілів. Введіть ще раз:\n")
	return (num_str.split())
	
def localSumList (num_list):
	local_sum_list = []
	for i in range(int(len(num_list)) - 1):
		local_sum_list.append(float(num_list[i-1]) + float(num_list[i+1]))
	if not (int(len(num_list)) == 1):
		local_sum_list.append(float(num_list[-2]) + float(num_list[0]))
	else: return num_list
	return local_sum_list

def formStr (local_sum_list):
	local_sum_str = str(local_sum_list[0])
	for i in range(len(local_sum_list) - 1):
		local_sum_str += " " + str(local_sum_list[i+1])
	return local_sum_str

def main():
	print ("Беспалов Антон Дмитрович \nЛабораторна робота №5 \nВаріант 3")
	print ("1) Локальні суми елементів списку")
	print ("2) Операції над множинами")
	while True:
		run_num = input ("Яку програму бажаєте запустити: ")
		while not bool (re.match(r'[1]|[2]\Z', run_num)):
			run_num = input ("Введіть номер програми: ")
		if run_num == "1":
			print (formStr(localSumList(readArr())))
		elif run_num == "2":
			print (setOperations())
		run = input ("Чи бажаєте продовжити роботу(y/n): ")
		while not bool (re.match(r'[y]|[n]\Z', run)):
			run = input ("Введіть y або n: ")
		if run == "n":
			return 0
	return 0

if __name__ == '__main__':
	main()

