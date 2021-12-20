from django.urls import path,re_path
from . import views

# urlpatterns =[ path('',views.post_list), ]
app_name='blog' #without it reverse url don't work

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]

# urlpatterns = [
#     re_path(r'^$', views.post_list, name='post_list'),
#     ]
