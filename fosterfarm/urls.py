"""
urls stuff
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include
import basicapp.views 
import signup.views
from django.urls import path

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', basicapp.views.index),
    path('home/', basicapp.views.home),
    path('signup/', signup.views.Signup),
    path('thanks/', signup.views.thanks),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
