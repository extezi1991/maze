from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  url(r'^$', views.show_page, name='show_page'),


]