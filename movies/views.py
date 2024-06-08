from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies'  : [
        {
            'id' : 5,
            'title' : 'jaws',
            'year' : 1669,
        },
        {
            'id' : 6,
            'title' : 'Sharkendo',
            'year' : 1660,
        },
        {
            'id' : 5,
            'title' : 'The Mag',
            'year' : 1669,
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html' , data)


def home(request):
    return HttpResponse("Welcome to Home Page.")