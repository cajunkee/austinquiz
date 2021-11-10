print ("Welcome to this simple Austin Quiz!")

playing = input("Do you want to play? ")
score = 0

if playing != "yes":
    quit()

answer = input("Where is the Austin City Limits Music Festival Held? ")
if answer.lower() == "zilker park":
    print("BOOYAH! You are right!")
    score += 1
else: print("wrrrrooonngggg")    

answer = input("What is the mascot of Austin Community College? ")
if answer.lower() == "river bat":
    print("Damn! That's an Austinite right there! You got it!")
    score += 1
else: print("Try again!!")   

answer = input("What's Lady Bird Lake's former name? ")
if answer.lower() == "town lake":
    print("oh yeah! Town Lake it is!! Good job!")
    score += 1
else: print("wrrrrooonngggg")   

answer = input("Who was the famous cross dressing South Austinite that once ran for mayor and often wore thongs as shorts? ")
if answer.lower() == "leslie":
    print("You are right! ")
    score += 1
else: print("try again!")   

answer = input("What is the now Amazon-owned natural grocer chain that was hatched in Austin? ")
if answer.lower() == "whole foods":
    print("yes indeed. right again!")
    score += 1
else: print("you were wrong this time")   

answer = input("What Austin band blew our minds with the electronic sounds in the song Sad Sad City? ")
if answer.lower() == "ghostland observatory":
    print("you know your shit, yes you do! RIGHT!")
    score += 1
else: print("wrrrrooonngggg")   

answer = input("What now-extinct south Austin video store made an appearance on Jimmy Kimmel during SXSW? ")
if answer.lower() == "vulcan video":
    print("ohhh yeahhh!! ")
    score += 1
else: print("wrong this time!")   

answer = input("What 24 hour diner sits on south Congress and famously operated 8 days/week? ")
if answer.lower() == "magnolia cafe":
    print("everybody knows, everybody goes! YES!!")
    score += 1
else: print("wrong")   

answer = input("What flying animal lives under the congress avenue bridge? ")
if answer.lower() == "bat":
    print("batshit YESSS")
    score += 1
else: print("nope")   

print("You got " + str(score) + " correct answers")