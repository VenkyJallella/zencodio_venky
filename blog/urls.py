from .views import upload_image
from django.urls import path
from .views import home, blog_detail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('upload_image/', upload_image, name='upload_image'),
    path('', home, name='home'),
    path('<slug:slug>/',blog_detail,name='blog_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)