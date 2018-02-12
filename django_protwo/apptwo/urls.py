from django.conf.urls import url
from apptwo import views

#Use namespaces with template tagging and relative urls
app_name = 'apptwo'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),
    url(r'^index/$',views.index,name='index'),
]
