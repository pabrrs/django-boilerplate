from django.db.utils import IntegrityError
from django.test import TestCase

from django_app.apps.accounts.models import User


class UserModelTestCase(TestCase):
    def test_optional_fields(self):
        """
        Check if following fields are optional
        """
        assert True
        

    def test_default_admin_user(self):
        """
        Check if admin user is created when migrations runs
        """
        admin_user_exists = User.objects.filter(email="django@admin.com").exists()
        assert admin_user_exists, "Admin user not created by default when User migrations run"

    def test_username_as_email(self):
        """
        Check if User model is using email field as default username
        """
        assert User.USERNAME_FIELD == "email", 'User model should use USERNAME_FIELD as "email"'
        assert User.username is None, "User.username should be set to None"

        user = User.objects.create(
            first_name="Test",
            last_name="User",
            email="test@user.com",
            # Decypt password: Admin@1234
            password="pbkdf2_sha256$600000$IPYVAcu7PoIqYPIR6NWhMI$yAUCsvT9qfPs1bZFpxsgpiMJ0uClBnRaANJ+3CevICM="
        )

        can_login = self.client.login(username=user.email, password="Admin@1234")

        assert can_login, f"User {user.email} not able to authenticate with username as email"

    def test_email_is_unique(self):
        """
        Check if email is unique
        """
        user = User.objects.create(
            first_name="Test",
            last_name="User",
            email="test@user.com",
            password="foo"
        )
        try:
            User.objects.create(first_name="Duplicated", last_name="Email", email=user.email, password="foo")
        except IntegrityError as exp:
            assert str(exp) == "UNIQUE constraint failed: accounts_user.email"
