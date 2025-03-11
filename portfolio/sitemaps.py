from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import blogpost  # Change to your model

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return blogpost.objects.all()  # Returns all blog posts

    def lastmod(self, obj):
        return obj.updated_at  # Ensure your model has an updated_at field

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['index', 'aboutus', 'contactus','faq_page','projects','payment_success',
                'privacy_policy','terms_conditions','subscribe_newsletter','home']  # Add static page names

    def location(self, item):
        return reverse(item)  # Uses URL names
