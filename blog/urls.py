from .views import upload_image
from django.urls import path
from .views import home, blog_detail


urlpatterns = [
    path('upload_image/', upload_image, name='upload_image'),
    path('', home, name='home'),
    path('<slug:slug>/',blog_detail,name='blog_detail'),
    
]