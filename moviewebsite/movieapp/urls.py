from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'movieapp'
urlpatterns = [
    path('',views.allMovieCat,name='home'),
    path('<slug:c_slug>/',views.allMovieCat,name='movie_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.movieDetail,name='movieCatDetail'),
    path('movies',views.movieadd,name='movieadd'),
    path('<slug:c_slug>/<slug:product_slug>/delete',views.delete,name='delete'),
    path('<slug:c_slug>/<slug:product_slug>/update',views.update,name='update'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
]