from django.shortcuts import render, get_object_or_404, redirect
from .models import Clothes


def filtr_clothes_new(request):
    filtr = Clothes.objects.all().order_by('-created')
    return redirect('dashboard')

def filtr_clothes_old(request):
    filtr = Clothes.objects.all().order_by('created')
