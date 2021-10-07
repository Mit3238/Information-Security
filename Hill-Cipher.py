def multipy(arr1, arr2):
	c = [0 for i in range(3)]
	for i in range(3):
		for j in range(1):
			for k in range(3):
				c[i] += (int(arr1[i][k]) * int(arr2[k][j]))
			c[i] = c[i] % 26

	return c


def encript(string, key):
	string = string.upper().replace(' ', '')
	abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if len(string) % 3 == 1:
		string += 'XX'
	if len(string) % 3 == 2:
		string += 'X'

	ans = ''
	for i in range(0, len(string), 3):
		a = []
		a.append([(abc.index(string[i]))])
		a.append([(abc.index(string[i+1]))])
		a.append([(abc.index(string[i+2]))])

		b = multipy(key, a)
		ans += abc[b[0]]
		ans += abc[b[1]]
		ans += abc[b[2]]

	return ans


def decript(string, key):
	string = string.upper()
	abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if len(string) % 3 == 1:
		string += 'XX'
	if len(string) % 3 == 2:
		string += 'X'

	ans = ''
	for i in range(0, len(string), 3):
		a = []
		a.append([(abc.index(string[i]))])
		a.append([(abc.index(string[i+1]))])
		a.append([(abc.index(string[i+2]))])

		b = multipy(key, a)
		ans += abc[b[0]]
		ans += abc[b[1]]
		ans += abc[b[2]]
		
	return ans


while True:
	print("[1]  Encription")
	print("[2]  Decription")
	print("[3]  Exit")
	option = input("Please select options from 1-3 :")

	if option == '3':
		print("Thank You")
		break

	string = input("Enter The String : ")
	key_e = [[2, 8, 15], [7, 4, 17], [8, 13, 6]]
	key_d = [[3, 7, 16], [2, 6, 17], [9, 8, 20]]

	if option == '1':
		encripted = encript(string, key_e)
		print("Encripted Text :", encripted, end='\n\n')
	elif option == '2':
		decripted = decript(string, key_d)
		print("Decripted Text :", decripted, end='\n\n')
	else:
		print("Enter valid option")
