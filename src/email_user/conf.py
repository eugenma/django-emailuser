import enum
from functools import partial
from typing import Any, Mapping

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager


def _store_exact(value: str) -> str:
    return value


# Below we want that functions are enum values. This is only possible with the trick using `partial()` wrapper without
#   any partial argument.
class StoreMethod(enum.Enum):
    exact = partial(_store_exact)
    lower = partial(str.lower)
    normalize = partial(BaseUserManager.normalize_email)

    @classmethod
    def from_settings(cls) -> 'StoreMethod':
        conf = getattr(settings, 'DJANGO_EMAIL_USER', {})  # type: Mapping[str, Any]
        key = conf['STORE_METHOD']
        try:
            return cls[key]
        except KeyError:
            keys = ', '.join(map(str, cls))
            msg = f"Key '{key}' not found. All available are {keys}."
            raise ValueError(msg)

    def __repr__(self):
        self.value.__repr__()
