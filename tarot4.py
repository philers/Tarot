import random, json

#Get card data from json file and build dictionary, with short name as key
with open('card_data.json') as card_data:
	card_data_fulldict = json.load(card_data)
card_data_dict = {}
for i in range(0, 78):
	card_data_dict[card_data_fulldict['cards'][i]['name_short']] = card_data_fulldict['cards'][i]

threec_spread_dict = {
	'Theme': ['Card1', 'Card2', 'Card3'],
    'Time': ['Past', 'Present', 'Future'],
    'Path' : ['You', 'Path', 'Potential'],
    'Relationship' : ['You', 'Relationship', 'Partner'],
    'Decision': ['Situation', 'Action', 'Outcome']}


class Deck():

	def __init__(self):
		self.cards = []

	def build_deck(self):
		self.cards = list(card_data_dict.keys())
		return self.cards

	def shuffle_deck(self):
		random.shuffle(self.cards)
		return self.cards

class Card():

	def __init__(self, short_name="",  value_int=0):
		self.short_name = short_name
		self.value_int = value_int
		self.name = ""

	def lookup_info(self):
		self.name = card_data_dict[self.short_name]['name']
		self.value_int = card_data_dict[self.short_name]['value_int']
		self.meaning_up = card_data_dict[self.short_name]['meaning_up']
		self.meaning_rev = card_data_dict[self.short_name]['meaning_rev']
		self.description = card_data_dict[self.short_name]['desc']

	def __repr__(self):
		return self.name


class Spread():

	def __init__(self, number_of_cards, theme=[], pattern=[], deck=[]):
		self.number_of_cards = number_of_cards
		self.theme = theme
		self.pattern = pattern
		self.fullspread = {}
		self.fullspread[self.theme] = self.pattern
		self.deck = deck
		self.pull = []
		self.pull_dic = {}
		self.pull_names = []

	def pull_cards(self):
		self.pull = self.deck[:self.number_of_cards]
		for card in self.pull:
			self.pull_dic[card] = Card(card.lower())
			self.pull_dic[card].lookup_info()
		for card in self.pull:
			self.pull_names.append(self.pull_dic[card].name)
		return self.pull_dic


	def layout_cards(self):
		self.layout = dict(zip(self.pattern, self.pull))
		reading = "Your {a} is {n}."
		for i in range(0, 3):
			print(reading.format(a=self.pattern[i], n=self.pull_names[i]))
		return self.layout

	def learn_meaning(self):
		meaning = "This card represents {m}"
		for card in self.pull:
 			print(meaning.format(m=self.pull_dic[card].meaning_up))


#Test building a deck
deck2 = Deck()
deck2.build_deck()
deck2.shuffle_deck()


three_card_spread_general = Spread(3, 'Theme', ['Card1', 'Card2', 'Card3'], deck2.cards)
three_card_spread_time = Spread(3, 'Time', ['Past', 'Present', 'Future'], deck2.cards)


three_card_spread_time.pull_cards()
three_card_spread_time.layout_cards()
three_card_spread_time.learn_meaning()
