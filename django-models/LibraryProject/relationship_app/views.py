from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def home(request):
    return render(request, 'list_books')


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Login View
from django.contrib.auth import views as auth_views

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'


# Logout View
class CustomLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')