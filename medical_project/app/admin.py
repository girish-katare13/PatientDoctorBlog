from django.contrib import admin
from .models import CustomUser,Category,BlogPost

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_draft', 'created_at')  # Add more fields as needed
    list_filter = ('category', 'author', 'is_draft')  # Add filters for convenient searching
    search_fields = ('title', 'content')  # Add search functionality for these fields


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost,BlogPostAdmin)