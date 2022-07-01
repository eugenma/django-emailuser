import dataclasses
from typing import Mapping

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager

from email_user.conf import StoreMethod
from email_user.tests.factories import EmailUserFactory


def get_setting_value(value: str) -> Mapping[str, str]:
    return {
        'STORE_METHOD': value,
    }


UserModel = get_user_model()

template_email = "ExacT.ThIsAn@RaNdOm.ml"


@dataclasses.dataclass
class Sample:
    name: str
    expected: str


testdata = [
    Sample(StoreMethod.exact.name, template_email),
    Sample(StoreMethod.lower.name, template_email.lower()),
    Sample(StoreMethod.normalize.name, BaseUserManager.normalize_email(template_email))
]

testdata_ids = [e.name for e in testdata]


@pytest.fixture(params=testdata, ids=testdata_ids)
def test_case(settings, request) -> Sample:
    settings.DJANGO_EMAIL_USER = get_setting_value(request.param.name)
    return request.param


@pytest.mark.django_db
def test_email_case_factory(test_case: Sample):
    obj = EmailUserFactory(email=template_email)

    actual = UserModel.objects.get(id=obj.id)

    assert actual.email == test_case.expected


@pytest.mark.django_db
def test_email_case_manager_create_user(test_case: Sample):
    data = EmailUserFactory.build(email=template_email)
    assert data.email == template_email, "Something went wrong, Factory should not modifiy the email."

    expected = UserModel.objects.create_user(email=template_email, password=data.password)
    actual = UserModel.objects.get(id=expected.id)

    assert actual.email == test_case.expected


@pytest.mark.django_db
def test_email_case_manager_create_superuser(test_case: Sample):
    data = EmailUserFactory.build(email=template_email)
    assert data.email == template_email, "Something went wrong, Factory should not modifiy the email."

    expected = UserModel.objects.create_superuser(email=template_email, password=data.password)
    actual = UserModel.objects.get(id=expected.id)

    assert actual.email == test_case.expected


@pytest.mark.django_db
def test_email_case_manager_create_by_save(test_case: Sample):
    expected = EmailUserFactory.build(email=template_email)
    assert expected.email == template_email, "Something went wrong, Factory should not modifiy the email."

    expected.save()
    actual = UserModel.objects.get(id=expected.id)

    assert actual.email == test_case.expected
