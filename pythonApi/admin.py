from django.contrib import admin
from .models import Post
from .models import Customer

admin.site.register(Post)
admin.site.register(Customer)