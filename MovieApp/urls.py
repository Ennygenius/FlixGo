from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('details/<str:pk>/', views.movie_details, name='movie_details'),
]