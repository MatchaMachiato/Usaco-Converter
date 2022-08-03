import time
import webbrowser
import os

global inp
global out

def get(s, l, r):
	ans = ""
	while l <= r:
		ans = ans + s[l]
		l += 1
	
	return ans;

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
	for i in range(n):
		if i + 4 < n:
			if get(s, i, i + 4) == '/file':
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
		print("Create " + s + " sucessfully!")

def createTextFile(s):
	if (not(os.path.isdir(s))):
		x = open(s, 'w')
		print("Create " + s + " sucessfully!")
		x.close();

def openfile(i):
	
	inpfile = open('D:/USACO CONVERTER/CSES/test_input.txt', 'r')
	outfile = open('D:/USACO CONVERTER/CSES/test_output.txt', 'r')

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

	# sleep(1)
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
		time.sleep(2)
		openfile(i)
main()
