import random

correctNum = 7
running = True

def testNumber(testedNumber, correctNumber):
	if testedNumber == correctNumber:
		return 1
	else:
		return 0

print "Hello Everybody!"

while running:
	choice = input("Please enter a number:")
	answer = testNumber(choice,correctNum)
	if answer == 1:
		print "Correct!"
		running = False
	else:
		print "Sorry, please choose again!"