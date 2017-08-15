from django.conf.urls import url
import views


urlpatterns=[
url(r'^$', views.list),
url(r'^detail$', views.detail),
]