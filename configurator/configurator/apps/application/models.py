from django.db import models

from configurator.apps.resource.models import Resource, DictResource


class AppResource(Resource):
    """An installed application."""
    required_resource = models.ForeignKey(
        DictResource,
        related_name='required_by_apps'
    )

    image_name = models.CharField(max_length=200)
    command = models.CharField(max_length=400, blank=True, null=True)


class MountedFile(models.Model):
    app = models.ForeignKey(AppResource, related_name='files')
    mount_path = models.CharField(max_length=300)
    file = models.FileField(upload_to='mounted_files/')

    def requirements(self):
        return frozenset([self.required_resource])

    def optional_requirements(self):
        return frozenset()

    def __str__(self):
        return '{}: {}'.format(self.app, self.mount_path)
