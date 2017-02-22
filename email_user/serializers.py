from __future__ import division, print_function, absolute_import
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import EmailUser

class EmailUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EmailUser
        fields = ('first_name', 'last_name', 
                  'email', 'password', 'is_staff', 'is_active',
                  'date_joined', 
                  )

        read_only_fields = ('is_staff', 'is_active',
                            'date_joined', 
                           )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = EmailUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = EmailUser(id=instance.id, **validated_data)

        user.save(update_fields=validated_data.keys(), force_update=True)

        return user

