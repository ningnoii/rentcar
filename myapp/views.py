from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Car, Rent
from django.views.generic import TemplateView
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import PersonForm,RentForm
from .models import Person, Image
class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'
class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'
def home(request):
	return 'Hello World'
#def listCar(request):
	#return render(request,'lsit.html',{})
class CarListView(ListView):
	model = Car
	template_name='carlist.html'
	#context_object_name = 'my_car_list'
	#การหา
	#queryset = Car.objects.filter(title_icontains='war')[:5]
	#template_name ='book/myarbitrary_template_name_list.html'
class RentListView(ListView):
	model = Rent
	template_name='rentlist.html'
class ListPersonView(ListView):
    model = Person
    template_name='list.html'
class RentCar(CreateView):
	queryset = Rent
	template_name = 'rentcar.html'
	form_class = RentForm
	success_url = '/cars_list'
#class Return(UpdateView):
#	queryset = Return.objects.all()
#	template_name = 'returncar.html'