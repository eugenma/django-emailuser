from rest_framework import serializers

from .models import EmailUser


class EmailUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EmailUser
        fields = ('first_name', 'last_name',
                  'email', 'password', 'is_staff', 'is_active',
                  'date_joined',
                  )

        read_only_fields = ('is_staff', 'is_active', 'date_joined', )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        user = EmailUser.objects.create(**validated_data)

        if password:
            user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        user = EmailUser(id=instance.id, **validated_data)

        update_fields = validated_data.keys()

        if password:
            user.set_password(password)
            update_fields = list(update_fields) + ['password', ]

        user.save(update_fields=update_fields, force_update=True)

        return user
