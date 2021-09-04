from django.urls import path
from .views import user_list, user_detail

app_name = 'users'
urlpatterns = [
    path('user-list/', user_list, name='user_list'),
    path('user-detail/<int:user_id>/', user_detail, name='user_detail')

]