import random
tvjokes = [
   "I think you're a drama queen that's why you always want to enter TV Lounge",
   "You watch tom n jerry on your TV? No wonder why everyone call youa kid",
   "I hope you don't get scolded by mom for watching too much TV"
]
computerjokes = [
   "I am also addicted to GTA V, no wonder it's so fun",
   "Oh kiddo you also a coder like me? no wonder why you got hairfall",
   "A typical youtube addiction",
]
stairjokes = [
   "Your mom again asked you to climb the stairs to open water tank while you were watching Money Heist in your room",
   "Oh you have to climb stairs to get to store room. Bad choice",
   "You have to climb stairs to get to your room after tired day, poor soul",
]
housejokes = [
   "Poor you have to go to groceries instead of playing PUBG",
   "I understand you get signal problems inside house, but house is comfort",
   "Ahh you had to go to neighbours house for a stupid tool, but you don't wanna, I feel you",
]
print("Welcome To The Adventure Champ. Get More Than 70% To Win.")
a = input("What's Your Name? ")
print(f"Good Luck {a}")
g = 0
h = 0
i = 0
j = 0
k = 0
health = 100
for i in range (0,4):
 b = input("In which direction you wanna move: South, East, West, North: ")
 if b.lower() == "south":
    c = input("You Entered TV Lounge. Select one thing. TV, Watch, Chair : ")
    h+=1
    if c.lower() == "tv" or "watch" or "chair":
        if c.lower() == "tv":
           print("You did it perfect")
           g+=10
        elif c.lower() == "watch":
           print("Nice")
           g+=5
        elif c.lower() == "chair":
           print("Alas")
           g+=0
           health-=25
 elif b.lower() == "east":
    d = input("You Entered Computer Room. Select one thing. Charger, Powerbank, Computer : ")
    i+=1
    if d.lower() == "charger" or "powerbank" or "computer":
        if d.lower() == "computer":
           print("You did it perfect")
           g+=10
        elif d.lower() == "powerbank":
           print("Nice")
           g+=5
        elif d.lower() == "charger":
           print("Alas")
           g+=0
           health-=25
 elif b.lower() == "west":
    e = input("You Climbed Stairs. Select one thing. Stone, Trash, Lizard : ")
    j+=1
    if e.lower() == "trash" or "lizard" or "stone":
        if e.lower() == "stone":
           print("You did it perfect")
           g+=10
        elif e.lower() == "trash":
           print("Nice")
           g+=5
        elif e.lower() == "lizard":
           print("Alas")
           g+=0
           health-=25
    if health<30:
      print("You Died")
      break
 elif b.lower() == "north":
    f = input("You Exited House. Do you want to enter house again. Yes or No? ")
    k+=1
    if f.lower() == "yes":
        print("You did it perfect")
        g+=10
    else:
       print("I understand you're getting scolded for not studying, but leaving house is not a good option")
       health-=25
       break
    if health<30:
      print("You Died")
      break
if g>=28:
   print("Congartulations Champ You Won")
   print(f"Your Total Score Is {g}")
   print(f"Your Health Is {health}")
   if h >= 2:
      print(random.choice(tvjokes))
   elif i >= 2:
      print(random.choice(computerjokes))
   elif j >= 2:
      print(random.choice(stairjokes))
   elif k >= 2:
      print(random.choice(stairjokes))
   else:
      print("You're just perfect, buddy")
elif g<28:
   print("Try Again Later")
   print(f"Your Total Score Is {g}")
   print(f"Your Health Is {health}")
GameCredit = "Credit : Game Built By Abu Huraira, In 2 Hours"
print(GameCredit)                                     