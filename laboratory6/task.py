import re

def read1Arr ():
	arr_len = int(input ("Введіть кількість елементів масива: "))
	arr = []
	print ("Введіть елементи масиву:")
	for i in range (arr_len):
		a = input ()
		while not bool (re.match(r'((?:[0](\.\d+)*)|(?:[1-9](?:\d+)?(?:\.\d+)?))+\Z', a)):
			a = input ("Елемент повинем бути дійсним числом. Введіть ще раз:\n")
		arr.append (a)
	return (arr)
	
def swapHalfsArr (arr):
	arr_len = int (len(arr))
	for i in range(int(arr_len/2)):
		t = arr[i]
		arr[i] = arr [i + int((arr_len + 1)/2)]
		arr [i + int((arr_len + 1)/2)] = t
	return arr
	
def read2Arr ():
	arr_line_len = int(input ("Введіть кількість рядків масива: "))
	arr_col_len = int(input ("Введіть кількість стовпців масива: "))
	arr = []
	for i in range (arr_line_len):
		line = []
		for j in range (arr_col_len):
			a = input ()
			while not bool (re.match(r'((?:[0](\.\d+)*)|(?:[1-9](?:\d+)?(?:\.\d+)?))+\Z', a)):
				a = input ("Елемент повинем бути дійсним числом. Введіть ще раз:\n")
			line.append (int(a))
		arr.append(line)
	return (arr)
	
def findMaxAbsSumCol (arr):
	max_col = 0
	max_col_ind = 0
	for j in range(int(len(arr[0]))):
		sum_col = 0
		for i in range(int(len(arr))):
			sum_col += abs(arr[i][j])
		if sum_col > max_col:
			max_col = sum_col
			max_col_ind = j
	return max_col_ind
	
def minColEl (arr, col):
	min_el = arr[0][col]
	for i in range(int(len(arr))):
		if arr[i][col] < min_el:
			min_el = arr[i][col]
	return (min_el)

def task1 ():
	arr = read1Arr()
	arr = swapHalfsArr(arr)
	print (arr)
	return 0
	
def task2 ():
	arr = read2Arr ()
	col = findMaxAbsSumCol(arr)
	print ("Результат: ", minColEl(arr, col))
	return 0

def main():
	print ("Беспалов Антон Дмитрович \nЛабораторна робота №6 \nВаріант 3")
	print ("1) Перестановка половин масиву")
	print ("2) Мінімальний елемент найбільшого за модулем стовбця двомірного масиву")
	while True:
		run_num = input ("Яку програму бажаєте запустити: ")
		while not bool (re.match(r'[1]|[2]\Z', run_num)):
			run_num = input ("Введіть номер програми: ")
		if run_num == "1":
			task1()
		elif run_num == "2":
			task2()
		run = input ("Чи бажаєте продовжити роботу(y/n): ")
		while not bool (re.match(r'[y]|[n]\Z', run)):
			run = input ("Введіть y або n: ")
		if run == "n":
			return 0
	return 0

if __name__ == '__main__':
	main()

