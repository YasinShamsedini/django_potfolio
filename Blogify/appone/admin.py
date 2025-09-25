from django.contrib import admin
from .models import Blogs

# Register your models here.
@admin.register(Blogs)
class app1admin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title",)
    list_filter = ("title", "created_at",)

