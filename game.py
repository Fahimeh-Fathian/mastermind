import random

from consts import *


class Game(object):
    length = GAME_LENGTH

    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.initial_state = self.new_game();
        self.turns = 0
        self.max_turns = MAX_TURNS
        self.is_won = False
        self.is_ended = False

    def new_game(self):
        initials = []
        while len(initials) < self.length:
            rand_num = random.randint(MIN_COLOR, MAX_COLOR)
            if rand_num not in initials:
                initials.append(rand_num)

        initials = [COLORS[item] for item in initials]
        return initials

    def turn(self):
        if self.is_ended:
            print("Game Over!")
            return

        guess = input()
        guess = guess.split(",")
        black = 0
        white = 0
        for i in range(self.length):
            if guess[i] == self.initial_state[i]:
                black += 1
            elif guess[i] in self.initial_state:
                white += 1
        print("black:{} , white:{}".format(black, white))
        self.turns += 1
        self.check_state(black)

    def to_str(self):
        return ",".join(self.initial_state)

    def check_state(self, black):
        if self.check_win(black):
            print("You Win!!")
            self.end()
        elif self.check_loose():
            print("You loose the initial state was: {}".format(self.to_str()))
            self.end()
        
    def check_win(self, black):
        return black == self.length

    def check_loose(self):
        return (self.turns == MAX_TURNS)

    def end(self):
        self.is_ended = True


game = Game()
for i in range(MAX_TURNS):
    game.turn()
