from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model


from app.forms import CustomUserCreationForm

def index(request):
    return render(request, 'app/index.html')

def users_detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    return render(request, 'app/users_detail.html', {'user': user})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']

            new_user = authenticate(username=input_username, password=input_password)

            if new_user is not None:

                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})




# Create your views here.
