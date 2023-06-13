
from django.contrib import admin
from app.views import webhook
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('webhook/', webhook, name='webhook'),
]