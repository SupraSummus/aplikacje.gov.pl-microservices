import django.forms as forms
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild
from configurator.apps.resource.models import *
from configurator.apps.application.models import *
from configurator.apps.http_resource.models import *

ResourceFormSet = polymorphic_modelformset_factory(Resource, formset_children=(
    PolymorphicFormSetChild(StringResource),
    PolymorphicFormSetChild(IntResource),
    PolymorphicFormSetChild(ListResource),
    PolymorphicFormSetChild(DictResource),
    PolymorphicFormSetChild(AppResource),
    PolymorphicFormSetChild(HTTPResource),
), fields = ('name', 'description',))

class StringResourceForm(forms.ModelForm):
    class Meta:
        model = StringResource
        fields = ('name', 'description','value',)
        widgets = {
            'name': forms.HiddenInput(),
            'description': forms.HiddenInput()
        }

# class ResourceForm(forms.Form):
# 	name = forms.CharField(widget=forms.HiddenInput)
# 	description = forms.TextField(widget=forms.HiddenInput)
# 	model = forms.CharField(widget=forms.HiddenInput)
# 	value = 

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Wybierz plik konfiguracyjny")