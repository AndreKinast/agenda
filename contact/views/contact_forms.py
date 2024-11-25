from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


def create(request):
    if request.method == 'POST':
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
    context = {
       
    }
    return render (
        request,
        'contact/create.html',
        context,     
    )  