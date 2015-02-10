from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from materials import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'materials.views.hello', name='hello'),
    # url(r'^hello_template/$', 'materials.views.home_template'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_template, name='home_template'), 
    url(r'^mat/', views.materials_list, name='materials_list'),
    url(r'^add/', views.add, name='add'), 
    #not sure why name='add'; it's unnecessary
    
    # ex: /5/
    url(r'^(?P<material_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<material_id>\d+)/$', views.add_material, name='add_material'),
    
    url(r'^create/$', views.create, name='create'),
    url(r'^create_job/$', views.create_job, name='create_job'),
    
    # hello_template is the function defined in views.py
    )
