from django.conf.urls import url
from . import views
urlpatterns = [
    url('file/details/(?P<pk>[0-9]+)/', views.home, name='file_details'),
    # url(r'^messages/$', views.messages,name="messages"),
]