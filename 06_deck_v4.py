'''
Задание-5 “Дурак без козырей”
Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.

Создайте колоду из 52 карт. Перемешайте ее.
Первый игрок берет сверху 6 карт
Второй игрок берет сверху 6 карт.
Игрок-1 ходит:
игрок-1 выкладывает самую маленькую карту по значению
игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
Если игрок-2 не может побить карту, то он проигрывает.
Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
Выведите в консоль максимально наглядную визуализацию данного игрового хода.
'''
# Сюда отправляем решение четвертой задачи с колодой
import random


class Card:
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'
    SPADES = 'spades'
    types_symbols = {'hearts': '\u2661',
                    				 'diamonds': '\u2662',
                     				'clubs': '\u2667',
                     				'spades': '\u2664'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f'{self.value}{Card.types_symbols[self.type]}'

    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.types.index(self.type) > Deck.types.index(other_card.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type


class Deck:
    types = ['spades', 'clubs', 'diamonds', 'hearts']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, num_cards=52):
        self.cards = []
        self.index = 0
        if num_cards == 36:
            self.values = Deck.values[4:]
        for t in Deck.types:
            for v in self.values:
                self.cards.append(Card(v, t))

    def show(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def __repr__(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def draw_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return card

    def __getitem__(self, index):
        return self.cards[index]


deck1 = Deck(num_cards=36)
deck2 = Deck(num_cards=36)
deck1.shuffle()
deck2.shuffle()

print(deck1)
print(deck2)

deck1_counter = 0
deck2_counter = 0

for card1, card2 in zip(deck1, deck2):
    if card1 > card2:
        deck1_counter += 1
    elif card2 > card1:
        deck2_counter += 1

print(f'{deck1_counter}:{deck2_counter}')
 