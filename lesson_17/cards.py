class Card:
    def __init__(self, name, weight):
        self.name = name
        self.__weight = weight
    @property
    def weight(self):
        return self.__weight

class Deck:
    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        self.__cards.append(card)

    def add_cards(self, *cards):
        [self.add_card(card) for card in cards]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cards:
            return self.__cards.pop(0)
        raise StopIteration

class Player:
    def __init__(self, name):
        self.name = name
        self.deck_in_hand = Deck()
        self.deck_win = Deck()

class Table:
    def __init__(self):
        self.__game = []

    def take_card(self, player, card):
        self.__game.append((player,card))

    def get_card(self, player):
        max = 1
        winner = None
        for val in self.__game:
            if val[1].weight > max:
                max = val[1].weight
                winner = val[0]

        if player is winner:
            return [card for card, _ in self.__game]

        return []
main_deck = Deck()

for i in range(1,53):
    card = Card('', i)
    main_deck.add_card(card)

player_1 = Player('Ivan')
player_2 = Player('Oleg')
player_3 = Player('Alex')
players = [player_1, player_3, player_2]

for index, card in enumerate(main_deck):
    players.deck_in_hand.add_card(card)

