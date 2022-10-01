import time
import webbrowser
import os

global inp
global out

def check(s):
	n = len(s)
	t = s[n - 2]
	if (t == '1'):
		return
	global inp, out

	t = s[n - 4]
	if (t == '1'):
		inp.append(s)
	
	if (t == '2'):
		out.append(s)

def process(s):
	n = len(s)
	for i in range(n - 4):
		if s[i:i + 5] == '/file':
			ans = "https://cses.fi"
			while s[i] != "\"":
				ans = ans + s[i]
				i += 1

			check(ans)

def access(s):
	webbrowser.open(s)

def down(i):
	global inp, out
	access(inp[i])
	access(out[i])

def createFile(s):
	if (not(os.path.isdir(s))):
		os.mkdir(s)
		print("Create", s, "sucessfully!")

def createTextFile(s):
	if (not(os.path.isdir(s))):
		x = open(s, 'w')
		print("Create", s, "sucessfully!")
		x.close();

def openfile(i):
	
	INPlocation = 'D:/USACO CONVERTER/CSES/test_input.txt'
	OUTlocation = 'D:/USACO CONVERTER/CSES/test_output.txt'

	print("Wating for: 0 ", end = '')
	second = 0
	while not(os.path.exists(INPlocation)):
		second += 1
		print(second, end = ' ')
		time.sleep(1)
		if (second == 10): break

	print()

	print("Wating for: 0 ", end = '')
	second = 0
	while not(os.path.exists(OUTlocation)):
		second += 1
		print(second, end = ' ')
		time.sleep(1)
		if (second == 10): break

	print()
	inpfile = open(INPlocation, 'r')
	outfile = open(OUTlocation, 'r')

	s = 'D:/USACO CONVERTER/CSES_download'
	createFile(s)

	number = str(i)
	location = s + '/' + number
	createTextFile(location + '.in')
	createTextFile(location + '.out')

	with open(location + '.in', 'w') as a:
		a.write(inpfile.read())
		a.close
	with open(location + '.out', 'w') as a:
		a.write(outfile.read())
		a.close


	inpfile.close()
	outfile.close()

	os.remove('D:/USACO CONVERTER/CSES/test_input.txt')
	os.remove('D:/USACO CONVERTER/CSES/test_output.txt')

def main():
	global inp, out
	inp = []
	out = []

	with open('D:/text.txt', 'r') as x:
		for line in x:
			process(line)

	n = len(inp)
	for i in range(n):
		down(i)
		openfile(i)
main()
