
from django.contrib import admin
from django.urls import path, include
from clients import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('clients.urls'))
]
