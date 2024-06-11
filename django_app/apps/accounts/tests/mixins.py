from rest_framework.authtoken.models import Token

from django_app.apps.accounts.models import User


class CreateUserTestMixin:
    TEST_USER_PASSWORD = "Abc@1234"

    @classmethod
    def setUpClass(cls):
        test_user = User.objects.create(first_name="Test", last_name="User", email="test_user@django.io")
        test_user.set_password(cls.TEST_USER_PASSWORD)
        test_user.save()

        test_user_token = Token.objects.create(user=test_user)
        test_user_token.save()

        cls.test_user = test_user
        cls.test_user_token = test_user_token

    @classmethod
    def tearDownClass(cls):
        cls.test_user.delete()
        cls.test_user_token.delete()
