from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.handle_register_login),
]