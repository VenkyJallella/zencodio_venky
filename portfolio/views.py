from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Contact_Me, About_me, projects, Payment
from .forms import contact_form
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Payment
from blog.models import blogpost
from blog.models import FAQ
from .models import Testimonial
from .models import NewsletterSubscriber

# Create your views here.

def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/\nSitemap: https://zencodio.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not NewsletterSubscriber.objects.filter(email=email).exists():
            NewsletterSubscriber.objects.create(email=email)
            messages.success(request, "You have successfully subscribed!")
        return redirect(request.META.get('HTTP_REFERER', 'home'))  # Stay on the same page

    return render(request, 'newsletter.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

def index(request):
   
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    all_projects = projects.objects.all()
    latest_blogs = blogpost.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {'all_projects': all_projects, 'latest_blogs':latest_blogs,'faqs':faqs,'testimonials': testimonials})

def contact_us(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send email notification
            subject = f"Contact Form Submission from {name}"
            body = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject,
                body,
                email,  # Email from the user
                [settings.EMAIL_HOST_USER],  # Email to send the notification to (e.g., admin)
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully")
            return redirect('contactus')
        else:
            messages.error(request, "Please correct the errors below")

    else:
        form = contact_form()
    return render(request, 'contactus.html', {'form':form})

def about_me(request):
    about_data = About_me.objects.all()
    return render(request, 'aboutus.html',{'about_data':about_data})


def projects_view(request):
    new_project = projects.objects.all()
    return render(request, 'projects.html',{'new_projects':new_project})

def product_detail(request, pk):
    project = get_object_or_404(projects, pk=pk)
    return render(request, 'product-detail.html', {'project': project})

def checkout(request, product_id):
    product = get_object_or_404(projects, id=product_id)
    
    amount = int(product.price)*100
    name = product.name
    if request.method == 'POST':
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        payment=Payment.objects.create(email=email,address=address,phone=phone)
        payment.save()
    razorpay_client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order_data = {'amount':amount, 'currency':'INR','payment_capture':'1'}
    order = razorpay_client.order.create(order_data)
    payment = Payment.objects.create(order_id=order['id'],amount=product.price,status='pending',name=product.name)

    return render(request,"payment.html", {
        'order_id':order['id'],
        'key_id': settings.RAZORPAY_KEY_ID,
        'amount':amount/100,
        'name': name
        })
    

   

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order_id = data.get("order_id")
        payment_id = data.get("payment_id")
        
        

        payment = Payment.objects.get(order_id=order_id)
        payment.payment_id = payment_id
        payment.status = "Paid"
        payment.save()

        return JsonResponse({"message": "Payment Successful!"})

    return JsonResponse({"error": "Invalid request"}, status=400)


def payment_success_view(request):
    payment_id = request.GET.get("payment_id")
    order_id = request.GET.get("order_id")
    amount = request.GET.get("amount") 
    return render(request, "success.html", {
        "payment_id": payment_id,
        "order_id": order_id,
       
        })











