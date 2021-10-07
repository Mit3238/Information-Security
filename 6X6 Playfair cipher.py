def find(mat, s):
	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j] == s:
				return i, j


def encript(string, key):
	string = string.upper().replace(' ','')
	key = key.upper()
	abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	mat = [[] for i in range(6)]
	col = -1

	i = 0
	while len(key) > 0:
		if i % 6 == 0:
			col += 1
		k = key[0]
		mat[col].append(k)
		key = key.replace(k, '')
		abc = abc.replace(k, '')
		i += 1

	for j in range(len(abc)):
		if i % 6 == 0:
			col += 1
		mat[col].append(abc[j])
		i += 1

	i = 0
	while i < len(string) - 1:
		if string[i] == string[i+1] and string[i] != 'X':
			string = string[:i+1] + 'X' + string[i+1:]
		elif string[i] == 'X':
			string = string[:i+1] + 'Y' + string[i+1:]
		i += 1
	col = 0
	row = 0
	if len(string) % 2 != 0:
		string += 'X'
	ans = ''
	i = 0
	while i < len(string):
		x1, y1 = find(mat, string[i]) 
		x2, y2 = find(mat, string[i+1])

		if x1 == x2:
			y1 = (y1 + 1) % 6
			y2 = (y2 + 1) % 6
		elif y1 == y2:
			x1 = (x1 + 1) % 6
			x2 = (x2 + 1) % 6
		else:
			temp = y1
			y1 = y2
			y2 = temp

		ans = ans + mat[x1][y1] + mat[x2][y2]
		i += 2
	return ans


def decript(string, key):
	string = string.upper().replace(' ','')
	key = key.upper()
	abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	mat = [[] for i in range(6)]
	col = -1

	i = 0
	while len(key) > 0:
		if i % 6 == 0:
			col += 1
		k = key[0]
		mat[col].append(k)
		key = key.replace(k, '')
		abc = abc.replace(k, '')
		i += 1

	for j in range(len(abc)):
		if i % 6 == 0:
			col += 1
		mat[col].append(abc[j])
		i += 1

	col = 0
	row = 0
	if len(string) % 2 != 0:
		string += 'X'
	ans = ''
	i = 0
	while i < len(string):
		x1, y1 = find(mat, string[i]) 
		x2, y2 = find(mat, string[i+1])

		if x1 == x2:
			y1 = (y1 - 1) % 6
			y2 = (y2 - 1) % 6
		elif y1 == y2:
			x1 = (x1 - 1) % 6
			x2 = (x2 - 1) % 6
		else:
			temp = y1
			y1 = y2
			y2 = temp

		ans = ans + mat[x1][y1] + mat[x2][y2]
		i += 2
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
	key = input("Enter The Key : ")

	if option == '1':
		encripted = encript(string, key)
		print("Encripted Text :", encripted, end='\n\n')
	elif option == '2':
		decripted = decript(string, key)
		print("Decripted Text :", decripted, end='\n\n')
	else:
		print("Enter valid option")
