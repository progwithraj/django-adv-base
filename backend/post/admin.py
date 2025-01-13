from django.contrib import admin

from .models import Bookmarks, Category, Comments, Posts

# Register your models here.
admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Bookmarks)
