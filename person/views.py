from django.shortcuts import render
from django.http import (
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpRequest,
)
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from person.models import Person


class IndexView(ListView):
    model = Person
    template_name = 'person/index.html'
    context_object_name = 'persons'
    allow_empty = True

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        return super().get_queryset()

class PersonDetailView(DetailView):
    model = Person
    template_name = 'person/detail.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


@login_required
def index(request: HttpRequest):
    persons: list[Person] = Person.objects.all()
    context = {"persons": persons}
    return render(request, "person/index.html", context)


@login_required
def detail(request: HttpRequest, person_id: int):
    person: Person = Person.objects.get(id=person_id)
    context = {"person": person}
    return render(request, "person/detail.html", context)


def page_not_found(request: HttpRequest):
    return HttpResponseNotFound()


def server_error(request: HttpRequest):
    return HttpResponseServerError()
