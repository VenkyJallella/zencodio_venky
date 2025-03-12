from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Contact_Me(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, blank=False)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class About_me(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = CloudinaryField('profile_pic')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class tech(models.Model):
    image = models.ImageField(upload_to='techimages/')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class projects(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description= models.CharField( max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.name
    def is_available(self):
        return self.stock > 0
    
class herosection(models.Model):
    heading = models.CharField( max_length=300)
    sub_heading = models.CharField(max_length=500)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    product_name = models.CharField(max_length=225)
    order_id = models.CharField( max_length=225, unique=True)
    payment_id = models.CharField(max_length=225, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=100, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.order_id} - {self.status}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)  # Optional
    review = models.TextField()
    rating = models.IntegerField(default=5)  # 1 to 5 stars
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Optional

    def __str__(self):
        return self.name