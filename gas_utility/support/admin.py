from django.contrib import admin
from .models import ServiceRequest, UserProfile

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'request_type')
    search_fields = ('user__username', 'details')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number')
