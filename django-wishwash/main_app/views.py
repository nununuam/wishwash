#from .models import (models name here)
#from calendar import calender
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response 
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import List, Book
import requests
import json

class Home(TemplateView):
    template_name = "home.html"
    response = requests.get("https://imdb-api.com/en/API/Top250Movies/k_lblhnjr6")
    #print(response.status_code)
    #print(response.json())
    #def jprint(obj):
     #   text = json.dumps(obj, sort_keys=True, indent=4)
      #  print(text)
       # return text
    #jprint(response.json())

    #def gprint(text):
     #   array1 = text[1]
      #  print(array1 + "hello")

class Movies(TemplateView):
    template_name = "movies.html"
#API testing codes below
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #name = self.request.GET.get('moviename')
        #if name != None:
        #print(name)
        #response = requests.get(f'https://imdb-api.com/en/API/Search/k_lblhnjr6/{name}')
        #print(response.status_code)
        #print(response.json())
        #def jprint(obj):
            #text = json.dumps(obj, sort_keys=True, indent=4)
            #print(text)
            #return text
        #jprint(response.json())
        #with open(response.json()) as response:
            #data = json.load(response)
            #print(data)
           # context['movies'] = response.json()
            #context['header'] = f'Searching for {name}'
        #else:
         #   response2 = requests.get("https://imdb-api.com/en/API/Top250Movies/k_lblhnjr6")
          #  context['movies'] = response2.json()
           # context['header'] = 'Top 250 Movies'
        #return context
    
class Books(TemplateView):
    template_name = "books.html"
#APIs Testing code below
    # url = 'http://openlibrary.org/search.json?'
    # response = requests.get(url)
    # data = response.text
    # parse_json = json.loads(data)
    # # print(response.status_code)
    
    # print(data)

class Broadways(TemplateView):
    template_name = "broadways.html"

class CreateList(LoginRequiredMixin, CreateView):
    template_name = "createList.html"

class EditDeleteList(UpdateView, DeleteView):
    template_name = "editDeleteList.html"

class DetailListPage(DetailView):
    template_name = "detailList.html"

class DetailBookPage(DetailView):
    template_name = "detailBook.html"

class DetailBroadwayPage(DetailView):
    template_name = "detailBroadway.html"

class DetailMoviePage(DetailView):
    template_name = "detailMovie.html"

def Profile(request, username):
    user = User.objects.get(username=username)
    list = List.objects.all()
    return render(request, 'profile.html',{'username':username, 'list':list})
    
def Signup(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/' + str(user.username))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})