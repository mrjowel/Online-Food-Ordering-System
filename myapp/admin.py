from django.contrib import admin
from myapp.models import Contact,Employees,product,Order

# Register your models here.
admin.site.site_header ="FooDie | Admin"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','added_on','is_approved']

class OrderAdmin(admin.ModelAdmin):
    list_display=['uname','phone','address','added_on','is_approved']

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'price', 'is_published','created_at')
    list_display_links=('id','name')
    list_filter=('price',)
    list_editable=('is_published',)
    search_fields=('name','price')
    ordering=('price',)
admin.site.register(product,ProductAdmin)   

admin.site.register(Contact, ContactAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Employees)