from django.urls import path, reverse_lazy
from . import views

app_name = 'AiAssistant'

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('converseAI/', views.converseAI, name='converseAI'),
    path('details/', views.details, name='details'),
    path('StudentRegister/<int:pk>/update', 
         views.UserDetailsUpdateView.as_view(success_url=reverse_lazy('AiAssistant:details')), name='data_update'),
]
