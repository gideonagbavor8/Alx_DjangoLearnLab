from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def list_books(request):
    # Your logic to retrieve and display books
    books = []  # Replace with actual book retrieval logic
    return render(request, 'relationship_app/book_list.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')  # Redirect to the book list or homepage
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'relationship_app/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
