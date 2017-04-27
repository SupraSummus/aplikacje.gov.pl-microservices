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
), exclude=('id', 'polymorphic_ctype', 'delete'))

class StringResourceForm(forms.ModelForm):
    class Meta:
        model = StringResource
        fields = ('name', 'description','value',)
        widgets = {
            'name': forms.HiddenInput(),
            'description': forms.HiddenInput()
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()