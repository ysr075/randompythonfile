
from time import sleep

def timer():
	sleep(1)

def strAttr():
	x = str(5)
	for i in range(3):
		timer()
		print(x.split())

def main():
	strAttr()

main()
