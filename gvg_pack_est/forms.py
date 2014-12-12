from django import forms
from gvg_pack_est.models import Estimator

class EstimatorForm(forms.ModelForm):
	n_trials = forms.IntegerField(initial = 100, help_text = 'The number of times to simulate buying a complete set of GvG')
	n_comm_excl = forms.IntegerField(initial = 0, help_text = 'The number of common cards that you do not want to collect. Set to 0 to collect them all.')
	n_rare_excl = forms.IntegerField(initial = 5, help_text = 'The number of rare cards that you do not want to collect. Set to 0 to collect them all.')
	n_epic_excl = forms.IntegerField(initial = 10, help_text = 'The number of epic cards that you do not want to collect. Set to 0 to collect them all.')
	n_leg_excl = forms.IntegerField(initial = 10, help_text = 'The number of legendary cards that you do not want to collect. Set to 0 to collect them all.')

	class Meta:
		model = Estimator
		fields = ('n_trials', 'n_comm_excl', 'n_rare_excl', 'n_epic_excl', 'n_leg_excl')