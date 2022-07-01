from django.db.models import EmailField

from email_user.conf import StoreMethod


class CaseEmailField(EmailField):
    def to_python(self, value):
        value = super().to_python(value)

        if not isinstance(value, str):
            return value

        method = StoreMethod.from_settings()
        return method.value(value)
