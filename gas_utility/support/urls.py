from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('status/', views.request_status, name='request_status'),
    path('detail/<int:request_id>/', views.request_detail, name='request_detail'),
    path('update/<int:request_id>/', views.update_request, name='update_request'),
]
