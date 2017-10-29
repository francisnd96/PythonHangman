givenWord = input("Write the Hangman Game Word (all caps please): ")
listShownWord = ["_"] * len(givenWord)

sInput = ""

noGuesses = 10
letterNo = 0
noCorrectGuesses = 0

print ("\nWelcome to console hangman!! You have 10 Guesses \nType END to leave at any moment \n")

while(sInput != "END" and noGuesses != 0):
	print ("The word you're looking for is: " + str(listShownWord) + "\n")
	print ("You have: " +  str(noGuesses) + " guesses left")
	sInput = input("Enter a capital letter please: ")
	
	while(letterNo < len(givenWord)):
		if(givenWord[letterNo] == sInput):
			listShownWord[letterNo] = sInput
			noCorrectGuesses += 1
		letterNo += 1
		
	noGuesses -= 1
	letterNo = 0
	
	if(noCorrectGuesses == len(givenWord)):
		print ("Winner Winner!!")
		break
	
	if(noGuesses == 0):
		print ("You're out of guesses. Game Over")