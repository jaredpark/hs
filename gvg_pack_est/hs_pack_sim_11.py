# exec(open("C:\\Python34\\Scripts\\hs\\gvg_pack_est\\scripts\\hs_pack_sim.py").read())

import random

def roll_for_gold(opened_pack):
	for card in range(len(opened_pack)):
		if opened_pack[card] == 0:
			gold_list = [0] * 49 + [4]
		elif opened_pack[card] == 1:
			gold_list = [0] * 19 + [4]
		elif opened_pack[card] == 2:
			gold_list = [0] * 14 + [4]
		elif opened_pack[card] == 3:
			gold_list = [0] * 9 + [4]
		upgrade_amount = random.choice(gold_list)
		opened_pack[card] += upgrade_amount
	return(opened_pack)

def open_pack():
	"""

	"""
	opened_pack = []
	card_level = -1
	upgrade = 1
	
	for card in range(5):
	
		while upgrade == 1 and card_level < 3:
			upgrade = random.choice([0,0,0,0,1])
			card_level += 1
	
		opened_pack.append(card_level)
		card_level = -1
		upgrade = 1
	
	if opened_pack.count(0) == 5:
	
		card_level = 0
		upgrade = 1
	
		while upgrade == 1 and card_level < 3:
			upgrade = random.choice([0,0,0,0,1])
			card_level += 1
	
		opened_pack[-1] = card_level

	opened_pack = roll_for_gold(opened_pack)
	return(opened_pack)

def pack_to_cards(opened_pack, n_common = 40, n_rare = 37, n_epic = 26, n_legendary = 20):
	card_list = []
	for i in range(len(opened_pack)):
		card_level = opened_pack[i]
		if card_level == 0:
			card = random.choice(range(1, 1 + n_common))
		elif card_level == 1:
			card = random.choice(range(1 + n_common, 1 + n_common + n_rare))
		elif card_level == 2:
			card = random.choice(range(1 + n_common + n_rare, 1 + n_common + n_rare + n_epic))
		elif card_level == 3:
			card = random.choice(range(1 + n_common + n_rare + n_epic, 1 + n_common + n_rare + n_epic + n_legendary))
		else:
			# golden common = card num 124, golden rare = card num 125, etc (with 123 cards in the set)
			# card identity unimportant b/c all golds are auto-disenchanted for our purposes
			card = card_level + n_common + n_rare + n_epic + n_legendary - 3
		card_list.append(card)
	# print(card_list)
	return(card_list)

class Collection(object):

	n_list = [40, 37, 26, 20]
	n_common = n_list[0]
	n_rare = n_list[1]
	n_epic = n_list[2]
	n_leg = n_list[3]
	n_total = sum(n_list)
	dust_value = {'comm': 5, 'rare': 20, 'epic': 100, 'leg': 400, 'g_comm': 50, 'g_rare': 100, 'g_epic': 400, 'g_leg': 1600}
	dust_cost = {'comm': 50, 'rare': 100, 'epic': 400, 'leg': 1600}
	complete_set_dust_cost = n_common * 2 * dust_cost['comm'] + n_rare * 2 * dust_cost['rare'] + n_epic * 2 * dust_cost['epic'] + n_leg * 2 * dust_cost['leg']
	full_collection = {}
	for card in range(1, n_total + 1):
		if card < n_total - n_leg + 1:
			full_collection[card] = 2
		else:
			full_collection[card] = 1

	def __init__(self, all_cards, pct_bad_cards = [0,0,0,0], dust = 0):
		self.all_cards = all_cards
		self.dust = dust
