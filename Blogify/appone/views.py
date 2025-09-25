from django.shortcuts import render
from .models import Blogs
# Create your views here.
def showblogs(request):
    blogs = Blogs.objects.all()
    return render(request, "app1/app1.html", {"blogs": blogs})

def showhome(request):
    return render(request, "app1/home.html")