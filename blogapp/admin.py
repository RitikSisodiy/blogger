from django.contrib import admin
# ragister your models here
from .models import blog,like,comment,otp
admin.site.register(blog)
admin.site.register(comment)
admin.site.register(like)