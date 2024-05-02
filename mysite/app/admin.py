from django.contrib import admin
from .models import Customer
from markdownx.admin import MarkdownxModelAdmin

class CustomerAdmin(MarkdownxModelAdmin):  
    list_display = ('user', 'bio', 'exp')
    search_fields = ('user__username', 'bio', 'exp')
    readonly_fields = ('user',)  

admin.site.register(Customer, CustomerAdmin)
