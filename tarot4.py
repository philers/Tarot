import random, json

#Get card data from json file and build dictionary, with short name as key
with open('card_data.json') as card_data:
	card_data_fulldict = json.load(card_data)
card_data_dict = {}
for i in range(0, 78):
	card_data_dict[card_data_fulldict['cards'][i]['name_short']] = card_data_fulldict['cards'][i]

threec_spread_dict = {
	'Generic Three Card': ['Card1', 'Card2', 'Card3'],
    'Time': ['Past', 'Present', 'Future'],
    'Path' : ['You', 'Path', 'Potential'],
    'Relationship' : ['You', 'Relationship', 'Partner'],
    'Decision': ['Situation', 'Action', 'Outcome']}

#Define the class, Deck, which is holds all of the cards.
class Deck():

	def __init__(self):
		self.cards = []
		self.spread_list = []

	def build_deck(self):
		self.cards = list(card_data_dict.keys())
		return self.cards

	def shuffle_deck(self):
		random.shuffle(self.cards)
		return self.cards

	def build_spreads(self):
		for spread in threec_spread_dict:
			spread = Spread(3, spread, threec_spread_dict[spread], self)
			self.spread_list.append(spread)
		return self.spread_list

	def what_spreads(self):
		print(self.spread_list)

	def layout_spread(self, spread_int, user_learn_choice = "Y", user_see_choice = "N"):
		self.shuffle_deck()
		self.spread_list[spread_int].pull_cards()
		self.spread_list[spread_int].layout_cards()
		if user_learn_choice == "Y":
			self.spread_list[spread_int].learn_meaning()
		if user_see_choice == "Y":
			self.spread_list[spread_int].see_cards()

#Use the card dictionary to look up meanings or descriptions
class Card():

	def __init__(self, short_name="",  value_int=0, reverse=False):
		self.short_name = short_name
		self.value_int = value_int
		self.reversed = reverse
		self.name = ""

	def lookup_info(self):
		self.name = card_data_dict[self.short_name]['name']
		self.value_int = card_data_dict[self.short_name]['value_int']
		self.meaning_up = card_data_dict[self.short_name]['meaning_up']
		self.meaning_rev = card_data_dict[self.short_name]['meaning_rev']
		self.description = card_data_dict[self.short_name]['desc']

	def find_description(self):
		return self.description

	def __repr__(self):
		return self.name

#Build spreads where you lay out your cards with different meanings
class Spread():

	def __init__(self, number_of_cards, theme="", pattern=[], deck=[]):
		self.number_of_cards = number_of_cards
		self.theme = theme
		self.pattern = pattern
		self.deck = deck
		self.pull = []
		self.pull_dic = {}
		self.pull_names = []

	def pull_cards(self):
		self.pull = self.deck.cards[:self.number_of_cards]
		for card in self.pull:
			self.pull_dic[card] = Card(card.lower())
			self.pull_dic[card].lookup_info()
		for card in self.pull:
			self.pull_names.append(self.pull_dic[card].name)
		for value in self.pull_dic.values():
			reverse_int = random.randint(0,1)
			if reverse_int == 0:
				value.reversed = False
			else:
				value.reversed = True
		return self.pull_dic

	def layout_cards(self):
		reading = "Your {a} is {n}, {position}"
		for card, i in zip(self.pull, range(0, 3)):
			if self.pull_dic[card].reversed == False:
				print(reading.format(a=self.pattern[i], n=self.pull_names[i], position="upright"))
			else:
				print(reading.format(a=self.pattern[i], n=self.pull_names[i], position="reversed"))

	def learn_meaning(self):
		meaning = "\n {n} {position} represents {m}"
		for card in self.pull:
			if self.pull_dic[card].reversed == False:
 				print(meaning.format(n=self.pull_dic[card].name, position="upright", m=self.pull_dic[card].meaning_up))
			else:
			 	print(meaning.format(n=self.pull_dic[card].name, position="reversed", m=self.pull_dic[card].meaning_rev))

	def see_cards(self):
		description_message = "\n On this card, you will see {desc}"
		for card in self.pull:
			print(description_message.format(desc=self.pull_dic[card].description))

	def __repr__(self):
		return self.theme

def main():
	deck1 = Deck()
	deck1.build_deck()
	deck1.shuffle_deck()
	deck1.build_spreads()
	deck1.what_spreads()
	user_spread_choice = int(input(" \n Pick a theme from the list to learn from the cards... \n \n Choose a number:"))
	user_learn_choice = str(input("Would you like to learn the meaning of your cards? Y/N:"))
	user_see_choice = str(input("Would you like to 'see' your cards with a description? Warning: these can be quite long Y/N:"))
	deck1.layout_spread((user_spread_choice - 1), user_learn_choice, user_see_choice)
	return deck1

if __name__ == "__main__":
	main()
