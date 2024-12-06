from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    # Create
    path('', views.Create_enquiry, name='create_enquiry'),

    # Read (list all enquiries)
    path('read', views.read, name='read'),

    # Update
    path('update_enquires/<int:id>/', views.update_enquires, name='update_enquiry'),

    # Delete
    path('delete/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
]
