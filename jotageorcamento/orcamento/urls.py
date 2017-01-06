from django.conf.urls import include
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', ),
    url(r'^accounts/login/$' , login, {'template_name': 'registration/login_gvx.html'}, name="login"),
    url(r'^accounts/logout/$' , logout_then_login, {'login_url':'/login/accounts/login/'}, name="logout"),

]