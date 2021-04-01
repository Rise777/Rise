'''
	Задание-5 “Дурак без козырей”
	Теперь немного сложнее:
		создадим имитацию одного хода в “Дурака без козырей”.

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
    """Класс создаёт игральную карту"""
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'
    SPADES = 'spades'
    types_symbols = {'hearts': '\u2661',
                     'diamonds': '\u2662',
                     'clubs': '\u2667',
                     'spades': '\u2664'}

    def __init__(self, value, type):
        """Блок инициализации - создания экземпляра
         класса class = Class(x, y)"""
        self.value = value
        self.type = type

    def __repr__(self):
        """Блок вывода экземпляра' класса print(Class)"""
        return f'{self.value}{Card.types_symbols[self.type]}'

    def __gt__(self, other_card):
        """Блок проверки экземпляров классов 
        на >, <, >=, <=, !=  class1 > class2"""
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.types.index(self.type) > Deck.types.index(other_card.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other):
        """Блок проверки экземпляров классов 
        на равенство class1 == class2 """
        return self.value == other.value and self.type == other.type

    def eq_types(self, other):
        """Блок проверки экземпляров классов
        на равенство типов class1.type == class2.type """
        return self.type == other.type

class Deck:
    """Класс для создания колоду карт. По умолчанию 52
    По старшинству: черви, бубны, трефы, пики"""
    types = ['spades', 'clubs', 'diamonds', 'hearts']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, num_cards=52):
        """Блок инициализации - создания экземпляра
         класса class = Class(x, y)"""
        self.cards = []
        self.index = 0
        if num_cards == 36:
            self.values = Deck.values[4:]
        for type in Deck.types:
            for value in self.values:
                self.cards.append(Card(value, type))

    def __repr__(self):
        """Блок вывода экземпляра' класса print(Class)"""
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def draw(self, take_card):
        """Блок удаления заданного количества карт из колоды.
        Принимает количество удаляемых карт с верха колоды
        (с конца списка) и возвращает список удалённых карт  """
        cards = []
        for _ in range(take_card):
            cards.append(self.cards.pop(0))
        return cards

    def draw_card(self):
        """Блок удаления одной карты.
        Возвращает удалённую карту"""
        return self.cards.pop(0)
        
    def del_card(self, card):    	
    	del_card_index = self.index(card)
    	self.pop(del_card_index)
    	return self
    			
    def shuffle(self):
        """Блок перемешивания колоды карт"""
        random.shuffle(self.cards)

    def __iter__(self):
        """Блок делает экземпляр класса итерируемым,
        исчисляемым. for deck in decks"""
        self.index = 0
        return self

    def __next__(self):
        """Блок позволяет запрашивать следующий
         элемент экземпляра класса при итерировании"""
        try:
            card = self.cards[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return card

    def __getitem__(self, index):
        """Блок возвращает элемент экземпляра класса"""
        return self.cards[index]

##############################################################
# Создаём 2 колоды и перемешиваем их
# deck1 = Deck(num_cards=36)
# deck2 = Deck(num_cards=36)
# deck1.shuffle()
# deck2.shuffle()
#
# print(deck1)
# print(deck2)
#
# # Выставляем счётчики по нулям
# deck1_counter = 0
# deck2_counter = 0
#
# # Перебераем сразу в двух колодах
# for card1, card2 in zip(deck1, deck2):
#     if card1 > card2:
#         deck1_counter += 1
#     elif card2 > card1:
#         deck2_counter += 1
#
# print(f'{deck1_counter}:{deck2_counter}')
##############################################################

deck = Deck()
print("Колода создана: ", deck)
deck.shuffle()
print("Колода перемешана: ", deck)

player_1 = []
player_2 = []
table = {"player_1" : Deck(),
			 "player_2" : Deck()}
			 


player_1 = deck.draw(6)
player_2 = deck.draw(6)

player_1.sort()
player_2.sort()

print(f"Карты игрока 1: {player_1}")
print(f"Карты игрока 2: {player_2}")
#print(player_1[0])
#print(player_1[1])

# if player_1[0] > player_1[1]:
#     print("Bigest 1: ", player_1[0])
# if player_1[0] < player_1[1]:
#     print("Bigest 2: ", player_1[0])

def del_card (player_cards: list, card) -> list:
    del_card_index = player_cards.index(card)
    del_card = player_cards.pop(del_card_index)
    
    return player_cards, del_card


min_card = player_1[0]

for card in player_1:
    if card < min_card:
        min_card = card

print("Ход игрока 1 минимальной картой: ", min_card)

player_1, table["player_1"] = del_card(player_1, min_card)

print("Колода игрока 1: ", player_1)

biger_card = None

for card in player_2:
    if card > min_card:
        if card.eq_types(min_card):
            biger_card = card
            break

if biger_card is None:
	print("Игрок 2 проиграл")

player_2, table["player_2"] = del_card(player_2, biger_card)
			
print("Ход игрока 2 большей картой: ", biger_card)
print("Колода игрока 2: ", player_2)

#table["player_1"].append(player_1[0])

print(type(table))
print(type(table["player_1"]))
print(type(player_1[0]))
