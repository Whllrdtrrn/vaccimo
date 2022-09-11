from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('login-page/', views.login_page, name='loginpage' ),
    path('register-page/', views.register_page, name='register' ),
    path('information-page/', views.information_page, name='information' ),
    path('side-effect-page/', views.sideeffect_page, name='sideeffect' ),
    path('success-page/', views.success_page, name='success' ),

    path('dashboard/', views.dashboard, name='dashboard' ),
        path("logout_user", views.logout_user, name="logout_user"),




]