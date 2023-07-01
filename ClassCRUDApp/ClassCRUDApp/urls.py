from django.contrib import admin
from django.urls import path, include
from CrudApp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('CrudApp.urls')),
]
