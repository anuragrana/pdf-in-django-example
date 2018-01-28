from django.conf.urls import url
from testapp import views

app_name = "testapp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
