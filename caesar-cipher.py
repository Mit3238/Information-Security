def encript(string, key):
	string = string.lower().split()
	ans = []
	for i in range(len(string)):
		ans1 = ''
		for j in range(len(string[i])):
			ans1 = ans1 + chr((ord(string[i][j]) + key - 97) % 26 + 97)
		ans.append(ans1)
	
	answer = ''
	for i in range(len(ans)):
		answer = answer + ans[i] + ' '
	return answer


def decript(string, key):
	string = string.lower().split()
	ans = []
	for i in range(len(string)):
		ans1 = ''
		for j in range(len(string[i])):
			ans1 = ans1 + chr((ord(string[i][j]) - key - 97) % 26 + 97)
		ans.append(ans1)
	
	answer = ''
	for i in range(len(ans)):
		answer = answer + ans[i] + ' '
	return answer


while True:
	print("[1]  Encription")
	print("[2]  Decription")
	print("[3]  Exit")
	option = input("Please select options from 1-3 :")

	if option == '3':
		print("Thank You")
		break

	string = input("Enter The String : ")
	key = int(input("Enter The Key : "))

	if option == '1':
		encripted = encript(string, key)
		print("Encripted Text :", encripted, end='\n\n')
	elif option == '2':
		decripted = decript(string, key)
		print("Decripted Text :", decripted, end='\n\n')
	else:
		print("Enter valid option")
