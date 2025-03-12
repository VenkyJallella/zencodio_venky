from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render , get_object_or_404
from .models import blogpost
import cloudinary



@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES:
        image = request.FILES['file']  # TinyMCE sends the file as 'file'

        # Upload the image to Cloudinary
        result = cloudinary.uploader.upload(image)

        # Get the secure URL of the uploaded image
        image_url = result.get("secure_url")

        return JsonResponse({'location': image_url})  # TinyMCE expects 'location'
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    posts = blogpost.objects.all()
    return render(request, 'blog/blogpost.html',{'posts':posts})

def blog_detail(request, slug):
    post = get_object_or_404(blogpost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post':post})

