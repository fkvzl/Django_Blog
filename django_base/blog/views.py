from django.shortcuts import render
from blog.models import BlogK
def archive(request):
    posts=BlogK.objects.all() #获取数据库所有对象
    return render(request, 'archive.html', {'posts': posts})

# Create your views here.
