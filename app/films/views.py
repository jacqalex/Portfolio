from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film
from films.serializer import FilmSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view

class FilmBaseView(View):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films:all')

class FilmListView(FilmBaseView, ListView):
    @api_view(['GET', 'POST', 'DELETE'])
    def film_list(request):
        if request.method == 'POST':
          film_data = JSONParser().parse(request)
        film_serializer = FilmSerializer(data=film_data)
        if film_serializer.is_valid():
           film_serializer.save()
           return JsonResponse(film_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(film_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

       
class FilmDetailView(FilmBaseView, DetailView):
    @api_view(['GET', 'PUT', 'DELETE'])
    def film(request,pk):        # find film by pk (id)
        pass
        try: 
            films = Film.objects.get(pk=pk) 
        except Film.DoesNotExist: 
            return JsonResponse({'message': 'The film does not exist'}, status=status.HTTP_404_NOT_FOUND) 
   
class FilmCreateView(FilmBaseView, CreateView):
    """View to create a new film"""

class FilmUpdateView(FilmBaseView, UpdateView):
    """View to update a film"""

class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""
