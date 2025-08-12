from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AdminPermissionsTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        self.client.login(username='admin', password='pass')

    def test_contact_no_add_change(self):
        # Add page should be disallowed (403)
        resp = self.client.get('/admin/blog/contactrequest/add/')
        self.assertEqual(resp.status_code, 403)