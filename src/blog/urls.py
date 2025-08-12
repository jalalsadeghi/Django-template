from django.urls import path
from .views import ArticleListView, ArticleDetailView, ContactView

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # URL contains both id and slug as required
    path('articles/<int:pk>/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]