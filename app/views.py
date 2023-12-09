import logging
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser as User, LinkUser
from .forms import CustomUserForm as UserForm
from .forms import LinksForm

class general_view(View):
    def get(self, request, slug):
        user = User.objects.get(url=slug)
        links = LinkUser.objects.filter(user__url=slug)
        me = (user == request.user)
        return render(request, 'shareMe/general.html', context={'connect':request.user.is_authenticated, 'user': user, 'links': links, 'me': me})

class create_view(View):
    
    def get(self, request):
        logout(request)
        return render(request, 'shareMe/new_user.html', context={'connect':request.user.is_authenticated, 'form': UserForm()})
    
    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'shareMe/new_user.html', context={'connect':request.user.is_authenticated, 'form': UserForm(), 'error_message': 'Email already exists'})
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('index')
        return render(request, 'shareMe/new_user.html', context={'connect':request.user.is_authenticated, 'form': UserForm()})

class login_view(View):
    def get(self, request):
        return render(request, 'shareMe/login.html')
    
    def post(self, request):
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if not user:
            return render(request, 'shareMe/login.html', {'error_message': 'Invalid credentials'})
        login(request, user)
        return redirect('index')

class index(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        return redirect('view', slug=request.user.url)

class desc_view(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        url = request.user.url
        user = User.objects.get(url=url)
        return render(request, 'shareMe/desc.html', context={'connect':request.user.is_authenticated, 'user': user, 'form': UserForm(instance=user)})
    
    def post(self, request):
        url = request.user.url
        user = User.objects.get(url=url)
        form = UserForm(request.POST, request.FILES, instance=user)
        password = request.POST.get('password')
        if form.is_valid():
            user.url = form.cleaned_data['url']
            user.bio = form.cleaned_data['bio']
            user.avatar = form.cleaned_data['avatar']
            if password:
                user.set_password(password)
            user.save()
            return redirect('index')
        return render(request, 'shareMe/login.html', {'error_message': 'Invalid form'})

class links_view(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        return render(request, 'shareMe/links.html', context={'connect':request.user.is_authenticated, 'form': LinksForm(), 'links': LinkUser.objects.filter(user__url=request.user.url)})
    
    def post(self, request):
        form = LinksForm(request.POST)
        if form.is_valid():
            if LinkUser.objects.filter(user__url=request.user.url, link__name=form.cleaned_data['link'].name).exists():
                link = LinkUser.objects.get(user__url=request.user.url, link__name=form.cleaned_data['link'].name)
                link.url = form.cleaned_data['url']
                link.save()
                return render(request, 'shareMe/links.html', context={'connect':request.user.is_authenticated, 'form': LinksForm(), 'links': LinkUser.objects.filter(user__url=request.user.url), 'error_message': 'Link already exists'})
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return render(request, 'shareMe/links.html', context={'connect':request.user.is_authenticated, 'form': LinksForm(), 'links': LinkUser.objects.filter(user__url=request.user.url)})
        return render(request, 'shareMe/links.html', context={'connect':request.user.is_authenticated, 'form': LinksForm(), 'links': LinkUser.objects.filter(user__url=request.user.url)})

class logout_view(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return redirect('index')
    
class delete_link(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, name):
        try:
            LinkUser.objects.get(user__url=request.user.url, link__name=name).delete()
        except:
            pass
        return redirect('links')