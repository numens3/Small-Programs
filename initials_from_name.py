# This Program takes your name and converts it into your intials :D

name = input('Please enter your name: ')

def initials(name):
	FirstAndLastname = name.split()
	print(FirstAndLastname[0][0],'.',FirstAndLastname[1][0])

initials(name)