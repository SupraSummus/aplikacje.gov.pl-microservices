import json, sys
import django.forms
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from configurator.apps.resource.forms import UploadFileForm
from configurator.apps.resource.models import *
from configurator.apps.application.models import *

# factory for a modelForm of specific model_name
def get_resource_form(model_name):
    model = getattr(sys.modules[__name__], model_name)
    model_form = modelform_factory(model, 
        fields = ('name', 'description','value',), 
        widgets = {'name': django.forms.HiddenInput(),'description': django.forms.HiddenInput()})
    return model_form
        

# processing submitted form
# TODO check if validation as is is good enough
def configured(request):
    keys = request.POST['keys'].split(',')
    meta = request.POST['meta'].split(',')
    img, app_name = meta[0], meta[1]
    forms = []

    # parse data from forms
    for k in keys:
        prf, model_name = k.split(':')
        model = getattr(sys.modules[__name__], model_name)
        model_form = modelform_factory(model, 
            fields = ('name', 'description','value',), 
            widgets = {'name': django.forms.HiddenInput(),'description': django.forms.HiddenInput()})
        forms.append(model_form(request.POST, prefix=prf))

    #create dict resources for wrapping up parameters
    app_dict = DictResource(name='{} dict'.format(app_name))
    app_dict.save()
    app_resource = AppResource(required_resource=app_dict, image_name=img, name=app_name)
    app_resource.save()

    #create objects from forms
    for f in forms:
        if f.is_valid():
            resource = f.save()
            dict_resource = DictResourceEntry(dictionary=app_dict, value=resource, key=resource.name)
            dict_resource.save()

    return render(request, 'done.html')


# function processing uploaded file
def forms(request):

    # import and read paramteres.json file
    file = request.FILES['file']
    data = json.loads(file.read().decode("utf-8"))

    required = data['requires']
    
    # prepare forms
    forms = []
    for resource in required:
        form_dict = {}
        form_dict['name'] = resource
        form_dict['description'] = required[resource]['description']
        forms.append(form_dict)

    resource_forms = []
    req = []
    for f in forms:
        model_name = required[f['name']]['type'].title()+'Resource'
        model_form = get_resource_form(model_name)
        prf = '{}:{}'.format(f['name'], model_name)
        req.append(prf)
        res_form = model_form(initial=f, prefix=f['name'])
        resource_forms.append(res_form)

    # pass along app meta data
    meta = '{},{}'.format(data['image'], data['name']).replace(' ','-')

    return render(request, 'main.html', {'forms': resource_forms, 'meta': meta, 'req' : ','.join(req)})


# first view -- for file upload
def index(request):
    form = UploadFileForm()
    if request.method == "POST":
        return forms(request)
    return render(request, 'index.html', {'form': form})