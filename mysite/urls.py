
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import password_reset

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html',
    	'blog.views.view_post',
    	name="view_blog_post"),
    url(r'^blog/category/(?P<slug>[^\.]+).html',
    	'blog.views.view_category',
    	name='view_blog_category'),

    url(r'^login/', 'blog.views.login_user', name='login'),

    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),

    url(r'^logout/', 'blog.views.logout_user', name='logout'),

    url(r'^like/$', 'blog.views.like', name='like'),

    url(r'^reset/', password_reset, {'template_name': 'password_reset.html'}),
  
    url(r'^create_post/$', 'blog.views.create_post', name='create_post'),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),


)

