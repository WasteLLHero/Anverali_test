
from django.contrib import admin
from django.urls import include, path

from offices.views import registration


urlpatterns = [
    path('admin/', admin.site.urls),        
    path('accounts/registration/', registration),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("offices.urls")),  
]
