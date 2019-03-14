from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.ListBlogApi.as_view(),name='location'),
    #url(r'^thanks$',views.thanks,name='thanks')
]