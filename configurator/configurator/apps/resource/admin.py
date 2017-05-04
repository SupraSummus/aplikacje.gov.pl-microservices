from django.contrib import admin
from .models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


class ResourceChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Resource

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     ...
    # )


@admin.register(StringResource)
class StringResourceAdmin(ResourceChildAdmin):
    base_model = StringResource
    show_in_index = True
    # define custom features here


@admin.register(IntResource)
class IntResourceAdmin(ResourceChildAdmin):
    base_model = IntResource
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here

@admin.register(ListResource)
class ListResourceAdmin(ResourceChildAdmin):
    base_model = ListResource
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here

@admin.register(DictResource)
class DictResourceAdmin(ResourceChildAdmin):
    base_model = DictResource
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here


@admin.register(Resource)
class ResourceParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Resource
    child_models = (StringResource, IntResource, ListResource, DictResource)
    # list_filter = (PolymorphicChildModelFilter,)  # This is optional.


admin.site.register(DictResourceEntry)