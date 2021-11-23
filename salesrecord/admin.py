from django.contrib import admin
from .models import Salesrecord

class SalesrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'purchased_items',   'price', 'showroom','paid', 'date']
    list_filter = ['customer_name','customer_name', 'customer_phone', 'purchased_items',   'price', 'showroom','paid', 'date']
    search_fields =['customer_name','customer_name', 'customer_phone', 'purchased_items',   'price', 'showroom','paid', 'date'
    ]


admin.site.register(Salesrecord, SalesrecordAdmin)