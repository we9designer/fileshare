from django.conf.urls import url
#from . import views
from .views import *

urlpatterns = [
	# File
	url('file/list/', FileList.as_view(), name='file_list'),
	url('file/add/', FileCreate.as_view(), name='file_add'),
	url('file/details/(?P<pk>[0-9]+)/', FileDetail.as_view(), name='file_details'),
	url('file/(?P<pk>[0-9]+)/delete/', FileDelete.as_view(), name='file_delete'),
	url('file/(?P<pk>[0-9]+)/update/', FileUpdate.as_view(), name='file_update'),
]