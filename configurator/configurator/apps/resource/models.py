from django.db import models
from polymorphic.models import PolymorphicModel

class Resource(PolymorphicModel):
    """Abstract resource."""

    # czy name nie powinien być czasem unique?
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def requirements(self):
        """Frozenset of resources directly required by this resource."""
        raise NotImplementedError()

    def optional_requirements(self):
        """Frozenset of resources directly optionally required by this
        resource."""
        raise NotImplementedError()

    def to_dicts_and_lists(self, depth=None):
        """Convert resource to structure of dicts and lists suitable for
        encoding in JSON.

        `depth` is integer or None. If None all subresources should be
        inlined. If not None subresources to this level should be
        inlined. Value of 0 means that only single id will be returned.
        """
        raise NotImplementedError()

    def __str__(self):
        return self.name


class StringResource(Resource):
    type_name = 'string'
    value = models.TextField()

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset()


class IntResource(Resource):
    type_name = 'int'
    value = models.IntegerField()

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset()


class ListResource(Resource):
    """List of resources. All of them should be same type."""
    type_name = 'list'
    value = models.ManyToManyField(Resource, related_name='member_of_lists')

    def requirements(self):
        return frozenset()

    def optional_requirements(self):
        return frozenset(self.value.all())


class DictResource(Resource):
    """Dictionary of which keys are strings and values are resources."""
    type_name = 'dict'

    def requirements(self):
        return frozenset(entry.value for entry in self.entries)

    def optional_requirements(self):
        return frozenset()

    def as_dict(self):
        return {entry.key: entry.value for entry in self.entries}


class DictResourceEntry(models.Model):
    """Single mapping string -> resource in dictionary of resources."""
    dictionary = models.ForeignKey(DictResource, related_name='entries')
    key = models.TextField()
    value = models.ForeignKey(Resource)

    def __str__(self):
        return '{} : {}'.format(self.dictionary, self.value)
