import django.forms as forms
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild
from configurator.apps.resource.models import *
from configurator.apps.application.models import *
from configurator.apps.http_resource.models import *

# django-polymorphic formset 
ResourceFormSet = polymorphic_modelformset_factory(Resource, formset_children=(
    PolymorphicFormSetChild(StringResource),
    PolymorphicFormSetChild(IntResource),
    PolymorphicFormSetChild(ListResource),
    PolymorphicFormSetChild(DictResource),
    PolymorphicFormSetChild(AppResource),
    PolymorphicFormSetChild(HTTPResource),
), fields = ('name', 'description',))

# file upload form
class UploadFileForm(forms.Form):
    file = forms.FileField(label="Wybierz plik konfiguracyjny")