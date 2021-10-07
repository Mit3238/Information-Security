def encript(string, key):
	li = [[] for i in range(len(key))] 

	for i in range(len(string)):
		li[i%len(key)].append(string[i])

	answer = ''
	for i in range(1, len(key)+1):
		for j in range(len(key)):
			if str(i) == key[j]:
				for k in range(len(li[j])):
					answer += li[j][k]
				break

	return answer


def decript(string, key):
	li = [[] for i in range(len(key))]
	num = len(string) // len(key)
	mod = len(string) % len(key)
	lenn = []

	for i in range(len(key)):
		if mod >= 1:
			mod -= 1
			lenn.append(num+1)
		else:
			lenn.append(num)
	
	k = 0
	for i in range(len(key)):
		a = int(key[i]) - 1
		for j in range(lenn[a]):
			li[a].append(string[k])
			k += 1

	answer = ''
	j = 0
	while True:
		for i in range(len(key)):
			try:
				answer += li[i][j]
			except:
				return answer
		j += 1


while True:
	print("[1]  Encription")
	print("[2]  Decription")
	print("[3]  Exit")
	option = input("Please select options from 1-3 :")

	if option == '3':
		print("Thank You")
		break

	string = input("Enter The String : ")
	key = input("Enter The Key : ")

	if option == '1':
		encripted = encript(string, key)
		print("Encripted Text :", encripted, end='\n\n')
	elif option == '2':
		decripted = decript(string, key)
		print("Decripted Text :", decripted, end='\n\n')
	else:
		print("Enter valid option")
