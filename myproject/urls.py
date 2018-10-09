from django.contrib import admin
from django.urls import path

from keywords import views

urlpatterns = [
	path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls'))
]
