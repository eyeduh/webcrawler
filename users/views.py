from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def user_list(request):
    users = Profile.objects.all()
    context = {"user": users}
    return render(request, 'users/user_list.html', context)


def user_detail(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    context = {'user': user}
    return render(request, 'users/user_detail.html', context)

def register_request(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.phone_number = form.cleaned_data.get('phone number')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('/')
        
    else:
        messages.error(request, "Unsuccessful Registration. Invalid Information.")
        form = SignUpForm()
    return render(request, 'users/register.html', context={'form':form})