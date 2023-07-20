from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
   
    
)
from .models import Empleado
# Create your views here.

class InicioView(TemplateView):
    template_name='inicio.html'

class ListAllEmpleados(ListView):
    """ Lista de todos los empleados"""
    template_name = 'persona/list_all.html'
    paginate_by=5
    model = Empleado

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )    
        return lista
    

class ListByAreaEmpleado(ListView):
    """ Lista de empleados de un área"""
    template_name = 'persona/list_by_area.html'
    context_object_name='empleados'
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista
    

class ListaEmpleadosAdmin(ListView):
    """ Lista de empleados de un área"""
    template_name = 'persona/lista_empleados.html'
    paginate_by=10
    ordering='first_name'
    context_object_name='empleados'
    model=Empleado    
    

class ListEmpleadosByKwords(ListView):
    """ lista de empleados por palabra clave """
    template_name='persona/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self):
        print('*********************************')
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )    
        return lista
    

class ListHabilidadesEmpleados(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=6)
        return empleado.habilidades.all()
        
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"




class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields=['first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            ]
    success_url=reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado=form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields=['first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            ]
    success_url=reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #logica del proceso
        empleado=form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url=reverse_lazy('empleados_app:empleados_admin')
