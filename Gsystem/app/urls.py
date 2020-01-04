from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    path('signup/', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('JHstart/',views.JHstart,name='JHstart'),
    path('Hstart/',views.Hstart,name='Hstart'),
    path('JHquestion/',views.JHquestion,name='JHquestion'),
    path('Hquestion/',views.Hquestion,name='Hquestion'),
    path('answer/',views.answer,name='answer'),
]
