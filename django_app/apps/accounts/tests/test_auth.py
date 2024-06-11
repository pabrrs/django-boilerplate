from http import HTTPStatus

from django.test import TestCase

from django_app.apps.accounts.tests.mixins import CreateUserTestMixin


class AccountsAuthTestCase(CreateUserTestMixin, TestCase):
    def test_login_jwt(self):
        """
        Authenticate user in /api/login, retrieve the token and make a simple
        request to the api to check if token is valid and user can authenticate
        """
        jwt_res = self.client.post(
            "/api/login/",
            data={"email": self.test_user.email, "password": self.TEST_USER_PASSWORD},
            content_type="application/json",
        )

        assert jwt_res.status_code == HTTPStatus.OK, f"Request JWT failed: {jwt_res.content}"

        jwt_data = jwt_res.json()
        jwt_token = jwt_data["access"]

        assert jwt_token is not None
        assert jwt_data["refresh"] is not None

        api_res = self.client.get("/api/workers/", HTTP_AUTHORIZATION=f"Bearer {jwt_token}")

        assert api_res.status_code == HTTPStatus.OK, f"Request workers failed: {api_res.content}"

        workers = api_res.json()

        assert workers["results"] is not None

    def test_login_with_basic_token(self):
        """
        Authenticate to /integration/* nested endpoints using header Authorization: Token <token>
        """
        api_res = self.client.get(
            "/integration/workers/",
            HTTP_AUTHORIZATION=f"Token {self.test_user_token.key}",
        )

        assert api_res.status_code == HTTPStatus.OK, f"Request workers failed: {api_res.content}"

        workers = api_res.json()

        assert workers["results"] is not None
