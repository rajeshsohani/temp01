from django.contrib import admin
from .models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description', 'url','add_date')
    search_fields = ('title',)
    list_per_page = 20

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 20


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
