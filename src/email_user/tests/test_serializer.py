import os

import dateutil.parser
from django.conf import settings

from django.test import TestCase

from .factories import EmailUserFactory

from ..serializers import EmailUserSerializer
from ..models import EmailUser


class EmailUserSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'Max',
            'last_name': 'Mustermann',
            'email': 'max.mustermann@abcd.de',
            'password': '123#234abc'
        }

    def test_serialize(self):
        obj = EmailUserFactory()

        ser = EmailUserSerializer(obj)
        result = ser.data

        self.assertEqual(result['first_name'], obj.first_name)
        self.assertEqual(result['last_name'], obj.last_name)
        self.assertEqual(result['email'], obj.email)
        self.assertEqual(result['is_staff'], obj.is_staff)
        self.assertEqual(result['is_active'], obj.is_active)
        self.assertEqual(dateutil.parser.parse(result['date_joined']), obj.date_joined)

    def test_serialize_write_only_not_found(self):
        obj = EmailUserFactory()

        ser = EmailUserSerializer(obj)

        self.assertNotIn('password', ser.data)

    def test_serialize_valid(self):
        ser = EmailUserSerializer(data=self.valid_data)
        self.assertTrue(ser.is_valid(True))

    def test_create(self):
        password = 'a1b2c3d4'
        obj = EmailUserFactory.build()

        self.assertFalse(EmailUser.objects.filter(email=obj.email).exists())

        ser = EmailUserSerializer(obj)
        data = dict(ser.data)
        data['password'] = password
        deser = EmailUserSerializer(data=data)
        deser.is_valid(True)
        deser.save()

        users = EmailUser.objects.filter(email=ser.data['email'])

        self.assertTrue(users.exists())
        self.assertTrue(users.get().check_password(password))

    def test_update_valid_field(self):
        obj = EmailUserFactory.create()

        self.assertTrue(EmailUser.objects.filter(email=obj.email).exists())

        ser = EmailUserSerializer(obj)
        data = dict(ser.data)
        data['first_name'] = 'SomeNew123 Random'
        deser = EmailUserSerializer(obj, data=data, partial=True)
        deser.is_valid(True)
        deser.save()

        obj.refresh_from_db()

        self.assertEqual(data['first_name'], obj.first_name)

    def test_update_password(self):
        obj = EmailUserFactory.create()

        ser = EmailUserSerializer(obj)
        data = {'email': ser.data['email'], 'password': 'NewNew1234'}
        deser = EmailUserSerializer(obj, data=data, partial=True)
        deser.is_valid(True)
        deser.save()

        obj.refresh_from_db()

        self.assertTrue(obj.check_password(data['password']))
