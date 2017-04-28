import json, sys
import django.forms
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from configurator.apps.resource.forms import ResourceFormSet, StringResourceForm, UploadFileForm
from configurator.apps.resource.models import *


def get_resource_form(model_name):
    model = getattr(sys.modules[__name__], model_name)
    model_form = modelform_factory(model, 
        fields = ('name', 'description','value',), 
        widgets = {'name': django.forms.HiddenInput(),'description': django.forms.HiddenInput()})
    return model_form
        
def configured(request):
    keys = request.POST['keys'].split(',')
    forms = []
    for k in keys:
        prf, model_name = k.split(':')
        model = getattr(sys.modules[__name__], model_name)
        model_form = modelform_factory(model, 
            fields = ('name', 'description','value',), 
            widgets = {'name': django.forms.HiddenInput(),'description': django.forms.HiddenInput()})
        forms.append(model_form(request.POST, prefix=prf))

    for f in forms:
        if f.is_valid():
            f.save()

    print(forms)

    return render(request, 'done.html')

def forms(request):
    file = request.FILES['file']
    data = json.loads(file.read().decode("utf-8"))
    required = data['requires']
    forms = []
    for resource in required:
        form_dict = {}
        # form_dict['form'] = required[resource]['type'].title()+'ResourceForm'
        form_dict['name'] = resource
        form_dict['description'] = required[resource]['description']
        forms.append(form_dict)
    print(forms)
    resource_forms = []
    req = []
    for f in forms:
        model_name = required[f['name']]['type'].title()+'Resource'
        model = getattr(sys.modules[__name__], model_name)
        model_form = modelform_factory(model, 
            fields = ('name', 'description','value',), 
            widgets = {'name': django.forms.HiddenInput(),'description': django.forms.HiddenInput()})
        prf = '{}:{}'.format(f['name'], model_name)
        req.append(prf)
        res_form = model_form(initial=f, prefix=f['name'])
        resource_forms.append(res_form)

    # name = required['title']['type'].title()+'ResourceForm'
    
    print(req)
    formset = ResourceFormSet(queryset=Resource.objects.none())

    # form = resource_forms[0](initial=forms[0])
    return render(request, 'main.html', {'forms': resource_forms, 'req' : ','.join(req)})

def index(request):
    form = UploadFileForm()
    if request.method == "POST":
        return forms(request)
    return render(request, 'index.html', {'form': form})