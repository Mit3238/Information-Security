def encript(string, key):
	string = string.replace(' ', '').lower()
	li = []
	for i in range(key):
		li.append([string[i]])

	plus = True
	n = key - 1
	for i in range(key, len(string)):
		if plus == True:
			n += 1
		else:
			n -= 1
		if n >= key:
			plus = False
			n -= 2
		if n < 0:
			plus = True
			n += 2

		li[n].append(string[i])

	ans = ''
	for i in range(key):
		for j in range(len(li[i])):
			ans += li[i][j]
	return ans


def decript(string, key):
    string = string.replace(' ', '').lower()
    fence = [[] for i in range(key)]
    rail  = 0
    var   = 1

    for char in string:
        fence[rail].append(char)
        rail += var

        if rail == key-1 or rail == 0:
            var = -var

    rFence = [[] for i in range(key)]

    i = 0
    l = len(string)
    string = list(string)
    for r in fence:
        for j in range(len(r)):
            rFence[i].append(string[0])
            string.remove(string[0])
        i += 1

    rail = 0
    var  = 1
    r = ''
    for i in range(l):
        r += rFence[rail][0]
        rFence[rail].remove(rFence[rail][0])
        rail += var

        if rail == key-1 or rail == 0:
            var = -var

    return r


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
 
