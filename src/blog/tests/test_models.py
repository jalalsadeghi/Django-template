from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from blog.models import Article, ContactRequest

User = get_user_model()

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='p1')

    def test_article_slug_autofill(self):
        a = Article.objects.create(
            title='Hello World',
            content='x',
            author=self.user,
            publication_datetime=timezone.now(),
            is_online=True,
        )
        self.assertTrue(a.slug)

    def test_contact_str(self):
        c = ContactRequest.objects.create(email='a@b.com', name='Alice', content='Hi')
        self.assertIn('Alice', str(c))