import random


POSSIBLE_NUMBERS = range(1, 91)

PLAYER_LOST_TEXT = 'You lost! Try again'


class Card:
    def __init__(self, is_player):
        self.is_player = is_player
        self.rows = 3
        self.numbers_p_row = 5
        self.cells_p_row = 9
        self.pos_n_num = []  # [{0:23, 4:78}, {}..]

    def remove_number(self, n):
        for i in range(len(self.pos_n_num)):
            row = self.pos_n_num[i]
            new_row = row.copy()
            for k, v in row.items():
                if v == n:
                    del new_row[k]
            self.pos_n_num[i] = new_row

    def check_empty(self):
        return len([e for row in self.pos_n_num for e in row.values()]) == 0

    def check_number(self, n):
        # print([e for row in self.pos_n_num for e in row])
        return n in [e for row in self.pos_n_num for e in row.values()]

    def generate_card(self):
        numbers = random.sample(POSSIBLE_NUMBERS, k=self.rows * self.numbers_p_row)
        for i in range(self.rows):
            # reshape numbers
            # i=0 numbers[0:5] == numbers[5*i:5*(i+1)]
            # i=1 numbers[5:10] == numbers[5*i:5*(i+1)]
            # i=2 numbers[10:15] == numbers[5*i:5*(i+1)]
            numbers_in_row = numbers[self.numbers_p_row * i: self.numbers_p_row * (i + 1)]
            # generate random indices / positions
            positions_in_row = random.sample(range(self.cells_p_row), k=self.numbers_p_row)
            positions_in_row.sort()
            # convert numbers and positions into a dict
            self.pos_n_num.append(dict(zip(positions_in_row, numbers_in_row)))

    def display_card(self):
        card_length = self.cells_p_row * self.rows
        print("-------- Your Card --------" if self.is_player else "----- Computer's Card -----")
        # i is for i-th row
        for i in range(self.rows):
            row_to_print = ''
            # j for j-th cell empty or with a number, we'll see
            for j in range(self.cells_p_row):
                if j in self.pos_n_num[i].keys():
                    row_to_print += '{:2d}'.format(self.pos_n_num[i][j]) + ' '
                else:
                    row_to_print += '   '
            print(row_to_print)
        print('-' * card_length)


class Game:
    def __init__(self):
        self.game_on = True
        self.possible_numbers = list(POSSIBLE_NUMBERS)
        self.player_card = Card(True)
        self.computer_card = Card(False)

    def generate_number(self):
        while True:
            l = len(self.possible_numbers)
            if l == 0:
                break
            n = random.sample(range(l), k=1)[0]
            yield self.possible_numbers[n]
            del self.possible_numbers[n]

    def get_n_remain(self):
        return len(self.possible_numbers) - 1

    def remove_number_from_card(self, new_number):
        player_input = input('Remove the number from your card? (y/n)')
        if player_input.lower() == 'n':
            if self.player_card.check_number(new_number):
                print('You missed a number')
                return True
        else:
            if self.player_card.check_number(new_number):
                self.player_card.remove_number(new_number)
            else:
                print("You don't have this number")
                return True

        if self.computer_card.check_number(new_number):
            self.computer_card.remove_number(new_number)

        return False

    def play(self):
        print('\nGame started')

        self.player_card.generate_card()
        self.player_card.display_card()
        self.computer_card.generate_card()
        self.computer_card.display_card()

        for new_number in self.generate_number():
            print('\n\nNew number is', new_number, f'({self.get_n_remain()} remaining)')
            self.player_card.display_card()
            self.computer_card.display_card()

            if self.remove_number_from_card(new_number):
                print(PLAYER_LOST_TEXT)
                break

            if self.player_card.check_empty():
                if self.computer_card.check_empty():
                    print('The draw! Try again')
                    break
                else:
                    print('You won! Congratulations!')
                    break
            elif self.computer_card.check_empty():
                print('Computer won!')
                print(PLAYER_LOST_TEXT)
                break

        print('\nGame is over')


game = Game()
game.play()
