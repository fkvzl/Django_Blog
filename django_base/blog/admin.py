from django.contrib import admin
from blog.models import BlogK
 
# Register your models here.

class BlogKAdmin(admin.ModelAdmin):
    # pk:索引
    # 属性list_display表示要显示哪些属性
    list_display = ['pk','title','body','create_date']
admin.site.register(BlogK,BlogKAdmin)