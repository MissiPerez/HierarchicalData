from django.shortcuts import render
from mysite.models import Genre


def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
