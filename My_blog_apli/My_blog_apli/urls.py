
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.ulogin,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>',views.update___post,name='updatepost'),
    path('delete/<int:id>',views.delete_post,name='deletepost'),
    
]