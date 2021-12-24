from django.shortcuts import render
from django.views.generic import *
from empapp.models import Employee
from empapp.forms import EmployeeForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

class HomeView(TemplateView):
    template_name = 'emp/home.html'
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp/list.html'
    paginate_by = 10
    queryset = Employee.objects.order_by('id')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee List"
        return context    
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'emp/empform.html'
    form_class = EmployeeForm
    
    def get_success_url(self)->str:
        messages.add_message(self.request,messages.INFO,'Employee Created Successfully')
        return reverse('list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employee Entry'
        context["heading" ] = 'Create New Employee'
        return context   
    
class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()
    template_name = 'emp/details.html'   