from django.conf.urls import url
import views


urlpatterns = [
    url(r'^regist$', views.regist),
    url(r'^login$', views.login),
]