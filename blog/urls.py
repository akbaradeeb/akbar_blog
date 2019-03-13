from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/update/$',views.profile_update,name='profile_update'),
    url(r'^profile/blogs/$',views.profile_blogs,name='profile_blogs'),
    url(r'^blog/post-comment/$', views.post_comment, name='post_comment'),
    url(r'^blog/add$', views.add_blog, name='add_blog'),
    url(r'^blog/edit/(?P<id>[0-9]+)$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<slug>[-\w]+)$', views.detail, name='detail')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)