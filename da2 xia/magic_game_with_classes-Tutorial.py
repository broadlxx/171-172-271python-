""" This is a framework to handle the card game 'Magic' in which the
defender holds a set of N cards, each with a defense value (up to N) and
a value (up to N).

The attacker also hold a set of cards, but these only have an attack
strength (up to N).

All values, attack and defence strengths are chosen randomly, in the range
1...N (including N) and so values may occur more then once.

On each turn, you can pick an attacker's card, and pair it with one of
your cards.
    If your card's defense_strength >= attacker's  strength,
       your card lives, and is moved to the 'alive' pile.
    If your card loses (dies), it's removed from your hand (set of cards).

Your goal is to maximise the SUM OF THE VALUES of your cards that live.

To enable comparisons between different strategies (which needs
evaluations over many rounds to find the average) the play_game() method
returns the fraction of points (i.e. range 0-1) preserved for each game.

written by Giovanni Moretti, March 2017
"""
import random

#=======================================================================

class One_defense_card():
    "Create a class to store a single card, and to display it"
    "Set the initial value and defense strength randomly in range 1..N"
    def __init__(self, N):
        self.value = random.randint(1,N)
        self.defense = random.randint(1, N)

    def __str__(self):
        return '  (value: %3d - defense: %3d)' %(self.value, self.defense)

    def print(self):
        print(self.__str__())

#=======================================================================

class Defence_Cards():
    "A class to handle a set of user's cards for the game 'Magic'"

    def __init__(self, N):
        "Maintain a hand of 'Magic' cards (in a list), and another"
        "list for cards that have played and survived against the attacker."
        self.cards = []
        self.live_cards = []
        for i in range(N):
            self.cards.append(One_defense_card(N))

    def print(self, heading = None):
        'print the hand of cards'
        if heading:
            print(heading)
        for card in self.cards:
            card.print()

    def get_value_limits(self):
        """Returns the two cards that have the highest and lowest values"""
        self.cards.sort(key = lambda card: card.value, reverse = True)   # Sort cards on values
                                                                         # so cards[0] has highest value
        return self.cards[0], self.cards[-1]

    def get_value2_limits(self):
        list2 = []
        """Returns the two cards that have the highest and lowest values"""
        self.cards.sort(key = lambda card: card.value, reverse = True)   # Sort cards on values
        for i in self.cards:                                             # so cards[0] has highest value
            if i == self.cards[-1]:
                list2.append(i)

        list2.sort(key = lambda card: card.defense, reverse=True)
        bestnum = list2[-1]

        return bestnum

    def get_value3_limits(self,list1):
        list1.sort(key = lambda card: card.defense, reverse=True)  # Sort cards on values
        bestnum = list1[-1] # get the max number
        return  bestnum


    def get_defense_limits(self):
        """Returns the two cards that have the highest and lowest defense strengths"""
        self.cards.sort(key = lambda card: card.defense, reverse=True)   # Sort cards on defence strength
                                                             # so cards[0] is greatest strength
        return self.cards[0], self.cards[-1]


    def pick_random_card(self,attack_strength):
        "This chooses a random card but does NOT delete it from 'cards'."
        "If deletion is required, use delete_card(card)."
        list1 = []
        for i in self.cards:
            if i.defense >= attack_strength:
                list1.append(i)
        if len(list1) == 0:
            bestn = self.get_value2_limits()
            return bestn
        else:
            bestn = self.get_value3_limits(list1)
            return bestn

        #return random.choice(self.cards)

    def delete_card(self, card):
        self.cards.remove(card)

    def move_to_live_cards(self, card):
        "Live cards are those that survive an encounter with the enemy"
        self.live_cards.append(card)
        self.delete_card(card)

    def print_live_cards(self, heading = None):
        if heading:
            print(heading)
        for card in self.live_cards:
            card.print()

    def total_value(self):
        "Calculate the total value of my (remaining) cards."
        total = 0
        for card in self.cards:
            total += card.value
        return total

    def live_card_total(self):
        total = 0
        for card in self.live_cards:
            total += card.value
        return total

#=======================================================================

def create_attackers_cards(N):
    """The attackers cards are just a list of the attack strength of each attack"""
    cards = []
    for n in range(N):
        attack_strength = random.randint(1,N)
        cards. append(attack_strength)
    return cards

#=======================================================================
# The main function - it plays a single game and returns the fraction of
# the initial points that have been saved (i.e. are still alive)

def play_game(N, display_cards = True):
    mycards = Defence_Cards(N)
    liveCards = []                    # Cards that survive end up here
    initial_total = mycards.total_value()

    attackers_cards = create_attackers_cards(N)

    if display_cards:
        print("My cards at the start: ")
        mycards.print()
        print("Attacker's cards", attackers_cards)
        print("My cards: total initial value:", initial_total)

    while True:
        if len(attackers_cards) == 0:
            break

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # StraTEGY:  RANDOMLY CHOOSE AN ATTACKER CARD - YOU CAN MODIFY THIS
        attack_strength = random.choice(attackers_cards)
        attackers_cards.remove(attack_strength)        # Remove cards as they're used.
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        if display_cards:
            print("\nAttacker\'s Strength", attack_strength)
            mycards.print(heading="My remaining cards:")

        #*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # STRATEGY:    RANDOMLY CHOOSE DEFENSE CARD - YOU CAN MODIFY THIS
        this_card = mycards.pick_random_card(attack_strength)

        if this_card.defense >= attack_strength:
            print("My card", this_card, "vs. Attacker's:", attack_strength, ">>> My card LIVES")
            mycards.move_to_live_cards(this_card)
        else:
            print("My card", this_card, "vs. Attacker's:", attack_strength, ">>> My card DIES")
            mycards.delete_card(this_card)
        #*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if display_cards:
        mycards.print_live_cards("\nRemaining Live cards")

    final_hand_value = mycards.live_card_total()
    fraction_preserved = final_hand_value/initial_total
    print("Value Preserved in alive cards = %d%%" % (fraction_preserved*100))
    return fraction_preserved

#=======================================================================
# Now run a set of games and report the outcome
N = 10           # No of cards and also max value, defence and attack strengths
no_of_games = 100

total_preserved = 0
for i in range(no_of_games):
    print("\n>>>> ROUND", i+1)
    preserved = play_game(N, display_cards=True)  # %%%%%% set False to hide card details
    total_preserved += preserved

print("\nAverage Value Preserved = %0.1f%%" % (total_preserved / no_of_games * 100))
