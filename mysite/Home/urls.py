from django.conf.urls import url
from mysite import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views


urlpatterns = [
	url(r'^$', views.index, name='home_page'),
]