#		self.opened_by_type = {'comm': 0, 'rare': 0, 'epic': 0, 'leg': 0, 'g_comm': 0, 'g_rare': 0, 'g_epic': 0, 'g_leg': 0}
		self.opened_by_type = [0] * 8
		self.bad_cards = []
		for rarity in range(len(pct_bad_cards)):
			starting_point = sum(self.n_list[:rarity])
			n_bad = round(pct_bad_cards[rarity] * self.n_list[rarity])
			self.bad_cards.extend(range(1 + starting_point, 1 + starting_point + n_bad))
		self.missing_cards = self.return_missing_cards()

	def print_collection(self):
		print('you have %d cards and %d dust' % (sum(self.all_cards.values()), self.dust))

	def return_card_type(self, card):
		if card in range(1, 1 + self.n_common):
			card_type = [1] + [0] * 7
		elif card in range(1 + self.n_common, 1 + self.n_common + self.n_rare):
			card_type = [0] * 1 + [1] + [0] * 6
		elif card in range(1 + self.n_common + self.n_rare, 1 + self.n_total - self.n_leg):
			card_type = [0] * 2 + [1] + [0] * 5
		elif card in range(1 + self.n_total - self.n_leg, 1 + self.n_total):
			card_type = [0] * 3 + [1] + [0] * 4
		elif card == self.n_total + 1:
			card_type = [0] * 4 + [1] + [0] * 3
		elif card == self.n_total + 2:
			card_type = [0] * 5 + [1] + [0] * 2
		elif card == self.n_total + 3:
			card_type = [0] * 6 + [1] + [0] * 1
		elif card == self.n_total + 4:
			card_type = [0] * 7 + [1]
		return(card_type)

	def dust_card(self, card):
		if card in range(1, 1 + self.n_common):
			self.dust += self.dust_value['comm']
		elif card in range(1 + self.n_common, 1 + self.n_common + self.n_rare):
			self.dust += self.dust_value['rare']
		elif card in range(1 + self.n_common + self.n_rare, 1 + self.n_total - self.n_leg):
			self.dust += self.dust_value['epic']
		elif card in range(1 + self.n_total - self.n_leg, 1 + self.n_total):
			self.dust += self.dust_value['leg']
		elif card == self.n_total + 1:
			self.dust += self.dust_value['g_comm']
		elif card == self.n_total + 2:
			self.dust += self.dust_value['g_rare']
		elif card == self.n_total + 3:
			self.dust += self.dust_value['g_epic']
		elif card == self.n_total + 4:
			self.dust += self.dust_value['g_leg']

	def add_pack(self, pack_of_cards):
		for card in pack_of_cards:
			card_type = self.return_card_type(card)
			self.opened_by_type = [x + y for x,y in zip(self.opened_by_type, card_type)]
			if card in range(self.n_total + 1, self.n_total + 5): #is is golden? if so, dust it
				self.dust_card(card)
			elif card in self.bad_cards: #is is a bad card? if so, dust it
				self.dust_card(card)
			else:
				if not card in self.all_cards: # don't have the cards yet?
					self.all_cards[card] = 1 # add it to the collection
					self.missing_cards[card] = self.missing_cards[card] - 1
				else:
					num_of_card = self.all_cards[card]
					if num_of_card == 1: # 
						if card > self.n_total - self.n_leg: # if it's a legendary
							self.dust_card(card) # dust it, can only have one
						else:
							self.all_cards[card] = 2 # else, add it to the collection
							self.missing_cards[card] = self.missing_cards[card] - 1
					else:
						self.dust_card(card)

	def open_packs(self, num = 40):
		#self.print_collection()
		cards_start = self.all_cards
		dust_start = self.dust
		for pack in range(num):
			self.add_pack(pack_to_cards(open_pack()))
		#self.print_collection()

	def return_missing_cards(self):
		missing_cards = {}
		for card in range(1, self.n_total + 1):
			if card in self.bad_cards:
				pass
			elif card in self.all_cards:
				missing_cards[card] = 2 - self.all_cards[card]
			else:
				missing_cards[card] = 2
		return(missing_cards)

	def craft_missing_cards_cost(self, missing_cards):
		dust_needed = 0
		for card in missing_cards.keys():
			n_missing = missing_cards[card]
			if card in range(1, 1 + self.n_common):
				dust_needed += self.dust_cost['comm'] * n_missing
			elif card in range(1 + self.n_common, 1 + self.n_common + self.n_rare):
				dust_needed += self.dust_cost['rare'] * n_missing
			elif card in range(1 + self.n_common + self.n_rare, 1 + self.n_total - self.n_leg):
				dust_needed += self.dust_cost['epic'] * n_missing
			elif card in range(1 + self.n_total - self.n_leg, 1 + self.n_total):
				dust_needed += self.dust_cost['leg'] * n_missing
		return(dust_needed)

	def buy_complete_set(self, spend_dust = True): #around 900 packs and 80k spare dust, but why?
		n = 0
		while sum(self.all_cards.values()) < self.n_total * 2 - self.n_leg:
			n += 1
			self.open_packs(1)
			if spend_dust:
				if self.craft_missing_cards_cost(self.missing_cards) <= self.dust:
					self.dust = self.dust - self.craft_missing_cards_cost(self.missing_cards)
					self.missing_cards = {}
					self.all_cards = self.full_collection
			# if n % 100 == 0:
				# print(self.craft_missing_cards_cost(self.missing_cards), self.dust)
		return(n)
					
		print('You opened %d packs to get a complete set' % (n))


def replicate_buy_complete_set(n, pct_bad_cards = [0,0,0,0]):
	n_packs_list = []
	for i in range(n):
		# print(i)
		n_packs_list.append(Collection({}, pct_bad_cards = pct_bad_cards).buy_complete_set())
	return(n_packs_list)

def mean(list):
	return(sum(list)/len(list))

pct_bad = [.1,.1,.5,.5]
trial = replicate_buy_complete_set(100, pct_bad_cards = pct_bad)
print([mean(trial), max(trial), min(trial)])

# n_list = [40, 37, 26, 20]
# n_opened = [0]*8
# for i in range(1000000):
# 	pack = open_pack()
# 	for card in pack:
# 		n_opened[card] += 1

# n_opened
# [round(x/sum(n_opened),5) for x in n_opened]
# [0.72011, 0.20162, 0.03951, 0.00956, 0.01465, 0.01067, 0.00283, 0.00104]
