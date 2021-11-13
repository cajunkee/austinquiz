print ("Welcome to Austin Trivia! What's your weird ass know about the ATX anyways?!")

playing = input("Do you want to play this game? ")
score = 0

if playing != "yes":
    quit()

answer = input("Where is the Austin City Limits Music Festival Held? ")
if answer.lower() == "zilker park":
    print("BOOYAH! You are right!")
    score += 1
else: print("Good try...but that's not correct! The ACL Fest is held at Zilker Park in South Austin every fall.")    

answer = input("What's the name of the natural spring-fed swimming pool inside that park? ")
if answer.lower() == "barton springs":
    print("Damn! That's an Austinite right there! You got it!")
    score += 1
else: print("No...the right answer is Barton Springs! It's 67 degrees year round and a great place to people watch.")   

answer = input("What's Lady Bird Lake's former name? ")
if answer.lower() == "town lake":
    print("oh yeah! Town Lake it is!! Good job!")
    score += 1
else: print("Wrong. Before it was dedicated to Ladybird it was called TOWN LAKE by pretty much everyone. ")   

answer = input("Who was the famous cross dressing South Austinite that once ran for mayor and often wore thongs as shorts? ")
if answer.lower() == "leslie":
    print("You are right! ")
    score += 1
else: print("Incorrect! Leslie is the iconic South Austin personality that will live in the hearts and memories of everyone blessed to have known him")   

answer = input("What is the now Amazon-owned natural grocer chain that was hatched in Austin? ")
if answer.lower() == "whole foods":
    print("yes indeed. right again!")
    score += 1
else: print("Wrong, but good try. Whole Foods is the answer. It started out as a super simple concept with just a few employees. ")   

answer = input("What Austin band blew our minds with the electronic sounds in the song Sad Sad City? ")
if answer.lower() == "ghostland observatory":
    print("you know your shit, yes you do! RIGHT!")
    score += 1
else: print("No, but Ghostland Observatory is the answer! ")   

answer = input("What now-extinct south Austin video store made an appearance on Jimmy Kimmel during SXSW? ")
if answer.lower() == "vulcan video":
    print("ohhh yeahhh!! Do the cabbage patch! That's right!")
    score += 1
else: print("Incorrect. It was Vulcan Video on Elizabeth Street that was the object of a Kimmel skit. They went on to get lots of attention before relocating and eventually closing down permanently.")   

answer = input("What 24 hour diner sits on south Congress and famously operated 8 days/week? ")
if answer.lower() == "magnolia cafe":
    print("everybody knows, everybody goes! YES!!")
    score += 1
else: print("Wrong! Magnolia Cafe is the right answer. There's only one location on South Congress, but before Covid they had another awesome location on Lake Austin!")   

answer = input("What flying animal lives under the congress avenue bridge? ")
if answer.lower() == "bat":
    print("batshit YESSS")
    score += 1
else: print("nope, wrong anser! It's actually a bat!! Mexican Free Tailed Bats moved to Austin in 1980 following construction of the Congress Avenue bridge and the addition of expansion gaps.")   

print("You got " + str(score) + " correct answers")

if score >= 6:
    print("Looks like you know Austin pretty well!! You big ole' Austinite, you!!")
else: print("Well. Maybe you don't know as much as you thought you did...but hopefully you learned some things today!")