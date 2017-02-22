# from __future__ import unicode_literals, print_function, division, absolute_import
#
# from common.testconfig import TestCase
#
# from authlayer.models import UserProfile, ThingAppUser
# from authlayer.serialization import ThingAppUserSerializer, UserProfileSerializer
# from authlayer.tests.factories import ThingAppUserFactory, UserProfileFactory
#
#
# class UserSerializerTest(TestCase):
#     def setUp(self):
#         self.orig_user = ThingAppUserFactory()
#         self.orig_profile = UserProfileFactory(user=self.orig_user)
#
#         self.user_data = ThingAppUserSerializer(instance=self.orig_user).data
#         self.profile_data = UserProfileSerializer(instance=self.orig_profile).data
#         self.orig_user.delete()
#
#     def test_create(self):
#         print(self.user_data['userprofile']['phone'])
#         user_serializer = ThingAppUserSerializer(data=self.user_data)
#         self.assertSerializerValid(user_serializer)
#
#         user_serializer.save()
#
#         self.assertTrue(1, ThingAppUser.objects.count())
#         self.assertTrue(1, UserProfile.objects.count())
#
#     def test_update(self):
#         orig_user = UserProfileFactory().user
#
#         user_data = ThingAppUserSerializer(instance=orig_user).data
#
#         expected_last_name = 'LastnameExt'
#         expected_phone = '+41524204242'
#
#         user_data['last_name'] = expected_last_name
#         user_data['userprofile']['phone'] = expected_phone
#
#         serializer = ThingAppUserSerializer(instance=orig_user, data=user_data)
#         self.assertSerializerValid(serializer)
#         serializer.save()
#
#         self.assertEqual(1, UserProfile.objects.count())
#         self.assertEqual(1, ThingAppUser.objects.count())
#
#         profile = UserProfile.objects.first()
#         user = ThingAppUser.objects.first()
#
#         self.assertEqual(expected_last_name, user.last_name)
#         self.assertEqual(expected_phone, profile.phone)