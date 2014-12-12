from django.db import models
from gvg_pack_est import hs_pack_sim

class Estimator(models.Model):
	# n_trials = models.IntegerField(max_length = 3, default = 1)
	# n_comm_excl = models.IntegerField(max_length = 2, default = 0)
	# n_rare_excl = models.IntegerField(max_length = 2, default = 0)
	# n_epic_excl = models.IntegerField(max_length = 2, default = 0)
	# n_leg_excl = models.IntegerField(max_length = 2, default = 0)
	# n_trials, n_comm_excl, n_rare_excl, n_epic_excl, n_leg_excl = 1, 10, 10, 10, 10
	# no_collect = [n_comm_excl, n_rare_excl, n_epic_excl, n_leg_excl]
	current_card_dict = {}

	def make_estimate(self):
		base_collection = hs_pack_sim.Collection(self.current_card_dict)
		no_collect_pct = [x/y for x,y in zip(self.no_collect, base_collection.n_list)]
		simulation = hs_pack_sim.replicate_buy_complete_set(self.n_trials, pct_bad_cards = no_collect_pct)
		mu = hs_pack_sim.mean(simulation)
		maxi = max(simulation)
		mini = min(simulation)
		return([mu, maxi, mini])


	# def __init__(self):
	# 	base_collection = hs_pack_sim.Collection(self.current_card_dict)
	# 	self.no_collect_pct = [x/y for x,y in zip(self.no_collect, base_collection.n_list)]
	# 	simulation = hs_pack_sim.replicate_buy_complete_set(self.n_trials, pct_bad_cards = self.no_collect_pct)
	# 	self.mu = hs_pack_sim.mean(simulation)
	# 	self.maxi = max(simulation)
	# 	self.mini = min(simulation)

	def __str__(self):
		return(self.name)
