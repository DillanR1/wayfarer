from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form,}
    return render(request, 'home.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
            form = SignUpForm(request.POST)
            if form.is_valid():
            # This will add the user to the database
                user = form.save()
                user.refresh_from_db()
                user.profile.city = form.cleaned_data.get('city')
                user.save()
      # This is how we log a user in via code
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
    else:
        form = SignUpForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)

def profile(request):
    return render(request, 'registration/profile.html')