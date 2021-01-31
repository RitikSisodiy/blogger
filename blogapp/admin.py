from django.contrib import admin
# ragister your models here
from .models import blog,comment,otp
admin.site.register(blog)
admin.site.register(comment)
