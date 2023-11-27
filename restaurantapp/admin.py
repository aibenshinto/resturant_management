from django.contrib import admin
from .models import Employee, Food, OrderItem, OrderDetail, District, State
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html

class EmpAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'ID_Number', 'Gender', 'phoneNumber', 'state', 'district')
    exclude = ('ID_Number',)
    # def save_model(self, request, obj, form, change):
    #     if not obj.ID_Number:
    #         # Generate OrderID based on customer name

    #         obj.ID_Number = f"{obj.FullName}"

    #     super().save_model(request, obj, form, change)
        
    def save_model(self, request, obj, form, change):
        if not obj.ID_Number:
            # Generate a unique ID starting with '00'
            last_id = Employee.objects.order_by('-ID_Number').first()

            if last_id:
                # Increment the last ID by 1
                new_id = int(last_id.ID_Number) + 1
            else:
                # If there are no existing IDs, start with '00'
                new_id = 0

            # Format the new ID as a string with leading zeros
            obj.ID_Number = f"{new_id:02d}"

        super().save_model(request, obj, form, change)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('items', 'price')

class OrderItemsAdmin(admin.TabularInline):  # Make sure it's a TabularInline or StackedInline
    model = OrderItem
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
        receipts_url = reverse('admin:%s_%s_changelist' % (OrderItem._meta.app_label,  OrderItem._meta.model_name))
        return format_html('<a href="{}?OrderId__id__exact={}">View Items</a>', receipts_url, obj.id)

    view_order_items.short_description = 'Order Items'
    



    
class StateAdmin(admin.ModelAdmin):
    list_display = ('state',)

class DistAdmin(admin.ModelAdmin):
    list_display = ('state', 'district')

admin.site.register(Employee, EmpAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(OrderItem, OrderItemsAdmin1)
admin.site.register(OrderDetail, OrderDetailsAdmin)

admin.site.register(District, DistAdmin)
admin.site.register(State, StateAdmin)
