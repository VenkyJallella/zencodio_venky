from django.contrib import admin
from . models import projects, herosection, Contact_Me, About_me, tech, Payment
from .models import Testimonial, NewsletterSubscriber

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'rating')

models = [projects, herosection, About_me, Contact_Me,tech,Payment, NewsletterSubscriber]
admin.site.register(models)
