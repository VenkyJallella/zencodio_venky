from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render , get_object_or_404
from .models import blogpost



@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES:
        image = request.FILES['file']  # TinyMCE sends file as 'file'
        path = default_storage.save('uploads/' + image.name, ContentFile(image.read()))
        image_url = '/media/' + path  # Media URL for serving images
        return JsonResponse({'location': image_url})  # TinyMCE expects 'location'
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    posts = blogpost.objects.all()
    return render(request, 'blog/blog_list.html',{'posts':posts})

def blog_detail(request, slug):
    post = get_object_or_404(blogpost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post':post})

