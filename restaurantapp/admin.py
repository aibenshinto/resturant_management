from django.contrib import admin
from .models import Employee, Food, OrderItems, OrderDetails, District, State
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html

class EmpAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'ID_Number', 'Gender', 'phoneNumber', 'state', 'district')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('items', 'price')

class OrderItemsAdmin(admin.TabularInline):  # Make sure it's a TabularInline or StackedInline
    model = OrderItems
    list_display = ('OrderId', 'Items', 'Quantity')
    extra = 2  # Number of empty forms to display
    min_num = 1  # Minimum number of forms
    max_num = 20
    
class OrderItemsAdmin1(admin.ModelAdmin): 
    list_display = ('OrderId', 'Items', 'Quantity')

class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('OrderId', 'location', 'orderDate', 'DeliveryTime', 'staff', 'price', 'view_order_items')
    inlines = [OrderItemsAdmin]
    exclude = ('OrderId', 'price') 
    

    
    def save_model(self, request, obj, form, change):
        if not obj.OrderId:
            # Generate OrderID based on customer name, date, and time
            date_str = obj.orderDate.strftime("%m:%d")
            time_str = obj.DeliveryTime.strftime("%H:%M")
            obj.OrderId = f"{obj.Customer_Name}_{date_str}_{time_str}"

        super().save_model(request, obj, form, change)
        
    def view_order_items(self, obj):
        receipts_url = reverse('admin:%s_%s_changelist' % (OrderItems._meta.app_label,  OrderItems._meta.model_name))
        return format_html('<a href="{}?OrderId__id__exact={}">View Items</a>', receipts_url, obj.id)

    view_order_items.short_description = 'Order Items'
    



    
class StateAdmin(admin.ModelAdmin):
    list_display = ('state',)

class DistAdmin(admin.ModelAdmin):
    list_display = ('state', 'district')

admin.site.register(Employee, EmpAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(OrderItems, OrderItemsAdmin1)
admin.site.register(OrderDetails, OrderDetailsAdmin)

admin.site.register(District, DistAdmin)
admin.site.register(State, StateAdmin)
