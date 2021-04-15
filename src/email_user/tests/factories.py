import factory
try:
    # new package since factory_boy 3.0.0
    from factory.django import DjangoModelFactory
except AttributeError:
    from factory import DjangoModelFactory

from email_user import models


class EmailUserFactory(DjangoModelFactory):
    PASSWORD = 'pw'

    class Meta(object):
        model = models.EmailUser
        exclude = ('PASSWORD', )
        django_get_or_create = ('email', )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda self: '{0}@example.com'.format(self.last_name))
    is_staff = False
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', PASSWORD)
