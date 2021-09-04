from django.shortcuts import render, get_object_or_404
from .models import Profile

# Create your views here.
def user_list(request):
    users = Profile.objects.all()
    context = {"user": users}
    return render(request, 'users/user_list.html', context)


def user_detail(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    context = {'user': user}
    return render(request, 'users/user_detail.html', context)