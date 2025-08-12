from django.views.generic import ListView, DetailView, FormView
from django.utils import timezone
from django.core.mail import EmailMessage
from django.urls import reverse_lazy

from .models import Article, ContactRequest
from .forms import ContactForm

class ArticleListView(ListView):
    """Show 5 entries per page with pagination at bottom."""
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5  # As explicitly required

    def get_queryset(self):
        # Show only online and published articles
        now = timezone.now()
        return Article.objects.filter(is_online=True, publication_datetime__lte=now)

class ArticleDetailView(DetailView):
    """Detail requires slug and id in the URL."""
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

class ContactView(FormView):
    """Stores entry and sends an email to debug@mir.de with Reply-To as the user's email."""
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:article-list')

    def form_valid(self, form):
        # Save to DB
        contact: ContactRequest = form.save()

        # Send email to debug@mir.de with content and name; set Reply-To
        body = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n\n"
            f"Message:\n{contact.content}\n"
        )
        msg = EmailMessage(
            subject="New Contact Request",
            body=body,
            to=["debug@mir.de"],
            reply_to=[contact.email],  # Critical: Reply-To must be sender's email
        )
        msg.send(fail_silently=False)
        return super().form_valid(form)