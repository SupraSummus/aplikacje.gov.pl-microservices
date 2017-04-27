import json, sys
from django.shortcuts import render
from configurator.apps.resource.forms import ResourceFormSet, StringResourceForm, UploadFileForm
from configurator.apps.resource.models import Resource

def forms(request):
    file = request.FILES['file']
    # print(dir(file))
    # with open(file, 'r') as myfile:
        # data = myfile.read().replace('\n', '')
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
    name = required['title']['type'].title()+'ResourceForm'
    model = getattr(sys.modules[__name__], name)
    print(forms[0])
    formset = ResourceFormSet()
    form = model(initial=forms[0])
    return render(request, 'main.html', {'formset': formset, 'form':form, 'req' : required})

def index(request):
    form = UploadFileForm()
    return render(request, 'index.html', {'form': form})