from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

class Article(models.Model):
    """Blog article with a prepopulated slug from title."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, help_text="Auto-generated from title.")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    publication_datetime = models.DateTimeField()
    is_online = models.BooleanField(default=False)

    class Meta:
        ordering = ['-publication_datetime']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # URL must contain both slug and id as required by the brief
        return reverse('blog:article-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def save(self, *args, **kwargs):
        # Ensure slug is generated from title if missing
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ContactRequest(models.Model):
    """Contact request; can only be removed in admin (no add/edit)."""
    email = models.EmailField()
    name = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"ContactRequest from {self.name} <{self.email}>"