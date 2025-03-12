from django.urls import path
from .views import index, contact_us, about_me, projects_view, product_detail, checkout,payment_success, payment_success_view
from django.conf.urls.static import static
from django.conf import settings
from .views import faq_page, privacy_policy,terms_conditions,subscribe_newsletter, robots_txt, create_superuser
from .sitemaps import BlogPostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blog': BlogPostSitemap(),
    'static': StaticViewSitemap(),
}


urlpatterns = [
    path('', index, name='index'),
    path('faq/', faq_page, name='faq_page'),
    path('contactus/', contact_us, name='contactus' ),
    path('aboutus/', about_me, name='aboutus'),
    path('projects/', projects_view, name='projects'),
    path('projects/<int:pk>', product_detail , name='product-detail'),
    path('checkout/<int:product_id>/', checkout, name='checkout'),
    path("success/", payment_success_view, name="payment_success"),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path("payment-success/", payment_success, name="payment_success"),
    path('terms-and-conditions/', terms_conditions, name='terms_conditions'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("create-superuser/", create_superuser, name="create_superuser"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)