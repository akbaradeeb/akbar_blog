from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^blog/(?P<slug>[-\w]+)$',views.detail,name='detail'),
    url(r'^login$',views.login,name='login'),
    url(r'^signup',views.signup,name='signup')
]