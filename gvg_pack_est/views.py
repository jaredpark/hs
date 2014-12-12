from django.shortcuts import render
from django.http import HttpResponse
from gvg_pack_est.models import Estimator
from gvg_pack_est.forms import EstimatorForm

def test_page(request):
	cont_dict = {
		'test_key': 'Test text'
	}
	return(render(request, 'gvg_pack_est/test_page.html', cont_dict))

def estimate(request):
	Sim = Estimator()
	Sim.no_collect = [request.POST.get('n_comm_excl'), request.POST.get('n_rare_excl'), request.POST.get('n_epic_excl'), request.POST.get('n_leg_excl')]
	for i in range(len(Sim.no_collect)):
		if Sim.no_collect[i] == '':
			Sim.no_collect[i] = 0
	Sim.no_collect = [int(float(x)) for x in Sim.no_collect]
	Sim.n_trials = request.POST.get('n_trials')
	if Sim.n_trials == '':
		Sim.n_trials = '1'
	Sim.n_trials = int(float(Sim.n_trials))
	results = Sim.make_estimate()

	cont_dict = {
		'average': round(results[0]),
		'maximum': results[1],
		'minimum': results[2],
	}
	return(render(request, 'gvg_pack_est/estimate.html', cont_dict))

def index(request):
	if request.method == 'POST':
		form = EstimatorForm(request.POST)

    	# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.

			# form.save(commit=True)
			n_trials = form.cleaned_data['n_trials']
			n_comm_excl = form.cleaned_data['n_comm_excl']
			n_rare_excl = form.cleaned_data['n_rare_excl']
			n_epic_excl = form.cleaned_data['n_epic_excl']
			n_leg_excl = form.cleaned_data['n_leg_excl']
			# return(HttpResponse, n_trials)

			# Now call the index() view.
			# The user will be shown the homepage.
			return(estimate(request))
		else:
			# The supplied form contained errors - just print them to the terminal.
			print(form.errors)
	else:
		# If the request was not a POST, display the form to enter details.
		form = EstimatorForm()

	cont_dict  = {
		'form': form,
	}
	return(render(request, 'gvg_pack_est/index.html', cont_dict))
	
