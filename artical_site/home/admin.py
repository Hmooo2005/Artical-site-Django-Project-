from django.contrib import admin
from .models import Artical, Comment
# Register your models here.

class ArticalAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')


admin.site.register(Artical, ArticalAdmin)
admin.site.register(Comment)
