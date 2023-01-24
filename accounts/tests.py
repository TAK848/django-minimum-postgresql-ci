from django.test import TestCase
from django.urls import reverse

from .models import User


class TestSignUpView(TestCase):
    def setUp(self):
        self.url = reverse("accounts:signup")

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_success_post(self):
        user_data = {
            "username": "test",
            "email": "abcde@example.com",
            "password1": "i*9U92aasIhm",
            "password2": "i*9U92aasIhm",
        }

        response = self.client.post(self.url, user_data)

        self.assertRedirects(
            response,
            reverse("index"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

        self.assertTrue(
            User.objects.filter(
                username=user_data["username"],
                email=user_data["email"],
            ).exists(),
        )

    def test_failure_post_with_empty_password(self):
        username_empty_data = {
            "username": "test",
            "email": "testmail@example.com",
            "password1": "",
            "password2": "",
        }

        response = self.client.post(self.url, data=username_empty_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.all().count(), 0)

        context = response.context
        form = context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("このフィールドは必須です。", form.errors["password1"])
        self.assertIn("このフィールドは必須です。", form.errors["password1"])

    def test_failure_post_with_too_short_password(self):
        data = {
            "username": "test",
            "email": "test@example.com",
            'password1': 'u8@j(x',
            "password2": "u8@j(x",
        }
        response = self.client.post(self.url, data)
        self.assertFalse(
            User.objects.filter(
                username=data["username"],
                email=data["email"],
            ).exists()
        )
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("このパスワードは短すぎます。最低 8 文字以上必要です。", form.errors["password2"])
