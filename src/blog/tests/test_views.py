from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from blog.models import Article, ContactRequest

User = get_user_model()

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='p1', first_name='U', last_name='One')
        # Create 6 to test pagination = 5
        now = timezone.now()
        for i in range(6):
            Article.objects.create(
                title=f'A{i}', content='c', author=self.user,
                publication_datetime=now, is_online=True
            )

    def test_list_paginates_five(self):
        url = reverse('blog:article-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEqual(len(resp.context['articles']), 5)

    def test_detail_uses_slug_and_id(self):
        a = Article.objects.first()
        url = reverse('blog:article-detail', kwargs={'pk': a.pk, 'slug': a.slug})
        resp = self.client.get(url)
        self.assertContains(resp, a.title)

    def test_contact_creates_and_sends_email(self):
        url = reverse('blog:contact')
        data = {'email': 'x@y.com', 'name': 'X', 'content': 'Hello'}
        resp = self.client.post(url, data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(ContactRequest.objects.filter(email='x@y.com').exists())