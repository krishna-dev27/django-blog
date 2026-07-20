from django.contrib import admin

# Register your models here.
from blogs.models import *
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
        
    }
    list_display = ('author','title', 'is_featured','status','category','category_id')
    search_fields = ('id', 'title')
    list_editable = ('is_featured','status')


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)