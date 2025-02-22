from django.contrib.auth import views as auth_views

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or another view
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
