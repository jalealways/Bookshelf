from django.conf.urls import url
import views


urlpatterns=[
    url(r'^bookshelf$', views.test),
    url(r'^$', views.weixin),
]