from django.conf.urls import url
import views


urlpatterns=[
url(r'^$', views.book_list),
url(r'^detail$', views.detail),
]