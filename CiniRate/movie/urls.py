from django.urls import path 
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    
    #movie details
    path('movie<int:movie_id>/',views.movie_detail, name='movie_detail'),
    
    #auth
    path('register/', views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    #reviews
    path('review<int:review_id>/edit',views.edit_review,name='edit_review'),
    path('review<int:review_id>/delete/',views.delete_review,name='delete_review'),
]