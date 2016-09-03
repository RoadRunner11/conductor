from django.conf import settings
import factory

from accounts import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class InviteEmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.InviteEmail

    email = factory.Faker('email')
