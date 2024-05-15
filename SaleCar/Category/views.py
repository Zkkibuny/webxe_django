

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Holder, Car, CarDetail
from django.db import connection
# Create your views here.

class HolderListView(ListView):
    model = Holder
    template_name='category/holder_info.html'
class HolderDetailView(DetailView):
    model = Car
    template_name="category/holder_detail.html"
class CarListView(ListView):
    model = Car
    template_name="category/car_info.html"
    context_object_name = 'holder'
class CarDetailView(DetailView):
    model = Car
    template_name="category/car_detail.html"
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_details'] = CarDetail.objects.filter(Car=self.object)
        return context
def Home(request):
    return render(request,'category/home.html')

