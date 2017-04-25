from django.shortcuts import render
from configurator.apps.resource.forms import ResourceFormSet
from configurator.apps.resource.models import Resource

def index(request):
	formset = ResourceFormSet(queryset=Resource.objects.all())
	return render(request, 'main.html', {'formset': formset})