from django.contrib import admin
# Register your models here.

#importing our POST model
from . models import Post

admin.site.register(Post)
