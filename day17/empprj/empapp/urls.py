from django.urls import path
from empapp import views

urlpatterns = [
    
    path('list',views.EmployeeListView.as_view(), name='list'),
    
]