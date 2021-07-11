from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reklam, News, Category, SubCategory, FirmReklam, Brands, UserReklam
from .forms import CreateReklam, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_list(request):
    users = UserReklam.objects.filter(is_active=True)
    return render(request, 'user/user.html', {'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(UserReklam, username=username, is_active=True)
    return render(request, 'user/user_detail.html', {'user': user})


@login_required
def index(request):
    news = News.objects.all().order_by('-date', 'spec', '-name')
    category = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {'news': news, 'subcategories': subcategories, 'category': category, 'section': 'dashboard',}
    return render(request, 'index.html', context)


def brands(request):
    reklams = Reklam.objects.all().order_by('name')
    context = {'news': news, 'reklams': reklams, 'section': 'brands'}
    return render(request, 'brand/brands.html', context)


def brands_detail(request, brand_id):
    news = News.objects.all()
    brand = Brands.objects.get(pk=brand_id)
    category = Category.objects.all()
    firms = FirmReklam.objects.all()
    brand_reklams = Reklam.objects.filter(brand=brand_id).order_by('name')
    context = {'news': news, 'brand_reklams': brand_reklams, 'category': category, 'firms': firms,  'brand': brand}
    return render(request, 'brand/brand.html', context)


def category(request, cat_id):
    reklams = Reklam.objects.filter(category=cat_id)
    category = Category.objects.all()
    default_category = SubCategory.objects.get(pk=cat_id)
    context = {'news': news, 'reklams': reklams, 'category': category, 'section': 'category',
               'default_category': default_category}
    return render(request, 'category/category.html', context)


def news(request):
    context = {'news': news, 'section': 'news'}
    return render(request, 'news.html', context)


def by_categories(request, cat_id):
    reklams = Reklam.objects.filter(category=cat_id)
    cur_subcategory = SubCategory.objects.get(pk=cat_id)
    news = News.objects.all()
    context = {'news': news, 'reklams': reklams, 'cur_subcategory': cur_subcategory}
    return render(request, 'subcategory/subcategory_detail.html', context)


def subcategory(request, cat_id):
    reklams = Reklam.objects.filter(category=cat_id)
    default_category = SubCategory.objects.get(pk=cat_id)
    news = News.objects.all()
    context = {'news': news, 'reklams': reklams, 'category': category,
               'default_category': default_category}
    return render(request, 'subcategory/subcategory.html', context)


def by_subcategory(request, subcat_id):
    reklams = Reklam.objects.filter(category=subcat_id)
    cur_category = SubCategory.objects.get(pk=subcat_id)
    categories = SubCategory.objects.all()
    news = News.objects.all()
    context = {'news': news, 'reklams': reklams, 'categories': categories, 'cur_category': cur_category}
    return render(request, 'by_categrories.html', context)


def by_brand(request, cat_id):
    reklams = Reklam.objects.filter(category=cat_id)
    cur_category = SubCategory.objects.get(pk=cat_id)
    specs = Category.objects.all()
    categories = SubCategory.objects.all()
    news = News.objects.all()
    context = {'news': news, 'reklams': reklams, 'categories': categories, 'cur_category': cur_category, 'specs': specs}
    return render(request, 'by_categrories.html', context)


class infoView(DetailView):
    model = Reklam
    template_name = 'products/info_list.html'
    context_object_name = 'info'


class infoFirmReklams(DetailView):
    model = FirmReklam
    template_name = 'products/info_list.html'
    context_object_name = 'infofirm'








