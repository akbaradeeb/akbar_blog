from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^signup',views.signup,name='signup'),
    url(r'^blog/post-comment/$', views.post_comment, name='post_comment'),
    url(r'^blog/add$', views.add_blog, name='add_blog'),
    url(r'^blog/(?P<slug>[-\w]+)$', views.detail, name='detail')
]