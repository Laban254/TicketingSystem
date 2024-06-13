# from django.urls import path
# from . import views

app_name = 'accounts'

# urlpatterns = [
#     path('register-customer/', views.register_customer , name='register_customer'),
#     path('login/', views.login_user, name='login'),
#     path('logout/', views.logout_user, name='logout'),
# ]

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
