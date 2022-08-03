import os
global location
# = 'D:/USACO CONVERTER/TESTING'
global problemName
# = 'TEST'
global destinationFile
global numTest

def process(source, name):
	global destinationFile, problemName
	s = str(name)

	a, b = s.split('.')


	nameTest = 'TEST' + a
	destination = destinationFile + '/' + problemName + '/' + nameTest
	if not(os.path.isdir(destination)):
		os.mkdir(destination)
		print("creat " + destination + " sucessfully")

	if b == 'in':
		b = b + 'p'

	s = problemName + '.' + b
	with open(destination + '/' + s, 'w') as file:
		with open(source, 'r') as ori:
			file.write(ori.read())


def creatMainFolder():
	global destinationFile
	destination = destinationFile + '/' + problemName
	if not(os.path.isdir(destination)):
		os.mkdir(destination)
		print("creat " + destination + " sucessfully")

def main():
	global location
	for name in os.listdir(location):
		f = os.path.join(location, name)

		if os.path.isfile(f): 
			process(f, name)

	print("Convert sucessfully!")

def fix(s):
	ans = ''
	for ch in s:
		if ch == '\\':
			ans = ans + '/'
		else:
			ans = ans + ch

	return ans

def takeInfo():
	global location, problemName, destinationFile
	problemName = input("Problem name: ")
	location = fix(input("Location of file want to convert: "))
	destinationFile = fix(input("Destination of the converted file: "))

takeInfo()
creatMainFolder()
main()
