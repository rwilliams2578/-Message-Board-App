from django.test import TestCase

from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    """Post Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests"""
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        """Test the model content"""
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        """Test that url exist at the correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url is available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test that the template name is correct"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """Test the content of the template"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
