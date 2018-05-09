import factory
from email_user import models


class EmailUserFactory(factory.DjangoModelFactory):
    PASSWORD = 'pw'

    class Meta(object):
        model = models.EmailUser
        exclude = ('PASSWORD', )
        django_get_or_create = ('email', )

    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda self: '{0}@example.com'.format(self.last_name))
    is_staff = False
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', PASSWORD)

