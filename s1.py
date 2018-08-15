import random
colors={
    1:"red",
    2:"blue",
    3:"green",
    4:"yellow",
    5:"white"
}
initials = []
while len(initials)<4:
    rand_num = random.randint(1,5)
    if rand_num not in initials:
        initials.append(rand_num)

initials = [colors[item] for item in initials]


win = False
for turn in range(len(initials)):
    guess = input()
    guess = guess.split(",")
    black = 0
    white = 0
    for i in range(len(guess)):
        if guess[i] == initials[i]:
            black +=1
        elif guess[i] in initials:
            white +=1
    print("black:{} , whilte:{}".format(black,white))
    if black == 4:
        print("You Win!!")
        win = True
if not win:
    initialstate = ",".join(initials)
    print("You loose the initial state was: {}".format(initialstate))