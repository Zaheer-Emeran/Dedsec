from django.urls import path
from . import views
#create view, create url for it
urlpatterns = [
    path('',views.home, name='home-page'),
    path('register/',views.register, name='register'),
    path('login/',views.loginPage, name='login'),
    path('delete-task/<str:name>',views.DeleteTask, name='delete'),
    path('update/<str:name>',views.Update, name='update'),
    path('logout/os.environ.get('DATABASE_URL') ',views.logoutView, name='logout'),
    
]