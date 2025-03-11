from django.contrib import admin
from .models import blogpost
from django.db import models
from tinymce.widgets import TinyMCE
from .models import FAQ
# Register your models here.

class blogpostadmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE(attrs={'cols':80,'rows':30})}
    }

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')

admin.site.register(blogpost, blogpostadmin)
